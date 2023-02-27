import pygame


def init_pygame_screen(screen_width, screen_height):
    pygame.init()
    size = screen_width, screen_height
    screen = pygame.display.set_mode(size)
    return screen, size


def init_scale(screen_width, screen_height, scaling_value):
    w_scale = screen_width / 1920 * scaling_value
    h_scale = screen_height / 1080 * scaling_value
    scale = (w_scale, h_scale)

    return scale
