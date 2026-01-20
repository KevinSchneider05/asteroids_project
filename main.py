import pygame
from constants import *
from logger import log_state
from player import Player


def main():
    pygame.init()
    fps_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while 1:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        dt = fps_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
