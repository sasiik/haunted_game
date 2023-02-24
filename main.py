import os
import sys
import tkinter as tk

import pygame


def init_pygame_screen():
    root = tk.Tk()

    # screen_width = root.winfo_screenwidth()
    # screen_height = root.winfo_screenheight()
    screen_width = 1280
    screen_height = 720
    w_scale = screen_width / 1920 * 1.5
    h_scale = screen_height / 1080 * 1.5
    scale = (w_scale, h_scale)

    pygame.init()
    size = screen_width, screen_height
    screen = pygame.display.set_mode(size)

    return screen, size, scale


def load_image(name, colorkey=None):
    fullname = os.path.join('sprites', name)
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


screen, size, scale = init_pygame_screen()
FPS = 60


# def load_level(filename):
#     filename = "levels/" + filename
#     with open(filename, 'r') as mapFile:
#         level_map = [line.strip() for line in mapFile]
#
#     max_width = max(map(len, level_map))
#     return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def terminate():
    pygame.quit()
    sys.exit()


#
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


tile_width = tile_height = 50
animations_frames_count = 5

# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


class AnimatedObject:
    def __init__(self, x, y, animation, scale):
        self.width = animation[0].get_width()
        self.height = animation[0].get_height()
        self.anim = animation
        self.scaling(scale)
        self.rect = self.anim[0].get_rect()
        self.rect.topleft = (x, y)

    def draw(self, frame):
        screen.blit(self.anim[frame], (self.rect.x, self.rect.y))

    def scaling(self, scale):
        if scale != (1, 1):
            for i in range(len(self.anim)):
                self.anim[i] = pygame.transform.scale(self.anim[i],
                                                      (int(self.width * scale[0]), int(self.height * scale[1])))


class Button(AnimatedObject):
    def __init__(self, x, y, animation, scale, action):
        super().__init__(x, y, animation, scale)
        self.clicked = False
        self.action = action

    def initialize(self, frame):
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

class Player(pygame.sprite.Sprite, AnimatedObject):
    def __init__(self, pos_x, pos_y, animation, scale):
        super().__init__(player_group, all_sprites, animation, scale)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.scaling(scale)

    def move(self, dir):
        if dir == 'L':
            self.pos_x -= 1
        elif dir == 'R':
            self.pos_x += 1
        elif dir == 'U':
            self.pos_y -= 1
        elif dir == 'D':
            self.pos_y += 1


def play_game():
    running = True
    while running:
        screen.fill(pygame.color.Color('black'))
        # обновляем положение всех спрайтов
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                terminate()
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


player_animations = {'forward': [], 'backward': [], 'left': [], 'right': []}
logo_animation = []
menu_logo_width, menu_logo_height = 700, 150
playbtn_animation = []
settings_btn_animation = []
navbtns_width, navbtns_height = 100, 100
for i in range(1, animations_frames_count + 1):
    logo_animation.append(load_image(f'mainmenu/menu_logo_{i}.png'))
    playbtn_animation.append(load_image(f'mainmenu/play_button_{i}.png'))
    settings_btn_animation.append(load_image(f'mainmenu/settings_logo_{i}.png'))
    for key in player_animations.keys():
        for i in range(1, animations_frames_count + 1):
            player_animations[key].append(f'game/hero_{key}_{i}')

play_button = Button(size[0] // 4, size[1] - 200 * scale[1], playbtn_animation, scale=scale, action=play_game)
settings_btn = Button(size[0] - size[0] // 4 - navbtns_width * scale[0], size[1] - 200 * scale[1],
                      settings_btn_animation,
                      scale=scale, action=True)
logo = AnimatedObject(size[0] // 2 - menu_logo_width * scale[0] // 2, 100 * scale[1], logo_animation, scale=scale)

player_image = pygame.transform.scale(load_image('game/hero_forward_1.png'), (tile_width, tile_height))
# основной персонаж
player = None


def start_screen():
    frame = 0
    last_upd = pygame.time.get_ticks()
    anim_cooldown = 150
    while True:
        screen.fill(pygame.Color('black'))

        current_time = pygame.time.get_ticks()
        if current_time - last_upd >= anim_cooldown:
            frame += 1
            last_upd = current_time
            if frame >= len(logo_animation):
                frame = 0

        logo.draw(frame)
        play_button.initialize(frame)
        settings_btn.initialize(frame)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    screen = pygame.display.set_mode(size)
    # camera = Camera()
    clock = pygame.time.Clock()
    start_screen()
    # player, level_x, level_y = generate_level(load_level('level1.txt'))
    # camera.init_camera(tiles_group, player_group)
    clock.tick(FPS)
    pygame.quit()
