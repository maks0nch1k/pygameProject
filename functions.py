import os
import pygame
import sys
import constants


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


def draw_spikes(screen):
    color = "black"
    for elem in constants.SPIKE_GROUP:
        pygame.draw.circle(screen, color, (elem.x0, elem.y0), 10)
        pygame.draw.polygon(screen, color, [elem.a1, elem.b1, elem.c1])
        pygame.draw.polygon(screen, color, [elem.a2, elem.b2, elem.c2])
        pygame.draw.polygon(screen, color, [elem.a3, elem.b3, elem.c3])