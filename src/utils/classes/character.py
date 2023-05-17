import pygame
import src.constants as C
from src.utils.classes.object import Object

class Character(Object):
    def __init__(self):
        Object.__init__(self, True, True)
        # All available animations
        self.animations = a = ["walking"]

        """"
        Structure:
        "Animation"
        "AnimationSpeed"
        "Speed * Number = the player speed *Speed = The given speed to the class*"
        """  # With spaces between each
        self.AI = [f"{a[0]} 0.1 0.5"]
        # ^ Animation information

        self.status = {
            # Player direction
            "oldDirection": "",
            "direction": "right",  # Is player facing left or right?

            # Player skin
            "skin": "arashi",
        }

        self.updateSkins()
        # TODO: Delete the hardcoding here
        self.surface = self.status["walking"]["skin"]["index"]

        # Create a variable to store the player's position.
        # self.position = {"x": 0, "y": 0, "old": {"x": 0, "y": 0}}

    def getSkin(self, animation, isIndex):
        if not animation:
            return 1

        ext = ""
        if isIndex:
            ext = "index/"

        s = self.status[f"{animation}.skin"] = pygame.image.load(
            f"src/images/{self.status['skin']}/{animation}/{ext}{self.direction}.png")
        return s

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

            self.status[name] = {
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

    def animate(self, animation):
        if not animation in self.animations:
            return "Invalid animation"
        
        animationDict = self.status[f"{animation}"]
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
            self.status[f"{animation}"]["frames"]["current"] = 0
        else:
            # Increase the count to reach closer to the next frame
            self.status[f"{animation}"]["frames"]["current"] = round(currentFrame + animationSpeed, 2)
        
        currentFrame = self.status[f"{animation}"]["frames"]["current"] # Update the var
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
        walkingSpeed = self.status["walking"]["speed"]

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

    def followMovements(self):
        # Calculate the change in x and y position.
        dx = self.pos["x"] - self.pos["ox"]
        dy = self.pos["y"] - self.pos["oy"]

        # Check if the player did not move.
        if dx == 0 and dy == 0:
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


    def render(self, screen, isLatest):
        if isLatest:
            self.updateAllIntents()
        
        screen.blit(self.surface, (self.pos["x"], self.pos["y"]))