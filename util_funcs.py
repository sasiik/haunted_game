import os
import sys

import pygame


def init_pygame_screen(screen_width, screen_height, scaling_value):
    w_scale = screen_width / 1920 * scaling_value
    h_scale = screen_height / 1080 * scaling_value
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



def terminate():
    pygame.quit()
    sys.exit()
