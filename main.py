import pygame
import constants
from functions import start_screen, load_image, generate_level, load_level


if __name__ == "__main__":
    pygame.init()
    constants.SCREEN.fill(constants.COLOR)
    pygame.display.set_caption("Geometry Trash")
    start_screen()

    constants.TILE_IMAGES = {'empty': load_image('empty_tile.png'), 'spike': load_image('spike.png')}
    constants.LEVEL = load_level("level" + str(constants.DIFFICULTY) + ".txt")
    constants.PLAYER_IMAGE = load_image('player.png')

    while constants.RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                constants.RUNNING = False

        constants.SCREEN.fill(constants.COLOR)
        constants.CLOCK.tick(constants.FPS)
        PLAYER, level_x, level_y = generate_level(constants.LEVEL)
        constants.ALL_SPRITES.update(constants.SCREEN)
        constants.ALL_SPRITES.draw(constants.SCREEN)
        pygame.display.flip()
    pygame.quit()