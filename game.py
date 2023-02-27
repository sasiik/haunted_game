import sys

import pygame
from AnimatedObjects import AnimatedObject
from vars import tiles_group, player_group


class Player(AnimatedObject, pygame.sprite.Sprite):
    def __init__(self, x, y, root_path, frames_count, scale):
        super().__init__(x, y, root_path, frames_count, scale)

    # def move(self, dir):
    #     if dir == 'L':
    #         self.pos_x -= 1
    #     elif dir == 'R':
    #         self.pos_x += 1
    #     elif dir == 'U':
    #         self.pos_y -= 1
    #     elif dir == 'D':
    #         self.pos_y += 1


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

def play_game(screen):
    running = True
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
                    # player.move('U')
                    pass
                elif event.key == pygame.K_DOWN:
                    # player.move('D')
                    pass
                elif event.key == pygame.K_LEFT:
                    # player.move('L')
                    pass
                elif event.key == pygame.K_RIGHT:
                    #  player.move('R')
                    pass
            # camera.init_camera(tiles_group, player_group)
        tiles_group.draw(screen)
        player_group.draw(screen)
        pygame.display.flip()
