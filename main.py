from instances import *

# невозможно переместить изза 'clock', который находится в if запускающем
def start_screen():
    frame = 0
    last_upd = pygame.time.get_ticks()
    anim_cooldown = 150
    while True:
        screen.fill(pygame.Color('black'))

        current_time = pygame.time.get_ticks()
        if current_time - last_upd >= anim_cooldown:
            frame += 1
            last_upd = current_time
            if frame >= len(logo_animation):
                frame = 0

        logo.draw(frame)
        play_button.initialize(frame)
        settings_btn.initialize(frame)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    screen = pygame.display.set_mode(size)
    # camera = Camera()
    clock = pygame.time.Clock()
    start_screen()
    # player, level_x, level_y = generate_level(load_level('level1.txt'))
    # camera.init_camera(tiles_group, player_group)
    clock.tick(FPS)
    pygame.quit()
