import pygame
import src.constants as C
from src.utils.classes.object import Object

class Character(Object):
    def __init__(self):
        super().__init__()
    
    def updateAllIntents(self):
        self.updateMovements()

        newX, oldX = self.position["x"], self.position["old"]["x"]
        newY, oldY = self.position["y"], self.position["old"]["y"]
        isOldXisNewX =  newX == oldX
        isOldYisNewY = newY == oldY
        walkingSpeed = self.status["walking"]["speed"]

        if not isOldXisNewX and isOldYisNewY:
            if ((newX - oldX) == walkingSpeed) or (abs(newX - oldX) == abs(walkingSpeed)):
                self.animate("walking")

        return self.surface
    
    def updateMovements(self):
        keys = pygame.key.get_pressed()
        self.position["old"]["x"], self.position["old"]["y"] = self.position["x"], self.position["y"]

        # TODO: Bruh bro! the player can go off down screen
        # Check if the player is about to go off screen.
        if self.position["x"] < 0:
            self.position["x"] = 0
        elif self.position["x"] >= C.screen["width"] - self.status["walking"]["dimensions"]["width"]:
            self.position["x"] = C.screen["width"] - self.status["walking"]["dimensions"]["width"]
            
        if self.position["y"] < 0:
            self.position["y"] = 0
        elif self.position["y"] >= C.screen["width"] - self.status["walking"]["dimensions"]["height"]:
            self.position["y"] = C.screen["width"] - self.status["walking"]["dimensions"]["height"]
        # TODO: Ends the last todo, the code down there doesn't have anything to do with this bug

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.position["y"] -= self.status["walking"]["speed"]
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.position["y"] += self.status["walking"]["speed"]
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.position["x"] -= self.status["walking"]["speed"]
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.position["x"] += self.status["walking"]["speed"]

        if not (self.position["old"]["x"] == self.position["x"] and self.position["old"]["y"] == self.position["y"]):
            if not self.position["old"]["y"] == self.position["y"]:
                # Moved up or down
                ""
            else:
                if self.position["x"] - 0.5 == self.position["old"]["x"]:
                    "Moved right"
                    self.updateDirection("right")
                elif self.position["x"] + 0.5 == self.position["old"]["x"]:
                    "Moved left"
                    self.updateDirection("left")