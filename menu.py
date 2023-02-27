import sys

import pygame

from AnimatedObjects import AnimatedObject, Button
from vars import menu_logo_width, navbtns_width, menu_sprites, FPS
from game import play_game


def create_menu_objects(screen_size, scale, settings_func, play_game_func):
    AnimatedObject(screen_size[0] // 2 - menu_logo_width * scale[0] // 2, 100 * scale[1], 'mainmenu/menu_logo',
                   5,
                   150,
                   scale, menu_sprites)
    Button(screen_size[0] // 4, screen_size[1] - 200 * scale[1], play_game_func, 'mainmenu/play_button',
           5,
           150,
           scale, menu_sprites)
    Button(screen_size[0] - screen_size[0] // 4 - navbtns_width * scale[0],
           screen_size[1] - 200 * scale[1], settings_func,
           'mainmenu/settings_button',
           5,
           150,
           scale, menu_sprites)


def menu_screen(screen, size, scale):
    clock = pygame.time.Clock()
    create_menu_objects(size, scale, True, lambda: play_game(screen))
    while True:
        screen.fill(pygame.Color('black'))
        for sprite in menu_sprites:
            sprite.flip_frame()
            sprite.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        clock.tick(FPS)
