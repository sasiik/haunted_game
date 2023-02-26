from game_process import *
from vars import *

logo = AnimatedObject(size[0] // 2 - menu_logo_width * scale[0] // 2, 100 * scale[1], 'mainmenu/menu_logo', 5,
                      scale, menu_sprites)
play_button = Button(size[0] // 4, size[1] - 200 * scale[1], play_game, 'mainmenu/play_button', 5, scale, menu_sprites)
settings_btn = Button(size[0] - size[0] // 4 - navbtns_width * scale[0], size[1] - 200 * scale[1], True,
                      'mainmenu/settings_button',
                      5,
                      scale, menu_sprites)
