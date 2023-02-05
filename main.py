import pygame
import random
import classes
import constants
from functions import start_screen, load_image, generate_level, load_level


if __name__ == "__main__":
    pygame.init()
    constants.SCREEN.fill(constants.COLOR)
    pygame.display.set_caption("Geometry Trash")
    start_screen()

    constants.TILE_IMAGES = {'empty': load_image('empty_tile.png'),
                             'spike': load_image('spike.png'),
                             'background': load_image(f"backgrounds for levels\\background{random.randint(1, 4)}.jpg")}
    # constants.LEVEL = load_level("level" + str(constants.DIFFICULTY) + ".txt")
    constants.PLAYER_IMAGE = load_image('player.png')
    constants.PLAYER = classes.Player(50, 320)
    # constants.CAMERA = Camera()

    background1 = classes.Background(0)
    background2 = classes.Background(constants.WIDTH)

    while constants.RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                constants.RUNNING = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    pass

        # constants.LEVEL[-1] = constants.LEVEL[-1][:constants.LEVEL[-1].find("@")] + ".@" + constants.LEVEL[-1][constants.LEVEL[-1].find("@") + 2:]

        constants.SCREEN.fill(constants.COLOR)
        constants.ALL_SPRITES.update()
        constants.BACKGROUND_GROUP.draw(constants.SCREEN)
        constants.PLAYER_GROUP.draw(background1.image)
        constants.CLOCK.tick(constants.FPS)
        pygame.display.flip()
    pygame.quit()