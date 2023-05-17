class Movements():
    def __init__(self):
        self.isMoveable = True

        self.directions = ["right", "left", "up", "up-right", "up-left", "down", "down-right", "down-left"]
        self.direction = "right" #? Why right? WHY NOT?
        self.oldDirection = None

    def updateDirection(self, direction):
        if self.direction == direction:
            return ""
        if direction in self.directions:
            self.oldDirection = self.direction
            self.direction = direction
            self.updateSkins()