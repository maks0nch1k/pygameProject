import pygame
import constants


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x - target.rect.w // 2 - constants.WIDTH // 2)
        self.dy = 0


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(constants.TILES_GROUP, constants.ALL_SPRITES)
        self.image = constants.TILE_IMAGES[tile_type]
        self.rect = self.image.get_rect().move(
            constants.TILE_WIDTH * pos_x, constants.TILE_HEIGHT * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(constants.PLAYER_GROUP, constants.ALL_SPRITES)
        self.image = constants.PLAYER_IMAGE
        self.rect = self.image.get_rect().move(
            constants.TILE_WIDTH * pos_x, constants.TILE_HEIGHT * pos_y)


"""class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(constants.ALL_SPRITES)
        self.image = constants.TILE_IMAGES["background"]
        self.rect = self.image.get_rect()
        self.rect.x = -600
        self.x = -600
        self.v = 20

    def update(self):
        if self.x < 0:
            self.x += self.v / constants.FPS
            self.rect = self.rect.move(self.x - self.rect.x, 0)"""