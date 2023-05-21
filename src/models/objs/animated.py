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
