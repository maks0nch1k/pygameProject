import pygame
from startFunks import start_screen, SIZE, COLOR, RUNNING, SCREEN, CLOCK, FPS

if __name__ == "__main__":
    pygame.init()
    SCREEN.fill(COLOR)
    pygame.display.set_caption("Geometry Trash")
    start_screen()

    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False

        SCREEN.fill(COLOR)
        CLOCK.tick(FPS)
        pygame.display.flip()
    pygame.quit()