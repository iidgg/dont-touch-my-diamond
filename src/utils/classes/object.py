import pygame
import src.constants as C

class Object():
    def __init__(self, hasSkin=False, isMoveable=False):
        if not isinstance(hasSkin, bool) or not isinstance(isMoveable, bool):
            return "Missing arguments"

        self.isMoveable = True
        self.animations = a = ["walking"]

        """"
        Structure:
        "Animation"
        "AnimationSpeed"
        "Speed * Number = the player speed *Speed = The given speed to the class*"
        """  # With spaces between each
        self.AI = [f"{a[0]} 0.1 0.5"]
        # ^ Animation information
        self.skinName = "arashi"
        self.currentSkin = None
        self.skins = {}
        self.rect = pygame.rect # TODO

        self.directions = ["right", "left", "up", "up-right", "up-left", "down", "down-right", "down-left"]
        self.direction = "right" #? Why right? WHY NOT?
        self.oldDirection = None
        self.updateSkins()

        self.pos = {
            "x": 0,
            "y": 0,
            "xy": (0, 0),
            "ox": 0, # Old x
            "oy": 0, # Old y
            "oxy": (0, 0) # Old x and y
        }

        self.hasSkin = hasSkin
        self.isMoveable = isMoveable

        # TODO: Delete the hardcoding here
        self.surface = self.skins["walking"]["skin"]["index"]

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
    
    def updateDirection(self, direction):
        if self.direction == direction:
            return ""
        if direction in self.directions:
            self.oldDirection = self.direction
            self.direction = direction
            self.updateSkins()
    
    def updateMovements(self):
        keys = pygame.key.get_pressed()
        self.swapPosition()

        walkingWidth = self.skins["walking"]["dimensions"]["width"]
        walkingHeight = self.skins["walking"]["dimensions"]["height"]

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

        ws = 0.5
        # self.status["walking"]["speed"] # Walking speed
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