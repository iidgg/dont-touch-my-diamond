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
        defaultSkin = self.skins[f"{defaultAnimation}"]["skin"]["index"]
        self.lastSkin = defaultSkin
        self.lastSkin = self.getSkin()

    def render(self, screen, isLatest=False):
        if isLatest:
            self.updateAllIntents()
        
        screen.blit(self.getSkin(), self.pos)

    def getSkin(self, updateDirection=True):
        if updateDirection:
            self.followMovements()
        detectAnimation = "walking" # TODO: Make a function that detect the animation
        animationDict = self.skins[f"{detectAnimation}"]
        animationFrames = animationDict["frames"]
        animationSkin = animationDict["skin"]["animated"]
        animationSpeed = animationFrames["speed"]
        totalFrames = animationFrames["total"]["count"]
        currentFrame = animationFrames["current"]
        direction = self.direction
        dimensions = animationDict["dimensions"]
        width, height = dimensions["width"], dimensions["height"]

        # ! The obj keep animating walking, Probably because you're animating without making sure if he even walked...

        if currentFrame >= (totalFrames - animationSpeed):
            # Reset frames to zero if we reached the last frame
            self.skins[f"{detectAnimation}"]["frames"]["current"] = 0
        else:
            # Increase the count to reach closer to the next frame
            self.skins[f"{detectAnimation}"]["frames"]["current"] = round(currentFrame + animationSpeed, 2)
        
        currentFrame = self.skins[f"{detectAnimation}"]["frames"]["current"] # Update the var
        if currentFrame % 1 == 0:
            if not self.hasMoved():
                return self.lastSkin
            if direction == self.directions[0]:
                # if the current direction is right
                self.lastSkin = animationSkin.subsurface(currentFrame * width, 0, width, height)
                return self.lastSkin
            else:
                n = (totalFrames - currentFrame)
                if n == totalFrames:
                    n = 0

                self.lastSkin = animationSkin.subsurface(n * width, 0, width, height)
                return self.lastSkin
        else:
            return self.lastSkin

    def loadSkin(self, animation, isIndex):
        if not animation:
            return 1

        ext = ""
        if isIndex:
            ext = "index/"

        s = self.skins[f"{animation}.skin"] = pygame.image.load(
            f"src/images/{self.skinName}/{animation}/{ext}{self.direction}.png")
        return s
    
    def reloadSkins(self):
        self.loadSkins()
    
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