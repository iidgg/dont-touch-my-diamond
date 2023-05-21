import pygame
import src.utils.constants as C

class Object():
    def __init__(self):
        self.currentSkin = None # ! Not needed atm
        self.rect = pygame.rect # TODO

        self.oldDirection = None
        self.updateSkins()

    def updateMovements(self):
        keys = pygame.key.get_pressed()
        self.swapPosition()

        walkingWidth = self.skins["walking"]["dimensions"]["width"]
        walkingHeight = self.skins["walking"]["dimensions"]["height"]

        # Check if the player is about to go off screen.
        if self.pos["x"] < 0:
            self.setX(0)
        elif self.pos["x"] >= C.canvas["width"] - walkingWidth:
            self.setX(C.canvas["width"] - walkingWidth)
            
        if self.pos["y"] < 0:
            self.setY(0)
        elif self.pos["y"] >= C.canvas["height"] - walkingHeight:
            self.setY(C.canvas["height"] - walkingHeight)

        ws = 0.5
        # self.status["walking"]["speed"] # Walking speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.changeYby(-ws)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.changeYby(ws)
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.changeXby(-ws)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.changeXby(ws)

        self.followMovements()