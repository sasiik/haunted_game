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


def terminate():
    pygame.quit()
    sys.exit()
