from circleshape import CircleShape
import constants
import pygame
import random
from logger import log_state,log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen,"White",self.position,self.radius,constants.LINE_WIDTH)
    def update(self,dt):
        self.position+=(self.velocity*dt)
    def split(self):
        self.kill()
        if self.radius < constants.ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_angle = random.uniform(20,50)
            new_velo1 = self.velocity.rotate(new_angle)
            new_velo2 = self.velocity.rotate(-1*new_angle)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = new_velo1*1.2
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = new_velo2*1.2
