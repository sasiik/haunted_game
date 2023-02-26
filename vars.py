from util_funcs import *
import tkinter

# commented for debug reasons. currently using custom screen values
# screen_width = tkinter.Tk().winfo_screenwidth()
# screen_height = tkinter.Tk().winfo_screenheight()


screen_width = 1280
screen_height = 720
scaling_value = 1.5
screen, size, scale = init_pygame_screen(screen_width, screen_height, scaling_value)

# FPS value
FPS = 60

# tile parameters
tile_width = tile_height = 50
animations_frames_count = 5

# sprite groups
game_sprites = pygame.sprite.Group()
menu_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


# buttons parameters
navbtns_width, navbtns_height = 100, 100
menu_logo_width, menu_logo_height = 700, 150

# player value idk???
player = None
