import pygame
import constants
from functions import start_screen, load_image, generate_level, load_level
from classes import Camera


if __name__ == "__main__":
    pygame.init()
    constants.SCREEN.fill(constants.COLOR)
    pygame.display.set_caption("Geometry Trash")
    start_screen()

    constants.TILE_IMAGES = {'empty': load_image('empty_tile.png'),
                             'spike': load_image('spike.png'),
                             'background': load_image("backgrounds for levels\\background1.jpg")}
    constants.LEVEL = load_level("level" + str(constants.DIFFICULTY) + ".txt")
    constants.PLAYER_IMAGE = load_image('player.png')
    constants.CAMERA = Camera()

    while constants.RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                constants.RUNNING = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    pass

        constants.LEVEL[-1] = constants.LEVEL[-1][:constants.LEVEL[-1].find("@")] + ".@" + constants.LEVEL[-1][constants.LEVEL[-1].find("@") + 2:]

        constants.SCREEN.fill(constants.COLOR)
        constants.CLOCK.tick(constants.FPS)
        constants.PLAYER, level_x, level_y = generate_level(constants.LEVEL)
        constants.CAMERA.update(constants.PLAYER)
        for sprite in constants.ALL_SPRITES:
            constants.CAMERA.apply(sprite)
        constants.ALL_SPRITES.update(constants.SCREEN)
        constants.ALL_SPRITES.draw(constants.SCREEN)
        pygame.display.flip()
    pygame.quit()