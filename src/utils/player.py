import pygame
import src.constants as C
from src.utils.character import Character


class Player(Character):
    def __init__(self, x, y, speed):
        # Initialize the extended classes
        super().__init__()

        # Create a variable to store the player's position.
        self.playerPOS = pygame.Vector2(x, y)
        self.playerOldPOS = {"x": 0, "y": 0}

        # Player initialize
        self.playerIndex = self.getPlayerIndex()
        self.playerDimensions = {
            "width": self.playerIndex.get_width(), "height": self.playerIndex.get_height()}
        self.playerSurface = self.playerIndex

        # Player walking animation information
        self.walking = {
            "speed": speed,
            "skin": None,
            "frames": 0
        }

    def getPlayerIndex(self):
        s = self.playerIndex = pygame.image.load(
            f"src/images/{self.status['skin']}/walking/index/{self.status['direction']}.png")
        return s

    def movePlayer(self):
        keys = pygame.key.get_pressed()
        self.playerOldPOS["x"] = self.playerPOS.x
        self.playerOldPOS["y"] = self.playerPOS.y

        # Check if the player is about to go off screen.
        if self.playerPOS.x < 0:
            self.playerPOS.x = 0
        elif self.playerPOS.x >= C.screen["width"] - self.playerDimensions["width"]:
            self.playerPOS.x = C.screen["width"] - \
                self.playerDimensions["width"]

        if self.playerPOS.y < 0:
            self.playerPOS.y = 0
        elif self.playerPOS.y >= C.screen["width"] - self.playerDimensions["height"]:
            self.playerPOS.y = C.screen["width"] - \
                self.playerDimensions["height"]

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.playerPOS.y -= self.walking["speed"]
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.playerPOS.y += self.walking["speed"]
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.playerPOS.x -= self.walking["speed"]
            # self.updatePlayerDirection("left")
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.playerPOS.x += self.walking["speed"]
            # self.updatePlayerDirection("right")

    def updateAllPlayerIntents(self):
        self.movePlayer()

        # if not self.playerOldPOS["x"] == self.playerPOS.x and self.playerOldPOS["y"] == self.playerPOS.y:
        #     if ((self.playerPOS.x - self.playerOldPOS["x"]) == self.walking["speed"]) or (abs(self.playerPOS.x - self.playerOldPOS["x"]) == abs(self.walking["speed"])):
        #         self.animate("walking")

        return self.playerSurface

    # def animate(self, animation):
    #     if not animation in self.animations:
    #         return "Bruh bro"

    #     animation = self.__dict__[animation]
    #     animationFrames = animation["frames"]
    #     animationSkin = animation["skin"]

    #     if self.animation["frame"] >= (animationFrames - self.animation["speed"]):
    #         self.animation["frame"] = 0
    #     else:
    #         self.animation["frame"] = round(
    #             self.animation["frame"] + self.animation["speed"], 2)

    #     if self.animation["frame"] % 1 == 0:
    #         if self.status["direction"] == "right":
    #             self.playerSurface = animationSkin.subsurface(
    #                 (self.animation["frame"] * self.frame["width"], 0, self.frame["width"], self.frame["height"]))
    #         else:
    #             n = (animationFrames - self.animation["frame"])
    #             if n == animationFrames:
    #                 n = 0

    #             self.playerSurface = animationSkin.subsurface(
    #                 n * self.frame["width"], 0, self.frame["width"], self.frame["height"])