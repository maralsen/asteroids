import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS

class Shot(CircleShape):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        color = "white"
        center = self.position
        radius = self.radius
        pygame.draw.circle(screen, color, center, radius, LINE_WIDTH)

    def update(self, dt: float):
        self.position += self.velocity * dt
