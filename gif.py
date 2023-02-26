import pygame.sprite

from vars import *


class AnimatedObject(pygame.sprite.Sprite):
    def __init__(self, x, y, root_path, frames_count, scale, *groups):
        super().__init__(*groups)
        self.frame = 0
        self.animations_frames_count = frames_count
        self.upload_images([], root_path, animations_frames_count)
        self.width = self.anim[0].get_width()
        self.height = self.anim[0].get_height()
        self.scaling(scale)
        self.rect = self.anim[0].get_rect()
        self.rect.topleft = (x, y)

    # changed upload images algo
    def upload_images(self, animation, root_path, animations_frames_count):
        for i in range(1, animations_frames_count + 1):
            animation.append(load_image(f'{root_path}_{i}.png'))
        self.anim = animation

    def draw(self, screen, frame):
        screen.blit(self.anim[frame], (self.rect.x, self.rect.y))

    def scaling(self, scale):
        if scale != (1, 1):
            for i in range(len(self.anim)):
                self.anim[i] = pygame.transform.scale(self.anim[i],
                                                      (int(self.width * scale[0]), int(self.height * scale[1])))
