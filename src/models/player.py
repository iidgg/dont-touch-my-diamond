import pygame
import src.utils.constants as C
from src.models.character import Character

class Player(Character):
    def __init__(self, x, y, speed):
        # Initialize the extended classes
        Character.__init__(self, speed)

    def isTouchingRect(self, rect):
        width = self.skins["walking"]["dimensions"]["width"]
        height = self.skins["walking"]["dimensions"]["height"] # TODO: remove hardcoding

        width = width - 12
        height = height - 12 # TODO remove hardcoding...
        #? these 12 pixels are invisible area's (:
        # Create a new rect object with the given vec, width and height
        tempRect = pygame.Rect(self.pos.x, self.pos.y, width, height)
        
        # Check if the new_rect is colliding with the given rect
        if rect.colliderect(tempRect):
            return True
        else:
            return False