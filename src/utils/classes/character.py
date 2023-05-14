import pygame
import src.constants as C
from src.utils.classes.object import Object

class Character(Object):
    def __init__(self):
        Object.__init__(self)
        # All available animations
        self.animations = a = ["walking"]
        self.directions = ["right", "left", "up", "down"]

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
            "skin": "whitish",
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
            f"src/images/{self.status['skin']}/{animation}/{ext}{self.status['direction']}.png")
        return s

    def updateDirection(self, direction):
        if self.status["oldDirection"] == direction:
            return ""
        if direction in self.directions:
            self.status["oldDirection"] = self.status["direction"]
            self.status["direction"] = direction
            self.updateSkins()

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
        direction = self.status["direction"]
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
    
    def updateMovements(self):
        keys = pygame.key.get_pressed()
        # self.pos["ox"], self.pos["oy"] = self.pos["x"], self.pos["y"]
        self.swapPosition()

        walkingWidth = self.status["walking"]["dimensions"]["width"]
        walkingHeight = self.status["walking"]["dimensions"]["height"]

        # TODO: Bruh bro! the player CAN go off down screen
        # Check if the player is about to go off screen.
        if self.pos["x"] < 0:
            self.setX(0)
        elif self.pos["x"] >= C.screen["width"] - walkingWidth:
            self.setX(C.screen["width"] - walkingWidth)
            
        if self.pos["y"] < 0:
            self.setY(0)
        elif self.pos["y"] >= C.screen["width"] - walkingHeight:
            self.setY(C.screen["width"] - walkingHeight)
        # TODO: Ends the last todo, the code down there doesn't have anything to do with this bug

        ws = self.status["walking"]["speed"] # Walking speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.changeYby(-ws)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.changeYby(ws)
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.changeXby(-ws)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.changeXby(ws)

        self.followMovements()

    def followMovements(self):
        if not (self.pos["ox"] == self.pos["x"] and self.pos["oy"] == self.pos["y"]):
            if not self.pos["oy"] == self.pos["y"]:
                "Moved up or down"
                if self.pos["y"] - 0.5 == self.pos["oy"]:
                    "Moved down"
                    self.updateDirection("down")
                elif self.pos["y"] + 0.5 == self.pos["oy"]:
                    "Moved up"
                    self.updateDirection("up")
            else:
                if self.pos["x"] - 0.5 == self.pos["ox"]:
                    "Moved right" # TODO: Change the hardcoded 0.5 Up and down
                    self.updateDirection("right")
                elif self.pos["x"] + 0.5 == self.pos["ox"]:
                    "Moved left"
                    self.updateDirection("left")

    def render(self, screen, isLatest):
        if isLatest:
            self.updateAllIntents()
        
        screen.blit(self.surface, (self.pos["x"], self.pos["y"]))