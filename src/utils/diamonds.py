import pygame
import random
from src.utils.classes.object import Object

class Diamonds(Object):
    def __init__(self):
        Object.__init__(self)

        self.skin = pygame.transform.scale(pygame.image.load("src/images/objects/rewards/diamond.png"), (11.54, 12.5))

        self.allDiamonds = []

    def spawnRandom(self, screen, count):
        for i in range(count):
            x = random.randint(0, screen.get_width())
            y = random.randint(0, screen.get_height())
            diamond = pygame.Rect(x, y, self.skin.get_width(), self.skin.get_height())

            screen.blit(self.skin, diamond)
            self.allDiamonds.append(diamond)
