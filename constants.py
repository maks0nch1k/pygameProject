import pygame

pygame.init()
SIZE = WIDTH, HEIGHT = 1280, 720
RUNNING = True
COLOR = "black"
SCREEN = pygame.display.set_mode(SIZE)
CLOCK = pygame.time.Clock()
FPS = 240
SCORE = 0
SPIKES_FOR_SCORE = []
TILE_WIDTH = TILE_HEIGHT = 80
ALL_SPRITES = pygame.sprite.Group()
SPIKE_GROUP = pygame.sprite.Group()
BACKGROUND_GROUP = pygame.sprite.Group()
PLAYER_GROUP = pygame.sprite.Group()
PLAYER = None
TILE_IMAGES = None
PLAYER_IMAGE = None
