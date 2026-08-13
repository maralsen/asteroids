import pygame
import circleshape
from constants import LINE_WIDTH

class Asteroid(circleshape.CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        color = "white"
        center = self.position
        radius = self.radius
        pygame.draw.circle(screen, color, center, radius, LINE_WIDTH)

    def update(self, dt: float):
        self.position += self.velocity * dt
