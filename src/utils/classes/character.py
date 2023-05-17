import pygame
import src.constants as C
from src.utils.classes.object import Object

class Character(Object):
    def __init__(self):
        Object.__init__(self, True, True)
        # All available animations



        self.status = {
            # Player direction
            "oldDirection": "",
            "direction": "right",  # Is player facing left or right?

            # Player skin
            "skin": "arashi",
        }

        self.updateSkins()
        # TODO: Delete the hardcoding here
        self.surface = self.skins["walking"]["skin"]["index"]

        # Create a variable to store the player's position.
        # self.position = {"x": 0, "y": 0, "old": {"x": 0, "y": 0}}

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
    
    def render(self, screen, isLatest):
        if isLatest:
            self.updateAllIntents()
        
        screen.blit(self.surface, (self.pos["x"], self.pos["y"]))