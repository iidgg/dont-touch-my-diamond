import pygame
from src.utils.classes.SkinAndMovements import SM

class Object(SM):
    def __init__(self, hasSkin=False, isMoveable=False):
        if not isinstance(hasSkin, bool) or not isinstance(isMoveable, bool):
            return "Missing arguments"

        self.initializeSM()
        self.hasSkin = hasSkin
        self.isMoveable = isMoveable

        # TODO: Delete the hardcoding here
        self.surface = self.skins["walking"]["skin"]["index"]

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

    def render(self, screen, isLatest):
        if isLatest:
            self.updateAllIntents()
        
        screen.blit(self.surface, (self.pos["x"], self.pos["y"]))

    def updateAllIntents(self):
        self.updateMovements()

        newX, oldX = self.pos["x"], self.pos["ox"]
        newY, oldY = self.pos["y"], self.pos["oy"]
        isOldXisNewX =  newX == oldX
        isOldYisNewY = newY == oldY
        walkingSpeed = 0.5
        # self.status["walking"]["speed"]

        # TODO: this WAS to give us the ability to jump and else, are you still thinking about it?
        if not isOldXisNewX and isOldYisNewY: 
            if abs(newX - oldX) == abs(walkingSpeed):
                self.animate("walking")
        elif not isOldYisNewY and isOldXisNewX:
            if abs(newY - oldY) == abs(walkingSpeed):
                self.animate("walking")
        elif not isOldYisNewY and not isOldXisNewX:
            if abs(newY - oldY) == abs(walkingSpeed):
                self.animate("walking")
        

        return self.surface
    
    def animate(self, animation):
        if not animation in self.animations:
            return "Invalid animation"
        
        animationDict = self.skins[f"{animation}"]
        animationFrames = animationDict["frames"]
        animationSkin = animationDict["skin"]["animated"]
        animationSpeed = animationFrames["speed"]
        totalFrames = animationFrames["total"]["count"]
        currentFrame = animationFrames["current"]
        direction = self.direction
        dimensions = animationDict["dimensions"]
        width, height = dimensions["width"], dimensions["height"]

        if currentFrame >= (totalFrames - animationSpeed):
            # Reset frames to zero if we reached the last frame
            self.skins[f"{animation}"]["frames"]["current"] = 0
        else:
            # Increase the count to reach closer to the next frame
            self.skins[f"{animation}"]["frames"]["current"] = round(currentFrame + animationSpeed, 2)
        
        currentFrame = self.skins[f"{animation}"]["frames"]["current"] # Update the var
        if currentFrame % 1 == 0:
            if direction == self.directions[0]:
                # if the current direction is right
                self.surface = animationSkin.subsurface(currentFrame * width, 0, width, height)
            else:
                n = (totalFrames - currentFrame)
                if n == totalFrames:
                    n = 0
                
                self.surface = animationSkin.subsurface(n * width, 0, width, height)