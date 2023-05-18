import pygame
import src.utils.constants as C
from src.models.character import Character

class Player(Character):
    def __init__(self, x, y, speed):
        # Initialize the extended classes
        Character.__init__(self)

    def updatePlayer(self):
        self.updateAllIntents()
        touchingDiamonds = True

        if touchingDiamonds: 
            ""

        print(self.pos["x"], self.pos["y"])
        print(self.skins["walking"]["dimensions"])

    def isPlayerTouchingDiamonds(self):
        ""
