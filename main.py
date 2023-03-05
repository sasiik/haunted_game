from init_funcs import init_pygame_screen, init_scale
from menu import menu_screen
from vars import screen_width, screen_height, scaling_value

if __name__ == '__main__':
    screen, size = init_pygame_screen(screen_width, screen_height)
    # size не нужен, фикс
    scale = init_scale(size[0], size[1], scaling_value)
    menu_screen(screen, size, scale)
    # camera = Camera()

    # start_screen()
    # # player, level_x, level_y = generate_level(load_level('level1.txt'))
    # # camera.init_camera(tiles_group, player_group)
    # clock.tick(FPS)
    # pygame.quit()
