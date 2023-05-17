import pygame
from src.utils.classes.SkinAndMovements import SM

class Object(SM):
    def __init__(self, hasSkin=False, isMoveable=False):
        if not isinstance(hasSkin, bool) or not isinstance(isMoveable, bool):
            return "Nah broda"

        self.initializeSM()
        self.hasSkin = hasSkin
        self.isMoveable = isMoveable

        self.skin = None
        self.rect = pygame.rect # TODO

    def initializeSM(self):
        SM.__init__(self)

    def updateSkins(self):
        for e in self.AI:  # e Stands for element
            eSplitted = e.split()
            name = eSplitted[0]

            if not name in self.animations:
                print("Failed to load animation Named: ", name)
                return

            skin = {
                "animated": self.getSkin(name, False),
                "index": self.getSkin(name, True)
            }

            self.skin[name] = {
                # animation speed "how fast do we switch frames"
                "speed": float(eSplitted[2]),
                "skin": {
                    "animated": skin["animated"],
                    "index": skin["index"]
                },
                "frames": {
                    "total": {
                        "count": skin["animated"].get_width() / skin["index"].get_width(), # ? This was a todo, i guess its done?
                        "width": skin["animated"].get_width()
                    },
                    "width": 0,
                    "current": 0,
                    "speed": float(eSplitted[1])
                },
                "dimensions": {
                    "width": skin["index"].get_width(),
                    "height": skin["index"].get_height()
                }
            }

    def getSkin(self, animation, isIndex):
        if not animation:
            return 1

        ext = ""
        if isIndex:
            ext = "index/"

        s = self.skin[f"{animation}.skin"] = pygame.image.load(
            f"src/images/{self.skin['skin']}/{animation}/{ext}{self.skin['direction']}.png")
        return s
    
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
