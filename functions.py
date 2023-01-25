import os
import pygame
import sys
import constants
from classes import Tile, Player


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Чтобы подпрыгнкть нажмите стрелку вверх или пробел",
                  "Чтобы начать играть выберете уровень сложности используя цифры на клавиатуре (от 1 до 6)"]

    fon = pygame.transform.scale(load_image('background_start_screen.jpg'), (constants.WIDTH, constants.HEIGHT))
    constants.SCREEN.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        constants.SCREEN.blit(string_rendered, intro_rect)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    constants.DIFFICULTY = 1
                    running = False
                if event.key == pygame.K_2:
                    constants.DIFFICULTY = 2
                    running = False
                if event.key == pygame.K_3:
                    constants.DIFFICULTY = 3
                    running = False
                if event.key == pygame.K_4:
                    constants.DIFFICULTY = 4
                    running = False
                if event.key == pygame.K_5:
                    constants.DIFFICULTY = 5
                    running = False
                if event.key == pygame.K_6:
                    constants.DIFFICULTY = 6
                    running = False
        pygame.display.flip()
        constants.CLOCK.tick(constants.FPS)

    pygame.time.delay(1000)


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('spike', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    return new_player, x, y


def load_level(filename):
    filename = "data/levels/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))