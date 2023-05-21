import pygame
import src.utils.constants as C
from src.models.objs.animated import animatedObject

none = "Unassigned"
class Character(animatedObject):
    def __init__(self, movementSpeedArg):
        animatedObject.__init__(self)

        self.movementSpeed = movementSpeedArg

    def goUP(self):
        self.changeYby(self.movementSpeed)

    def goDOWN(self):
        self.changeYby(-self.movementSpeed)

    def goRIGHT(self):
        self.changeXby(self.movementSpeed)

    def goLEFT(self):
        self.changeXby(-self.movementSpeed)

    def movingHandler(self):
        keys = pygame.key.get_pressed()
        self.swapPositions()

        ws = self.movementSpeed # ws = Walking speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.changeYby(-ws)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.changeYby(ws)
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.changeXby(-ws)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.changeXby(ws)