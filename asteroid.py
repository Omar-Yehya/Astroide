from circleshape import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)  
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity = pygame.Vector2(0, 0)  
        self.color = (255, 255, 255)  

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius, 2)

    def update(self, dt):
        self.x += self.velocity.x * dt
        self.y += self.velocity.y * dt






