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

        walkingWidth = self.skins["walking"]["dimensions"]["width"]
        walkingHeight = self.skins["walking"]["dimensions"]["height"]

        # Check if the character is about to go off screen.
        if self.pos.x < 0:
            self.setX(0)
        elif self.pos.x >= C.canvas["width"] - walkingWidth:
            self.setX(C.canvas["width"] - walkingWidth)
            
        if self.pos.y < 0:
            self.setY(0)
        elif self.pos.y >= C.canvas["height"] - walkingHeight:
            self.setY(C.canvas["height"] - walkingHeight)

        ws = self.movementSpeed # ws = Walking speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.changeYby(-ws)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.changeYby(ws)
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.changeXby(-ws)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.changeXby(ws)