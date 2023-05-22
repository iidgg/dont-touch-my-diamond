import pygame
from src.models.character import Character

class Ghost(Character):
    def __init__(self):
        Character.__init__(self, 0.5)

    def follow(self, target):
        direction = target - self.pos
        distance = direction.length()

        if distance > 0:
            direction.normalize_ip()
            self.pos += direction * min(distance, self.movementSpeed)
