import sys

import pygame
from AnimatedObjects import AnimatedObject
from vars import tiles_group, player_group


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
        super().__init__(x, y, self.get_root_path(self.animation_id), 5, anim_cooldown, scale)
        self.animations = {
            animation_id: AnimatedObject.upload_images(self.get_root_path(animation_id), animations_frames_count=5) for animation_id in [FORWARD_ANIMATION, BACKWARD_ANIMATION, LEFT_ANIMATION, RIGHT_ANIMATION]
        }

    def move(self, dir):
        if dir == 'L':
            self.animation_id = LEFT_ANIMATION
        elif dir == 'R':
            self.animation_id = RIGHT_ANIMATION
        elif dir == 'U':
            self.animation_id = BACKWARD_ANIMATION
        elif dir == 'D':
            self.animation_id = FORWARD_ANIMATION

        self.anim = self.animations[self.animation_id]


# class Tile(pygame.sprite.Sprite):
#     def __init__(self, tile_type, pos_x, pos_y):
#         super().__init__(tiles_group, all_sprites)
#         self.image = tile_images[tile_type]
#         self.rect = self.image.get_rect().move(
#             tile_width * pos_x, tile_height * pos_y)

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


# def generate_level(level):
#     new_player, x, y = None, None, None
#     for y in range(len(level)):
#         for x in range(len(level[y])):
#             if level[y][x] == '.':
#                 Tile('empty', x, y)
#             elif level[y][x] == '#':
#                 Tile('wall', x, y)
#             elif level[y][x] == '@':
#                 Tile('empty', x, y)
#                 new_player = Player(x, y)
#     # вернем игрока, а также размер поля в клетках
#     return new_player, x, y

# def load_level(filename):
#     filename = "levels/" + filename
#     with open(filename, 'r') as mapFile:
#         level_map = [line.strip() for line in mapFile]
#
#     max_width = max(map(len, level_map))
#     return list(map(lambda x: x.ljust(max_width, '.'), level_map))

def play_game(screen, size, scale):
    running = True

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
                if event.key == pygame.K_UP:
                    player.move('U')
                elif event.key == pygame.K_DOWN:
                    player.move('D')
                elif event.key == pygame.K_LEFT:
                    player.move('L')
                elif event.key == pygame.K_RIGHT:
                    player.move('R')
            # camera.init_camera(tiles_group, player_group)
        player_group.draw(screen)
        pygame.display.flip()
