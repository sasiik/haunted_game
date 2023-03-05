import os
import sys
from typing import List
import pygame.sprite


def load_image(name, colorkey=None):
    fullname = os.path.join("sprites", name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class AnimatedObject(pygame.sprite.Sprite):
    def __init__(self, x, y, root_path, frames_count, anim_cooldown, scale):
        super().__init__()
        self.anim = self.upload_images(root_path, frames_count)
        self.frame = 0
        self.animations_frames_count = frames_count
        self.cooldown = anim_cooldown
        self.last_upd = 0
        self.width = self.anim[0].get_width()
        self.height = self.anim[0].get_height()
        self.scale = scale
        self.scaling(self.scale, self.anim)
        self.rect = self.anim[0].get_rect()
        self.rect.topleft = (x, y)

    @property
    def x(self):
        return self.rect.x

    @x.setter
    def x(self, value):
        self.rect.x = value

    @property
    def y(self):
        return self.rect.y

    @y.setter
    def y(self, value):
        self.rect.y = value


    # changed upload images algo
    @classmethod
    def upload_images(cls, root_path, animations_frames_count):
        return [load_image(f"{root_path}_{i}.png") for i in range(1, animations_frames_count + 1)]

    def draw(self, screen):
        screen.blit(self.anim[self.frame], (self.rect.x, self.rect.y))

    def scaling(self, scale, animation):
        if scale != (1, 1):
            for i in range(len(animation)):
                animation[i] = pygame.transform.scale(
                    animation[i], (int(self.width * scale[0]), int(self.height * scale[1]))
                )

    def flip_frame(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_upd >= self.cooldown:
            self.frame += 1
            self.last_upd = current_time
            if self.frame >= len(self.anim):
                self.frame = 0

    @property
    def image(self):
        self.flip_frame()
        return self.anim[self.frame]

class Button(AnimatedObject):
    def __init__(self, x, y, action, root_path, frames_count, anim_cooldown, scale, *groups):
        super().__init__(x, y, root_path, frames_count, anim_cooldown, scale, *groups)
        self.clicked = False
        self.action = action

    def draw(self, screen):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                return self.action()
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        screen.blit(self.anim[self.frame], (self.rect.x, self.rect.y))
