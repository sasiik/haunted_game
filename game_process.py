from game_objs import *


# def generate_level(level):
#     new_player, x, y = None, None, None
#     for y in range(len(level)):
#         for x in range(len(level[y])):
#             if level[y][x] == '.':
#                 Tile('empty', x, y)
#             elif level[y][x] == '#':
#                 Tile('wall', x, y)
#             elif level[y][x] == '@':
#                 Tile('empty', x, y)
#                 new_player = Player(x, y)
#     # вернем игрока, а также размер поля в клетках
#     return new_player, x, y

# def load_level(filename):
#     filename = "levels/" + filename
#     with open(filename, 'r') as mapFile:
#         level_map = [line.strip() for line in mapFile]
#
#     max_width = max(map(len, level_map))
#     return list(map(lambda x: x.ljust(max_width, '.'), level_map))

def play_game():
    running = True
    while running:
        screen.fill(pygame.color.Color('black'))
        # обновляем положение всех спрайтов
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    # player.move('U')
                    pass
                elif event.key == pygame.K_DOWN:
                    # player.move('D')
                    pass
                elif event.key == pygame.K_LEFT:
                    # player.move('L')
                    pass
                elif event.key == pygame.K_RIGHT:
                    #  player.move('R')
                    pass
            # camera.init_camera(tiles_group, player_group)
        tiles_group.draw(screen)
        player_group.draw(screen)
        pygame.display.flip()
