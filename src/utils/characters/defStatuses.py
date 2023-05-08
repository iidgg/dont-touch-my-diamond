import pygame

# TODO: figure out where to keep the actual animation function, new class?


class CharacterStatuses:
    def __init__(self):
        # All available animations
        self.animations = a = ["walking", "running"]

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
            "direction": "right",  # Is player facing left or right?
            "allDirections": ["right", "left"],

            # Player skin
            "skin": "Scar_L_Solider",


        }

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
                        "count": float(eSplitted[2]),
                        "width": skin["animated"].get_width()
                    },
                    "width": 0,
                    "current": 0
                },
                "dimensions": {"width": skin["index"].get_width(), "height": skin["index"].get_height()}
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

    def updateDirection(self, direction):
        if direction in self.status["allDirections"]:
            self.status["direction"] = direction

            # TODO: do this update skin please bro
            # self.updatePlayerSkin()
