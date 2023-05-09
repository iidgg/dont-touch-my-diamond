import pygame
import src.constants as C
from src.utils.classes.character import Character

class Player(Character):
    def __init__(self, x, y, speed):
        # Initialize the extended classes
        super().__init__()