import pygame
import src.constants as C

class SM():
    def __init__(self):
        self.isMoveable = True

        self.directions = ["right", "left", "up", "up-right", "up-left", "down", "down-right", "down-left"]
        self.direction = "right" #? Why right? WHY NOT?
        self.oldDirection = None

        self.pos = {
            "x": 0,
            "y": 0,
            "xy": (0, 0),
            "ox": 0, # Old x
            "oy": 0, # Old y
            "oxy": (0, 0) # Old x and y
        }

        # # All available animations
        # self.animations = a = ["walking"]

        # """"
        # Structure:
        # "Animation"
        # "AnimationSpeed"
        # "Speed * Number = the player speed *Speed = The given speed to the class*"
        # """  # With spaces between each
        # self.AI = [f"{a[0]} 0.1 0.5"]
        # # ^ Animation information

        # self.hasSkin = True
        # self.skin = "" # Pygame load something
        # self.skinName = "arashi" # TODO: Remove hardcode
        
        # self.updateSkins()

    def updateDirection(self, direction):
        if self.direction == direction:
            return ""
        if direction in self.directions:
            self.oldDirection = self.direction
            self.direction = direction
            self.updateSkins()
    
    def updateMovements(self):
        keys = pygame.key.get_pressed()
        # self.pos["ox"], self.pos["oy"] = self.pos["x"], self.pos["y"]
        self.swapPosition()

        walkingWidth = self.status["walking"]["dimensions"]["width"]
        walkingHeight = self.status["walking"]["dimensions"]["height"]

        # TODO: Bruh bro! the player CAN go off down screen
        # Check if the player is about to go off screen.
        if self.pos["x"] < 0:
            self.setX(0)
        elif self.pos["x"] >= C.screen["width"] - walkingWidth:
            self.setX(C.screen["width"] - walkingWidth)
            
        if self.pos["y"] < 0:
            self.setY(0)
        elif self.pos["y"] >= C.screen["width"] - walkingHeight:
            self.setY(C.screen["width"] - walkingHeight)
        # TODO: Ends the last todo, the code down there doesn't have anything to do with this bug

        ws = self.status["walking"]["speed"] # Walking speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.changeYby(-ws)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.changeYby(ws)
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.changeXby(-ws)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.changeXby(ws)

        self.followMovements()