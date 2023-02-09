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
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.bg_now = 0
        self.x = pos_x
        self.pos_y = pos_y
        self.transparent = (0, 0, 0, 0)
        self.v = 100

    def update(self):
        self.image = pygame.transform.rotate(self.image, 10)
        self.rect = self.image.get_rect().move(self.x, self.pos_y)


class Background(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__(constants.BACKGROUND_GROUP, constants.ALL_SPRITES)
        self.image = constants.TILE_IMAGES["background"]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.x = x
        self.v = 100
        print(self.rect)

    def update(self):
        self.x -= self.v / constants.FPS
        self.rect = self.rect.move(self.x - self.rect.x, 0)
        if self.x <= -constants.WIDTH:
            self.x += 2 * constants.WIDTH
            self.rect = self.rect.move(self.x + (2 * constants.WIDTH), 0)
