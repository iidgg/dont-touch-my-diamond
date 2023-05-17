import pygame
from src.utils.classes.movements import Movements

class Skin(Movements):
    def __init__(self, isAnimated):
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

        self.hasSkin = True
        self.skin = "" # Pygame load something
        self.skinName = "arashi" # TODO: Remove hardcode
        
        self.updateSkins()