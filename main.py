import pygame
from player import Player
from constants import *
from logger import log_state

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Player1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            Player1.update (dt)
            screen.fill("black")
            Player1.draw(screen)
            pygame.display.flip()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
