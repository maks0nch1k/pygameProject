import pygame
import constants
import math


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

    def update(self):
        self.x -= self.v / constants.FPS
        self.rect = self.rect.move(self.x - self.rect.x, 0)
        if self.x <= -constants.WIDTH:
            self.x += 2 * constants.WIDTH
            self.rect = self.rect.move(self.x + (2 * constants.WIDTH), 0)


class Spike(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(constants.ALL_SPRITES, constants.SPIKE_GROUP)
        self.r = 70
        self.rect = pygame.Rect(pos_x - self.r, pos_y - self.r, pos_x + self.r, pos_y + self.r)
        print(self.rect)
        self.a1 = None
        self.b1 = None
        self.c1 = None
        self.a2 = None
        self.b2 = None
        self.c2 = None
        self.a3 = None
        self.b3 = None
        self.c3 = None
        self.x0, self.y0 = pos_x, pos_y
        self.pos = 270
        self.v_rotation = 200
        self.v_move = 100

    def update(self):
        self.a1 = (self.x0 + self.r * math.cos((self.pos + 15) / 180 * math.pi),
                   self.y0 + self.r * math.sin((self.pos + 15) / 180 * math.pi))
        self.b1 = (self.x0 + self.r * math.cos((self.pos - 15) / 180 * math.pi),
                   self.y0 + self.r * math.sin((self.pos - 15) / 180 * math.pi))
        self.c1 = (self.x0, self.y0)

        self.a2 = (self.x0 + self.r * math.cos((self.pos + 15 + 120) / 180 * math.pi),
                   self.y0 + self.r * math.sin((self.pos + 15 + 120) / 180 * math.pi))
        self.b2 = (self.x0 + self.r * math.cos((self.pos - 15 + 120) / 180 * math.pi),
                   self.y0 + self.r * math.sin((self.pos - 15 + 120) / 180 * math.pi))
        self.c2 = (self.x0, self.y0)

        self.a3 = (self.x0 + self.r * math.cos((self.pos + 15 + 240) / 180 * math.pi),
                   self.y0 + self.r * math.sin((self.pos + 15 + 240) / 180 * math.pi))
        self.b3 = (self.x0 + self.r * math.cos((self.pos - 15 + 240) / 180 * math.pi),
                   self.y0 + self.r * math.sin((self.pos - 15 + 240) / 180 * math.pi))
        self.c3 = (self.x0, self.y0)

        self.x0 -= self.v_move / constants.FPS
        self.pos += self.v_rotation / constants.FPS
