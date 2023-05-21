import pygame
import src.utils.constants as C
from src.models.character import Character
from src.models.diamonds import Diamonds

class Player(Character):
    def __init__(self, x, y, speed):
        # Initialize the extended classes
        Character.__init__(self)

        self.diamonds = diamonds = Diamonds()
        allDiamonds = diamonds.allDiamonds

    def renderPlayer(self, canvas):
        self.updatePlayer(canvas)
        self.render(canvas)
        
    def updatePlayer(self, canvas):
        self.updateAllIntents()
        touchingDiamonds = True

        if touchingDiamonds: 
            ""

        self.blitDiamonds(canvas)

    def blitDiamonds(self, canvas):
        if len(self.diamonds.allDiamonds) < 5:
            self.diamonds.generateDiamonds(canvas, 5)

        self.diamonds.blitAll(canvas)

    def isPlayerTouchingDiamonds(self, canvas):
        ""
        self.blitDiamonds(canvas)
