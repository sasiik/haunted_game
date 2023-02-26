from util_funcs import *

screen, size, scale = init_pygame_screen()

FPS = 60

tile_width = tile_height = 50
animations_frames_count = 5

# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

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


player_image = pygame.transform.scale(load_image('game/hero_forward_1.png'), (tile_width, tile_height))
# основной персонаж
player = None

