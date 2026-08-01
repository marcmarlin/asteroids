from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white",self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            theta = random.uniform(20, 50)
            vel_1 = self.velocity.rotate(theta)
            vel_2 = self.velocity.rotate(-theta)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
            new_asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)
            new_asteroid_1.velocity = vel_1 * 1.2
            new_asteroid_2.velocity = vel_2 * 1.2