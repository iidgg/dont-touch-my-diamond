import pygame
import src.utils.constants as C

# Set default x and y in the middle of game canvas
defaultX = C.canvas["width"] / 2
defaultY = C.canvas["height"] / 2

class defaultObj():
    def __init__(self, skinNameArg, x=defaultX, y=defaultY, objName=""):
        if len(objName) <= 0:
            objName = skinNameArg
        
        self.skinName = skinNameArg

        self.pos = pygame.math.Vector2(x, y)
        self.posOld = pygame.math.Vector2(x, y)

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

    # def render(self, screen, isLatest=False):
    #     if isLatest:
    #         self.updateAllIntents()
        
    #     screen.blit(self.surface, (self.pos.x, self.pos.y))
    
    # def getSkin():
    #     ""

        