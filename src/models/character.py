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