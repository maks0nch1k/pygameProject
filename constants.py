import pygame

pygame.init()
SIZE = WIDTH, HEIGHT = 1280, 720
RUNNING = True
COLOR = "black"
SCREEN = pygame.display.set_mode(SIZE)
CLOCK = pygame.time.Clock()
FPS = 240
DIFFICULTY = 0
TILE_WIDTH = TILE_HEIGHT = 45
ALL_SPRITES = pygame.sprite.Group()
TILES_GROUP = pygame.sprite.Group()
PLAYER_GROUP = pygame.sprite.Group()