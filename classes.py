import pygame
import constants


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(constants.PLAYER_GROUP, constants.ALL_SPRITES)
        self.image = constants.PLAYER_IMAGE
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.bg_now = 0
        self.x = pos_x
        self.pos_y = pos_y
        self.difference = 0
        self.v = 200

    def update(self):
        self.pos_y += self.v / constants.FPS
        self.rect = self.rect.move(0, self.pos_y - self.rect.y)
        if self.v < 0:
            self.difference -= self.pos_y - self.rect.y
        if self.difference > 100:
            self.v = 200

    def jump(self):
        self.v = -self.v
        self.difference = 0


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
