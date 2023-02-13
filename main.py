import os
import sys
import tkinter as tk

import pygame


def init_pygame_screen():
    root = tk.Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    pygame.init()
    size = screen_width, screen_height
    screen = pygame.display.set_mode(size)

    return screen, size


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


screen, size = init_pygame_screen()
FPS = 60


def load_level(filename):
    filename = "levels/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


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


tile_images = {
}

tile_width = tile_height = 50
animations_frames_count = 5


class AnimatedInstance:
    # переписать лого меню и сделать родительским классом баттона
    pass


class Button:
    def __init__(self, x, y, animation, scale):
        self.width = animation[0].get_width()
        self.height = animation[0].get_height()
        if scale != 1:
            for i in range(len(animation)):
                animation[i] = pygame.transform.scale(animation[i], (int(self.width*scale), int(self.height*scale)))
        self.anim = animation
        print(self.anim)
        self.rect = self.anim[0].get_rect()
        self.rect.topleft = (x, y)

    def draw(self, frame):
        screen.blit(self.anim[frame], (self.rect.x, self.rect.y))


logo_animation = []
menu_logo_width, menu_logo_height = 700, 150
playbtn_animation = []
settings_btn_animation = []
navbtns_width, navbtns_height = 100, 100
for i in range(1, animations_frames_count + 1):
    logo_animation.append(load_image(f'mainmenu/menu_logo_{i}.png'))
    playbtn_animation.append(load_image(f'mainmenu/play_button_{i}.png'))
    settings_btn_animation.append(load_image(f'mainmenu/settings_logo_{i}.png'))

scale = 1.5
play_button = Button(size[0] // 4, size[1] - 300, playbtn_animation, scale=scale)
settings_btn = Button(size[0] - size[0] // 4 - navbtns_width*scale, size[1] - 300, settings_btn_animation, scale=scale)


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

        screen.blit(logo_animation[frame], (size[0] // 2 - menu_logo_width // 2, menu_logo_height))
        play_button.draw(frame)
        settings_btn.draw(frame)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        pygame.display.flip()
        clock.tick(FPS)


player_image = pygame.transform.scale(load_image('game/hero_forward_1.png'), (tile_width, tile_height))

# основной персонаж
player = None

# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.init_location()

    def init_location(self):
        self.rect = self.image.get_rect().move(
            tile_width * self.pos_x, tile_height * self.pos_y)
        print(self.rect)

    def move(self, dir):
        if dir == 'L':
            self.pos_x -= 1
        elif dir == 'R':
            self.pos_x += 1
        elif dir == 'U':
            self.pos_y -= 1
        elif dir == 'D':
            self.pos_y += 1
        self.init_location()


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


if __name__ == '__main__':
    screen = pygame.display.set_mode(size)
    running = True
    # camera = Camera()
    clock = pygame.time.Clock()
    start_screen()
    # player, level_x, level_y = generate_level(load_level('level1.txt'))
    # camera.init_camera(tiles_group, player_group)
    while running:
        screen.fill(pygame.color.Color('white'))
        # обновляем положение всех спрайтов
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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
        clock.tick(FPS)
    pygame.quit()
