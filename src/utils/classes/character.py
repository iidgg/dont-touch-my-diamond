import pygame
import src.constants as C
from src.utils.classes.object import Object

class Character(Object):
    def __init__(self):
        Object.__init__(self)
    
    def updateAllIntents(self):
        self.updateMovements()

        newX, oldX = self.position["x"], self.position["old"]["x"]
        newY, oldY = self.position["y"], self.position["old"]["y"]
        isOldXisNewX =  newX == oldX
        isOldYisNewY = newY == oldY
        walkingSpeed = self.status["walking"]["speed"]

        if not isOldXisNewX and isOldYisNewY:
            if abs(newX - oldX) == abs(walkingSpeed):
                self.animate("walking")

        return self.surface
    
    def updateMovements(self):
        keys = pygame.key.get_pressed()
        self.position["old"]["x"], self.position["old"]["y"] = self.position["x"], self.position["y"]

        # TODO: Bruh bro! the player CAN go off down screen
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

        self.followMovements()

    def followMovements(self):
        if not (self.position["old"]["x"] == self.position["x"] and self.position["old"]["y"] == self.position["y"]):
            if not self.position["old"]["y"] == self.position["y"]:
                "Moved up or down"
                if self.position["y"] - 0.5 == self.position["old"]["y"]:
                    "Moved down"
                elif self.position["y"] + 0.5 == self.position["old"]["y"]:
                    "Moved up"
            else:
                if self.position["x"] - 0.5 == self.position["old"]["x"]:
                    "Moved right" # TODO: Change the hardcoded 0.5 Up and down
                    self.updateDirection("right")
                elif self.position["x"] + 0.5 == self.position["old"]["x"]:
                    "Moved left"
                    self.updateDirection("left")

    def render(self, screen, isLatest):
        if isLatest:
            self.updateAllIntents()
        
        screen.blit(self.surface, (self.position["x"], self.position["y"]))