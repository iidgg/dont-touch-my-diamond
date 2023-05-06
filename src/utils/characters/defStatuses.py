import pygame

class CharacterStatuses:
    def __init__(self):
        # All available animations
        self.animations = a = ["walking", "running"]

        """"
        Structure:
        "Animation"
        "AnimationSpeed"
        "Speed * Number = the player speed *Speed = The given speed to the class*"
        """ # With spaces between each
        self.AI = [f"{a[0]} 0.1 1", f"{a[1]} 0.2 2", "flying 0.5 5"] # Animation information

        self.status = {
            # Player direction
            "direction": "right",  # Is player facing left or right?
            "allDirections": ["right", "left"],

            # Player skin
            "skin": "Scar_L_Solider",

            
        }

        for e in self.AI: # e Stands for element
            eSplitted = e.split()

            self.status[eSplitted[0]] = {
                "speed": float(eSplitted[1]), # animation speed "how fast do we switch frames"
                "skin": None, # None is Null
                "frames": {
                    "total": int(eSplitted[2]),
                    "current": 0
                }
            }

    def getSkin(self, animation, isIndex):
        if not animation:
            return 1
        
        ext = ""
        if isIndex:
            ext = "index/"
        
        
        s = self.status[f"{animation}.skin"] = pygame.image.load(
            f"src/images/{self.status['skin']}/{animation}/{ext}{self.status['direction']}.png")
        return s
