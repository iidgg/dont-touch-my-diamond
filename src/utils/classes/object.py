import pygame

class Object:
    def __init__(self):
        self.pos = {
            "x": 0,
            "y": 0,
            "xy": (0, 0),
            "ox": 0, # Old x
            "oy": 0, # Old y
            "oxy": (0, 0) # Old x and y
        }
    
    def setPosition(self, x, y):
        chosenX = x if x != "same" else self.pos["x"]
        chosenY = y if y != "same" else self.pos["y"]

        self.setX(chosenX)
        self.setY(chosenY)

    def setY(self, y):
        self.pos["oy"] = self.pos["y"]
        self.pos["y"] = y

    def setX(self, x):
        self.pos["ox"] = self.pos["x"]
        self.pos["x"] = x

    def swapPosition(self):
        self.setPosition("same", "same")