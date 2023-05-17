import pygame
from src.utils.classes.SkinAndMovements import SM

class Object(SM):
    def __init__(self, hasSkin=False, isMoveable=False):
        if not isinstance(hasSkin, bool) or not isinstance(isMoveable, bool):
            return "Nah broda"

        self.initializeSM()
        self.hasSkin = hasSkin
        self.isMoveable = isMoveable

        self.currentSkin = None
        self.skinName = "arashi"
        self.skins = {}
        self.rect = pygame.rect # TODO

    def initializeSM(self):
        SM.__init__(self)

    def getSkin(self, animation, isIndex):
        if not animation:
            return 1

        ext = ""
        if isIndex:
            ext = "index/"

        s = self.skins[f"{animation}.skin"] = pygame.image.load(
            f"src/images/{self.skinName}/{animation}/{ext}{self.direction}.png")
        return s

    # def getSkin(self, animation, isIndex):
    #     if not animation:
    #         return 1

    #     ext = ""
    #     if isIndex:
    #         ext = "index/"

    #     s = self.skin[f"{animation}.skin"] = pygame.image.load(
    #         f"src/images/{self.skin['skin']}/{animation}/{ext}{self.skin['direction']}.png")
    #     return s
    
    def setPosition(self, x, y):
        chosenX = x if x != "same" else self.pos["x"]
        chosenY = y if y != "same" else self.pos["y"]

        self.setX(chosenX)
        self.setY(chosenY)

    def setY(self, y):
        self.pos["oy"] = self.pos["y"]
        self.pos["y"] = y

    def setX(self, x):
        self.pos["ox"] = self.pos["x"]
        self.pos["x"] = x

    def swapPosition(self):
        self.setPosition("same", "same")

    def changeXby(self, by):
        self.setX(self.pos["x"] + by)
    
    def changeYby(self, by):
        self.setY(self.pos["y"] + by)
