import pygame
import src.utils.constants as C
from src.models.object import Object

class Character(Object):
    def __init__(self):
        Object.__init__(self, True, True)

        self.updateSkins()

        # Create a variable to store the player's position.
        # self.position = {"x": 0, "y": 0, "old": {"x": 0, "y": 0}}