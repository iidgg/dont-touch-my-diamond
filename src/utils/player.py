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

        self.playerSpeed = speed

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
            subsurface = self.playerSkin.subsurface((self.walkingFrame * 48, 0, 48, 48))

        return subsurface

    # if walkingFrame % 1 == 0:
    #     subsurface = playerSkin.subsurface((walkingFrame * 48, 0, 48, 48))

    # screen.blit(subsurface, playerPOS)
    # if walkingFrame >= (6 - 0.1):
    #     walkingFrame = 0
    # else:
    #     walkingFrame = round(walkingFrame + 0.1, 2)
    
    # oldPlayerPOS = playerPOS
    # playerMovments(pygame, playerPOS, playerSpeed, WIDTH, HEIGHT, playerWidth, playerHeight)