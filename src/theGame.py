import pygame
import src.utils.constants as C
from src.models.character import Character
from src.models.diamonds import Diamonds

class Player(Character):
    def __init__(self, x, y, speed):
        # Initialize the extended classes
        Character.__init__(self, speed)