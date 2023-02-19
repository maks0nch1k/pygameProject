import pygame
import random
import classes
import constants
import functions


if __name__ == "__main__":
    pygame.init()
    constants.SCREEN.fill(constants.COLOR)
    pygame.display.set_caption("Geometry Trash")
    functions.start_screen()

    constants.TILE_IMAGES = {'empty': functions.load_image('empty_tile.png'),
                             'spike': functions.load_image('spike.png'),
                             'background': functions.load_image(f"backgrounds for levels\\background{random.randint(1, 4)}.jpg")}
    constants.PLAYER_IMAGE = functions.load_image('player.png')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                functions.terminate()

        functions.start_game()

        constants.PLAYER = classes.Player(50, 320)

        background1 = classes.Background(0)
        background2 = classes.Background(constants.WIDTH)

        spike1 = classes.Spike(500, 500)
        spike2 = classes.Spike(1000, 700)
        spike3 = classes.Spike(740, 280)

        functions.game()

        functions.end_screen()