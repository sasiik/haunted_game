import sys
import random
import pygame
from AnimatedObjects import AnimatedObject, load_image
from vars import tiles_group, player_group, FPS, screen_height, screen_width, game_sprites
from typing import Tuple

FORWARD_ANIMATION = 'forward'
BACKWARD_ANIMATION = 'backward'
LEFT_ANIMATION = 'left'
RIGHT_ANIMATION = 'right'


class Player(AnimatedObject):
    @classmethod
    def get_root_path(cls, animation_id: str) -> str:
        return f'game/hero_{animation_id}'

    def draw(self, screen):
        pass
        # screen.blit(self.anim[self.frame], (self.rect.x, self.rect.y))

    def __init__(self, x, y, anim_cooldown, scale):
        self.animation_id = FORWARD_ANIMATION
        self.velocity = 5
        self.direction = FORWARD_ANIMATION
        super().__init__(x, y, self.get_root_path(self.animation_id), 5, anim_cooldown, scale)
        self.max_x = screen_width - self.rect.width
        self.max_y = screen_height - self.rect.height

        self.animations = {
            animation_id: AnimatedObject.upload_images(self.get_root_path(animation_id), animations_frames_count=5,
                                                       colorkey=-1) for
            animation_id in [FORWARD_ANIMATION, BACKWARD_ANIMATION, LEFT_ANIMATION, RIGHT_ANIMATION]
        }
        for animations in self.animations.values():
            self.scaling(self.scale, animations)

        self.anim = self.animations[self.animation_id]

    def change_animation(self, dir):
        if dir == 'L':
            self.animation_id = LEFT_ANIMATION
        elif dir == 'R':
            self.animation_id = RIGHT_ANIMATION
        elif dir == 'U':
            self.animation_id = BACKWARD_ANIMATION
        elif dir == 'D':
            self.animation_id = FORWARD_ANIMATION

        self.anim = self.animations[self.animation_id]

    def tick(self):
        dx, dy = 0, 0
        if self.animation_id == LEFT_ANIMATION:
            dx = -1
        elif self.animation_id == RIGHT_ANIMATION:
            dx = 1
        elif self.animation_id == BACKWARD_ANIMATION:
            dy = -1
        elif self.animation_id == FORWARD_ANIMATION:
            dy = 1

        new_x = self.x + dx * self.velocity
        new_y = self.y + dy * self.velocity

        self.x = min(self.max_x, max(0, new_x))
        self.y = min(self.max_y, max(0, new_y))


class Tile(pygame.sprite.Sprite):

    @classmethod
    def get_tile_dimensions(cls, scale) -> Tuple[int, int]:
        image = load_image("game/tile_sprite.png")
        return pygame.transform.scale(
            image, (int(image.get_width() * scale), int(image.get_height() * scale))
        ).get_size()

    def __init__(self, tile_type, pos_x, pos_y, scale: float):
        super().__init__(tiles_group, game_sprites)
        if not isinstance(scale, float):
            raise TypeError('Scale must be float')

        self.scale = scale
        self.image = load_image('game/tile_sprite.png')
        width, height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(width * scale), int(height * scale)))
        self.image = pygame.transform.rotate(self.image, random.choice([0, 90, 180, 270]))

        width, height = self.image.get_size()
        self.rect = self.image.get_rect().move(
            width * pos_x, height * pos_y)


# class Camera:
#     # зададим начальный сдвиг камеры
#     def __init__(self):
#         self.dx = 0
#         self.dy = 0
#
#     # сдвинуть объект obj на смещение камеры
#     def apply(self, obj):
#         obj.rect.x -= self.past_dx
#         obj.rect.y -= self.past_dy
#         obj.rect.x += self.dx
#         obj.rect.y += self.dy
#
#     def apply_target(self, target):
#         target.rect.x += self.dx
#         target.rect.y += self.dy
#
#     # позиционировать камеру на объекте target
#     def update(self, target):
#         self.past_dx = self.dx
#         self.past_dy = self.dy
#         self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
#         self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)
#         print(self.dx)
#
#     def init_camera(self, tiles_group, player_group):
#         camera.update(player)
#         for sprite in tiles_group:
#             camera.apply(sprite)
#         for sprite in player_group:
#             camera.apply_target(sprite)


def generate_level(tiles_number_in_width, tiles_number_in_height, scale: float):
    for y in range(tiles_number_in_height):
        for x in range(tiles_number_in_width):
            Tile('empty', x, y, scale=scale)


def play_game(screen, size, scale: float):
    clock = pygame.time.Clock()
    running = True

    generate_level(40, 40, scale=scale)
    player = Player(0, 0, 150.0, scale)
    player_group.add([player])

    while running:
        screen.fill(pygame.color.Color('black'))
        # обновляем положение всех спрайтов
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_UP:
                    player.change_animation('U')
                elif event.key == pygame.K_DOWN:
                    player.change_animation('D')
                elif event.key == pygame.K_LEFT:
                    player.change_animation('L')
                elif event.key == pygame.K_RIGHT:
                    player.change_animation('R')

        player.tick()
        # camera.init_camera(tiles_group, player_group)
        tiles_group.draw(screen)
        player_group.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
