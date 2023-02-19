import os
import pygame
import sys

import classes
import constants
import random


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
                  "Чтобы подпрыгнуть нажмите стрелку вверх или пробел",
                  "Чтобы начать играть нажмите любую клавишу"]

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
                running = False
        pygame.display.flip()
        constants.CLOCK.tick(constants.FPS)

    pygame.time.delay(1000)


def draw_spikes(screen):
    color = "black"
    for elem in constants.SPIKE_GROUP:
        pygame.draw.circle(screen, color, (elem.x0, elem.y0), 10)
        pygame.draw.polygon(screen, color, [elem.a1, elem.b1, elem.c1])
        pygame.draw.polygon(screen, color, [elem.a2, elem.b2, elem.c2])
        pygame.draw.polygon(screen, color, [elem.a3, elem.b3, elem.c3])


def check_crash():
    ans = False
    for elem in constants.SPIKE_GROUP:
        if pygame.sprite.collide_mask(constants.PLAYER, elem):
            ans = True
            break
    if constants.PLAYER.pos_y + constants.TILE_HEIGHT > constants.HEIGHT or constants.PLAYER.pos_y < 0:
        ans = True
    return ans


def end_screen(score):
    intro_text = ["ИГРА ОКОНЧЕНА", "",
                  "Ваш счет: " + str(constants.SCORE),
                  "Ваш рекорд: " + score,
                  "Чтобы сыграть еще раз нажмите любую клавишу"]

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
                running = False
        pygame.display.flip()
        constants.CLOCK.tick(constants.FPS)

    pygame.time.delay(1000)


def start_game():
    pygame.init()
    constants.SCORE = 0
    constants.RUNNING = True
    constants.SPIKES_FOR_SCORE = []
    constants.ALL_SPRITES = pygame.sprite.Group()
    constants.SPIKE_GROUP = pygame.sprite.Group()
    constants.BACKGROUND_GROUP = pygame.sprite.Group()
    constants.PLAYER_GROUP = pygame.sprite.Group()
    constants.PLAYER = None


def game():
    while constants.RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    constants.PLAYER.jump()

        constants.SCREEN.fill(constants.COLOR)
        constants.ALL_SPRITES.update()
        constants.BACKGROUND_GROUP.draw(constants.SCREEN)
        constants.PLAYER_GROUP.draw(constants.SCREEN)
        draw_spikes(constants.SCREEN)
        show_score()
        constants.CLOCK.tick(constants.FPS)
        pygame.display.flip()

        if check_crash():
            constants.RUNNING = False


def show_score():
    font = pygame.font.Font(None, 50)
    text = font.render("ТЕКУЩИЙ СЧЕТ: " + str(constants.SCORE), True, (100, 255, 100))
    constants.SCREEN.blit(text, (900, 0))