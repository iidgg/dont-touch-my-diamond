import pygame
from src.models.objs.default import defaultObj

class animatedObject(defaultObj):
    def __init__(self):
        defaultObj.__init__(self, "arashi") #TODO: NO HARDCODING!
        defaultDirection = "right"
        defaultAnimation = "walking"

        self.directions = ["right", "left", "up", "up-right", "up-left", "down", "down-right", "down-left"]
        self.direction = defaultDirection #? Why right? WHY NOT?

        self.animations = a = ["walking"]

        """"
        Structure:
        "Animation"
        "AnimationSpeed"
        "Speed * Number = the player speed *Speed = The given speed to the class*"
        """  # With spaces between each
        self.AI = [f"{a[0]} 0.1 0.5"]
        # ^ Animation information

        self.skins = {}

        self.loadSkins()

    def render(self, screen, isLatest=False):
        if isLatest:
            self.updateAllIntents()
        
        screen.blit(self.getSkin(), self.pos)

    def getSkin(self):
        return self.skins["walking"]["skin"]["index"]

    def loadSkin(self, animation, isIndex):
        if not animation:
            return 1

        ext = ""
        if isIndex:
            ext = "index/"

        s = self.skins[f"{animation}.skin"] = pygame.image.load(
            f"src/images/{self.skinName}/{animation}/{ext}{self.direction}.png")
        return s
    
    def loadSkins(self):
        for e in self.AI:  # e Stands for element
            eSplitted = e.split()
            name = eSplitted[0]

            if not name in self.animations:
                print("Failed to load animation Named: ", name)
                return

            skin = {
                "animated": self.loadSkin(name, False),
                "index": self.loadSkin(name, True)
            }

            self.skins[name] = {
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