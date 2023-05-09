import pygame

class Object:
    def __init__(self):
        # All available animations
        self.animations = a = ["walking", "running"]
        self.directions = ["right", "left"]

        """"
        Structure:
        "Animation"
        "AnimationSpeed"
        "Speed * Number = the player speed *Speed = The given speed to the class*"
        """  # With spaces between each
        self.AI = [f"{a[0]} 0.1 0.5", f"{a[1]} 0.2 1.0"]
        # ^ Animation information

        self.status = {
            # Player direction
            "oldDirection": "",
            "direction": "right",  # Is player facing left or right?

            # Player skin
            "skin": "Scar_L_Solider",
        }

        self.updateSkins()
        # TODO: Delete the hardcoding here
        self.surface = self.status["walking"]["skin"]["index"]

        # Create a variable to store the player's position.
        self.position = {"x": 0, "y": 0, "old": {"x": 0, "y": 0}}


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
                        "count": skin["animated"].get_width() / skin["index"].get_width(), # TODO
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