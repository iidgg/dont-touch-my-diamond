import pygame
import random
import src.utils.constants as C

# Set default x and y in the middle of game canvas
defaultX = C.canvas["width"] / 2
defaultY = C.canvas["height"] / 2

class defaultObj():
    def __init__(self, skinNameArg, x=defaultX, y=defaultY, objName=""):
        if len(objName) <= 0:
            objName = skinNameArg
        
        self.skinName = skinNameArg

        randY = random.randint(20, C.canvas["height"] - 20)
        randX = random.randint(20, C.canvas["width"] - 20)

        self.pos = pygame.math.Vector2(randX, randY)
        self.posOld = pygame.math.Vector2(randX, randY)

    def setPosition(self, x, y):
        chosenX = x if x != "same" else self.pos.x
        chosenY = y if y != "same" else self.pos.y

        self.setX(chosenX)
        self.setY(chosenY)

    def setY(self, y):
        self.posOld.y = self.pos.y
        self.pos.y = y

    def setX(self, x):
        self.posOld.x = self.pos.x
        self.pos.x = x

    def swapPositions(self):
        self.setPosition("same", "same")

    def changeXby(self, by):
        self.setX(self.pos.x + by)
    
    def changeYby(self, by):
        self.setY(self.pos.y + by)

    def hasMoved(self):
        # Calculate the change in x and y position.
        dx = self.pos.x - self.posOld.x
        dy = self.pos.y - self.posOld.y

        # Check if the player did not move.
        if dx == 0 and dy == 0:
            return False
        return True

    def followMovements(self):
        # Calculate the change in x and y position.
        dx = self.pos.x - self.posOld.x
        dy = self.pos.y - self.posOld.y

        # Check if the player did not move.
        if not self.hasMoved():
            return
      
        # Determine the direction that the player moved to.
        if dx > 0 and dy == 0:
            self.updateDirection("right")
        elif dx < 0 and dy == 0:
            self.updateDirection("left")
        elif dx == 0 and dy > 0:
            self.updateDirection("down")
        elif dx == 0 and dy < 0:
            self.updateDirection("up")
        elif dx > 0 and dy > 0:
            self.updateDirection("down-right")
        elif dx < 0 and dy > 0:
            self.updateDirection("down-left")
        elif dx > 0 and dy < 0:
            self.updateDirection("up-right")
        else:
            self.updateDirection("up-left")

    def updateDirection(self, direction):
        if self.direction == direction:
            return ""
        if direction in self.directions:
            self.oldDirection = self.direction
            self.direction = direction
            self.reloadSkins()


    # def render(self, screen, isLatest=False):
    #     if isLatest:
    #         self.updateAllIntents()
        
    #     screen.blit(self.surface, (self.pos.x, self.pos.y))
    
    # def getSkin():
    #     ""

        