import pygame
import constants


class Player:
    def __init__(self, x, y, speed):
        # Player init location
        self.x = x
        self.y = y

        # Create a variable to store the player's position.
        self.playerPOS = pygame.Vector2(
            constants.screen["WIDTH"] / 2, constants.screen["HEIGHT"] / 2)
        self.playerOldPOS = {"x": 0, "y": 0}

        # Player direction
        self.playerDirection = "right"  # Is player facing left or right?

        # Player skin
        self.skin = "Scar_L_Solider"

        # Player initialize
        self.playerIndex = self.getPlayerIndex()
        self.playerDimensions = {"width": 0, "height": 0}
        self.playerSurface = self.playerIndex

        # Animation
        self.animation = {
            "frame": 0,
            "speed": 0.1
        }

        # Player walking animation information
        self.walking = {
            "speed": speed,
            "skin": None,
            "frames": 0
        }

        self.walking["skin"] = self.getPlayerWalkingSkin()
        self.walking["frames"] = self.walking["skin"].get_width() / \
            self.playerIndex.get_width()

        self.updatePlayerDirection("right")

        self.frame = self.playerDimensions

        self.totalFramesWidth = self.frame["width"] * self.walking["frames"]

    def updatePlayerDirection(self, direction):
        if direction in ["right", "left"]:
            self.playerDirection = direction
            self.updatePlayerSkin()

    def updatePlayerSkin(self):
        self.getPlayerIndex()
        self.getPlayerWalkingSkin()

    def getPlayerIndex(self):
        s = self.playerIndex = pygame.image.load(
            f"src/images/{self.skin}/walk/index/{self.playerDirection}.png")
        return s

    def getPlayerWalkingSkin(self):
        s = self.walking["skin"] = pygame.image.load(
            f"src/images/{self.skin}/walk/{self.playerDirection}.png")
        return s

    def movePlayer(self):
        keys = pygame.key.get_pressed()
        self.playerOldPOS["x"] = self.playerPOS.x
        self.playerOldPOS["y"] = self.playerPOS.y

        # Check if the player is about to go off screen.
        if self.playerPOS.x < 0:
            self.playerPOS.x = 0
        elif self.playerPOS.x >= constants.screen["WIDTH"] - self.playerDimensions["width"]:
            self.playerPOS.x = constants.screen["WIDTH"] - \
                self.playerDimensions["width"]

        if self.playerPOS.y < 0:
            self.playerPOS.y = 0
        elif self.playerPOS.y >= constants.screen["WIDTH"] - self.playerDimensions["height"]:
            self.playerPOS.y = constants.screen["WIDTH"] - \
                self.playerDimensions["height"]

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

    def updateAllPlayerIntents(self):
        self.movePlayer()

        if not self.playerOldPOS["x"] == self.playerPOS.x and self.playerOldPOS["y"] == self.playerPOS.y:
            self.animateWalking()

        return self.playerSurface
    
    def animateWalking(self):
        if self.animation["frame"] >= (self.walking["frames"] - self.animation["speed"]):
            self.animation["frame"] = 0
        else:
            self.animation["frame"] = round(
                self.animation["frame"] + self.animation["speed"], 2)

        if self.animation["frame"] % 1 == 0:
            if self.playerDirection == "right":
                self.playerSurface = self.walking["skin"].subsurface(
                    (self.animation["frame"] * 128, 0, 128, 128))
            else:
                n = (self.walking["frames"] - self.animation["frame"])
                if n == self.walking["frames"]:
                    n = 0

                self.playerSurface = self.walking["skin"].subsurface(
                    n * 128, 0, 128, 128)
