import pygame
import random
import classes
import constants
import functions
from functions import start_screen, load_image


if __name__ == "__main__":
    pygame.init()
    constants.SCREEN.fill(constants.COLOR)
    pygame.display.set_caption("Geometry Trash")
    start_screen()

    constants.TILE_IMAGES = {'empty': load_image('empty_tile.png'),
                             'spike': load_image('spike.png'),
                             'background': load_image(f"backgrounds for levels\\background{random.randint(1, 4)}.jpg")}
    constants.PLAYER_IMAGE = load_image('player.png')
    constants.PLAYER = classes.Player(50, 320)

    background1 = classes.Background(0)
    background2 = classes.Background(constants.WIDTH)

    spike1 = classes.Spike(500, 500)
    spike2 = classes.Spike(1000, 700)
    spike3 = classes.Spike(740, 280)

    while constants.RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                constants.RUNNING = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    constants.PLAYER.jump()

        constants.SCREEN.fill(constants.COLOR)
        constants.ALL_SPRITES.update()
        constants.BACKGROUND_GROUP.draw(constants.SCREEN)
        constants.PLAYER_GROUP.draw(constants.SCREEN)
        functions.draw_spikes(constants.SCREEN)
        constants.CLOCK.tick(constants.FPS)
        pygame.display.flip()

        if functions.check_crash():
            constants.RUNNING = None
    if constants.RUNNING is None:
        constants.RUNNING = True

        while constants.RUNNING:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    constants.RUNNING = False

    pygame.quit()