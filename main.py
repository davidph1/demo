import pygame
from asteroidfield import AsteroidField
from player import Player
from asteroid import Asteroid
from shot import Shot
from constants import *
from logger import log_state,log_event
import sys

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    afteroidfield1 = AsteroidField()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots,updatable,drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Player1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update (dt)
        for rocks in asteroids:
            for bullet in shots:
                if rocks.collides_with(bullet):
                    log_event("asteroid_shot")
                    rocks.split()
                    bullet.kill()
            if Player1.collides_with(rocks):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        screen.fill("black")
        for bits in drawable:
            bits.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
