import pygame
import random
from src.models.objs.inanimate import inanimateObject

class Diamonds(inanimateObject):
    def __init__(self):
        inanimateObject.__init__(self)

        self.skin = pygame.transform.scale(pygame.image.load("src/images/objects/rewards/diamond.png"), (11.54, 12.5))

        self.allDiamonds = []

    def generateDiamonds(self, screen, count):
        for i in range(count):
            x = random.randint(0, screen.get_width())
            y = random.randint(0, screen.get_height())
            diamond = pygame.Rect(x, y, self.skin.get_width(), self.skin.get_height())

            self.allDiamonds.append(diamond)
    
    def blitAll(self, screen):
        for i in range(len(self.allDiamonds)):
            self.blitOne(screen, i)

    def blitOne(self, screen, index):
        screen.blit(self.skin, self.allDiamonds[index])
