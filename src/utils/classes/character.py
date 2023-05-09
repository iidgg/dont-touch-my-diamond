from src.utils.classes.object import Object

class Character(Object):
    def __init__(self):
        super().__init__()
    
    def updateAllIntents(self):
        self.movePlayer()

        if not self.position["x"] == self.position["x"] and self.position["y"] == self.position["y"]:
            if ((self.position["x"] - self.position["x"]) == self.status["walking"]["speed"]) or (abs(self.position["x"] - self.position["x"]) == abs(self.status["walking"]["speed"])):
                self.animate("walking")

        return self.surface