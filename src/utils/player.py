import pygame
from constants import *

class Player:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y

        self.playerDirection = "right"
        self.playerSpeed = speed

        self.playerSkin = pygame.image.load(f"src/images/woodcutter/index/{self.playerDirection}.png")
        self.playerWalkingSkin = pygame.image.load(f"src/images/woodcutter/walk/{self.playerDirection}.png")

        self.playerWidth = self.playerSkin.get_width()
        self.playerHeight = self.playerSkin.get_height()

        self.playerSurface = self.playerSkin

        self.playerPOS = self.playerOldPOS = pygame.Vector2(WIDTH / 2, HEIGHT / 2) # Create a variable to store the player's position.

        self.walkingFrame = 0
        self.animationSpeed = 0.1

    def movePlayer(self):
        keys = pygame.key.get_pressed()
    
        # Check if the player is about to go off screen.
        if self.playerPOS.x < 0:
            self.playerPOS.x = 0
        elif self.playerPOS.x >= WIDTH - self.playerWidth:
            self.playerPOS.x = WIDTH - self.playerWidth
        
        if self.playerPOS.y < 0:
            self.playerPOS.y = 0
        elif self.playerPOS.y >= HEIGHT - self.playerHeight:
            self.playerPOS.y = HEIGHT - self.playerHeight
    
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.playerPOS.y -= self.playerSpeed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.playerPOS.y += self.playerSpeed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.playerPOS.x -= self.playerSpeed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.playerPOS.x += self.playerSpeed
        self.oldPlayerPOS = self.playerPOS

    def updateAllPlayerIntents(self):
        self.movePlayer()

        if self.walkingFrame % 1 == 0:
            self.playerSurface = self.playerWalkingSkin.subsurface((self.walkingFrame * 48, 0, 48, 48))

        if self.walkingFrame >= (6 - self.animationSpeed):
            self.walkingFrame = 0
        else:
            self.walkingFrame = round(self.walkingFrame + self.animationSpeed, 2)

        return self.playerSurface