import pygame
import src.constants as C
from src.utils.character import Character

# TODO: in short just clean the fucking code bro
class Player(Character):
    def __init__(self, x, y, speed):
        # TODO: Move this crap out to either Character class or else

        # Initialize the extended classes
        super().__init__()

        # Create a variable to store the player's position.
        self.playerPOS = pygame.Vector2(x, y)
        self.playerOldPOS = {"x": 0, "y": 0}

        # Player initialize
        self.playerSurface = self.status["walking"]["skin"]["index"]

    def movePlayer(self):
        self.playerSurface = self.status["walking"]["skin"]["index"]

        keys = pygame.key.get_pressed()
        self.playerOldPOS["x"] = self.playerPOS.x
        self.playerOldPOS["y"] = self.playerPOS.y

        # Check if the player is about to go off screen.
        if self.playerPOS.x < 0:
            self.playerPOS.x = 0
        elif self.playerPOS.x >= C.screen["width"] - self.status["walking"]["dimensions"]["width"]:
            self.playerPOS.x = C.screen["width"] - \
                self.status["walking"]["dimensions"]["width"]
            

        # TODO: Bruh bro! the player can go off screen down
        if self.playerPOS.y < 0:
            self.playerPOS.y = 0
        elif self.playerPOS.y >= C.screen["width"] - self.status["walking"]["dimensions"]["height"]:
            self.playerPOS.y = C.screen["width"] - \
                self.status["walking"]["dimensions"]["height"]

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.playerPOS.y -= self.status["walking"]["speed"]
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.playerPOS.y += self.status["walking"]["speed"]
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.playerPOS.x -= self.status["walking"]["speed"]
            self.updateDirection("left")
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.playerPOS.x += self.status["walking"]["speed"]
            self.updateDirection("right")

    def updateAllPlayerIntents(self):
        self.movePlayer()

        if not self.playerOldPOS["x"] == self.playerPOS.x and self.playerOldPOS["y"] == self.playerPOS.y:
            if ((self.playerPOS.x - self.playerOldPOS["x"]) == self.status["walking"]["speed"]) or (abs(self.playerPOS.x - self.playerOldPOS["x"]) == abs(self.status["walking"]["speed"])):
                self.animate("walking")

        return self.playerSurface
    
    # TODO: And this crap too needs to move the fuck out of here

    def animate(self, animation):
        if not animation in self.animations:
            return "Bruh bro"

        animation = self.status["walking"]
        animationFrames = animation["frames"]["total"]["count"]
        animationSkin = animation["skin"]["animated"]
        currentFrame = self.status["walking"]["frames"]["current"]

        if currentFrame >= (animationFrames - self.status["walking"]["speed"]):
            self.status["walking"]["frames"]["current"] = 0
            print("reset")
        else:
            self.status["walking"]["frames"]["current"] = round(currentFrame + self.status["walking"]["frames"]["speed"], 2)
            print("plus")
            print(self.status["walking"]["frames"]["current"])

        #TODO: Figure out what does that do and fix it
        # if self.status["walking"]["frames"]["current"] % 1 == 0:
        #     if self.status["direction"] == "right":
        #         self.playerSurface = animationSkin.subsurface(
        #             (self.status["walking"]["frames"]["current"] * self.status["walking"]["dimensions"]["width"], 0, self.status["walking"]["dimensions"]["width"], self.status["walking"]["dimensions"]["height"]))
        #     else:
        #         n = (animationFrames - self.status["walking"]["frames"]["current"])
        #         if n == animationFrames:
        #             n = 0

        #         self.playerSurface = animationSkin.subsurface(
        #             n * self.status["walking"]["dimensions"]["width"], 0, self.status["walking"]["dimensions"]["width"], self.status["walking"]["dimensions"]["width"])