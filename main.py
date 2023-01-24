import pygame
from constants import COLOR, RUNNING, SCREEN, CLOCK, FPS
from functions import start_screen, load_image


if __name__ == "__main__":
    pygame.init()
    SCREEN.fill(COLOR)
    pygame.display.set_caption("Geometry Trash")
    start_screen()

    # TILE_IMAGES = {'wall': load_image('box.png'), 'empty': load_image('grass.png')}
    # PLAYER_IMAGE = load_image('mario.png')

    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False

        SCREEN.fill(COLOR)
        CLOCK.tick(FPS)
        pygame.display.flip()
    pygame.quit()