from gif import *


#idk bout player yet
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


class Button(AnimatedObject):
    def __init__(self, x, y, action, root_path, frames_count, scale, *groups):
        super().__init__(x, y, root_path, frames_count, scale, *groups)
        self.clicked = False
        self.action = action

    def draw(self, frame):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                return self.action()

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        screen.blit(self.anim[frame], (self.rect.x, self.rect.y))

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
