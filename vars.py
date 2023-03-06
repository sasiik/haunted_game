import tkinter

import pygame

# commented for debug reasons. currently using custom screen values
screen_width = tkinter.Tk().winfo_screenwidth()
screen_height = tkinter.Tk().winfo_screenheight()



scaling_value = 1.5

# FPS value
FPS = 60

# tile parameters
tile_width = tile_height = 100
animations_frames_count = 5
anim_cooldown = 150

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
