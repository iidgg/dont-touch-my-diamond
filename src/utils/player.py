import pygame
from constants import *


class Player:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y

        self.playerSpeed = speed

        self.playerDirection = self.playerSkin = self.playerWalkingSkin = None  # None is NULL
        self.updatePlayerDirection("right")

        self.playerSurface = self.playerSkin

        # Create a variable to store the player's position.
        self.playerPOS = self.playerOldPOS = pygame.Vector2(
            WIDTH / 2, HEIGHT / 2)

        self.walkingFrame = 0
        self.totalWalkingFrames = 6
        self.animationSpeed = 0.1

        self.frameWidth = self.playerWidth = self.playerSkin.get_width()
        self.frameHeight = self.playerHeight = self.playerSkin.get_height()

        self.totalFramesWidth = self.frameWidth * self.totalWalkingFrames

    def updatePlayerDirection(self, direction):
        if direction in ["right", "left"]:
            self.playerDirection = direction
            self.playerSkin = pygame.image.load(
                f"src/images/Scar_L_Solider/index/{self.playerDirection}.png")
            self.playerWalkingSkin = pygame.image.load(
                f"src/images/Scar_L_Solider/walk/{self.playerDirection}.png")

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
            self.updatePlayerDirection("left")
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.playerPOS.x += self.playerSpeed
            self.updatePlayerDirection("right")
        self.oldPlayerPOS = self.playerPOS

    def updateAllPlayerIntents(self):
        self.movePlayer()

        if self.walkingFrame >= (self.totalWalkingFrames - self.animationSpeed):
            self.walkingFrame = 0
        else:
            self.walkingFrame = round(
                self.walkingFrame + self.animationSpeed, 2)

        if self.walkingFrame % 1 == 0:
            if self.playerDirection == "right":
                self.playerSurface = self.playerWalkingSkin.subsurface(
                    (self.walkingFrame * 128, 0, 128, 128))
            else:
                n = (self.totalWalkingFrames - self.walkingFrame)
                if n == self.totalWalkingFrames:
                    n = 0

                self.playerSurface = self.playerWalkingSkin.subsurface(
                    n * 128, 0, 128, 128)

        return self.playerSurface
