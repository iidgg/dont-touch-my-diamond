import pygame
import constants


class Player:
    def __init__(self, x, y, speed):
        # Player init location
        self.x = x
        self.y = y

        # Create a variable to store the player's position.
        self.playerPOS = self.playerOldPOS = pygame.Vector2(
            constants.screen["WIDTH"] / 2, constants.screen["HEIGHT"] / 2)

        # Player walking information
        self.walking = {
            "speed": speed,
            "skin": None,
            "frames": 6
        }

        # Player direction
        self.playerDirection = "right"  # Is player facing left or right?
        

        self.skin = "Scar_L_Solider"
        self.playerIndex = self.getPlayerIndex()
        self.playerDimensions = {"width": 0, "height": 0}
        self.playerSurface = self.playerIndex

        self.updatePlayerDirection("right")

        # Animation
        self.animation = {
            "frame": 0,
            "totalFrames": 6,
            "speed": 0.1
        }

        self.frameWidth = self.playerIndex.get_width()
        self.frameHeight = self.playerIndex.get_height()

        self.totalFramesWidth = self.frameWidth * self.walking["frames"]

    def updatePlayerDirection(self, direction):
        if direction in ["right", "left"]:
            self.playerDirection = direction
            self.updatePlayerSkin()
    
    def updatePlayerSkin(self):
        self.getPlayerIndex()
        self.playerWalkingSkin = pygame.image.load(
            f"src/images/Scar_L_Solider/walk/{self.playerDirection}.png")
        
    def getPlayerIndex(self):
        p = self.playerIndex = pygame.image.load(
            f"src/images/Scar_L_Solider/index/{self.playerDirection}.png")
        return p
        

    def movePlayer(self):
        keys = pygame.key.get_pressed()

        # Check if the player is about to go off screen.
        if self.playerPOS.x < 0:
            self.playerPOS.x = 0
        elif self.playerPOS.x >= constants.screen["WIDTH"] - self.playerDimensions["width"]:
            self.playerPOS.x = constants.screen["WIDTH"] - self.playerDimensions["width"]

        if self.playerPOS.y < 0:
            self.playerPOS.y = 0
        elif self.playerPOS.y >= constants.screen["WIDTH"] - self.playerDimensions["height"]:
            self.playerPOS.y = constants.screen["WIDTH"] - self.playerDimensions["height"]

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.playerPOS.y -= self.walking["speed"]
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.playerPOS.y += self.walking["speed"]
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.playerPOS.x -= self.walking["speed"]
            self.updatePlayerDirection("left")
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.playerPOS.x += self.walking["speed"]
            self.updatePlayerDirection("right")
        self.oldPlayerPOS = self.playerPOS

    def updateAllPlayerIntents(self):
        self.movePlayer()

        if self.animation["frame"] >= (self.walking["frames"] - self.animation["speed"]):
            self.animation["frame"] = 0
        else:
            self.animation["frame"] = round(
                self.animation["frame"] + self.animation["speed"], 2)

        if self.animation["frame"] % 1 == 0:
            if self.playerDirection == "right":
                self.playerSurface = self.playerWalkingSkin.subsurface(
                    (self.animation["frame"] * 128, 0, 128, 128))
            else:
                n = (self.walking["frames"] - self.animation["frame"])
                if n == self.walking["frames"]:
                    n = 0

                self.playerSurface = self.playerWalkingSkin.subsurface(
                    n * 128, 0, 128, 128)

        return self.playerSurface
