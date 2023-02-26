from game_process import *

logo = AnimatedObject(size[0] // 2 - menu_logo_width * scale[0] // 2, 100 * scale[1], logo_animation, scale=scale)
play_button = Button(size[0] // 4, size[1] - 200 * scale[1], playbtn_animation, scale=scale, action=play_game)
settings_btn = Button(size[0] - size[0] // 4 - navbtns_width * scale[0], size[1] - 200 * scale[1],
                      settings_btn_animation,
                      scale=scale, action=True)
