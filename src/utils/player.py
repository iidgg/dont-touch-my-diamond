import pygame
from constants import *

class Player:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y

        self.playerSkin = pygame.image.load("src/images/woodcutter/index.png")
        self.playerWalkingSkin = pygame.image.load("src/images/woodcutter/walk.png")

        self.playerWidth = self.playerSkin.get_width()
        self.playerHeight = self.playerSkin.get_height()

        
        self.playerPOS = self.playerOldPOS = pygame.Vector2(WIDTH / 2, HEIGHT / 2) # Create a variable to store the player's position.

        self.walkingFrame = 0

        self.speed = speed