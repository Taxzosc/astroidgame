import random
import pygame
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH )

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        if self.radius > ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            new_angle = random.uniform(20, 50)
            new_direction = self.velocity.rotate(new_angle)#first smaller asteroid direction
            new_negative_direction = self.velocity.rotate(-new_angle)#2nd smaller asteroid direction at the oposite angle
            new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_one = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            asteroid_two = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            asteroid_one.velocity = new_direction * 1.2
            asteroid_two.velocity = new_negative_direction * 1.2
