import pygame
import src.utils.constants as C
from src.models.character import Character
from src.models.diamonds import Diamonds
from src.models.player import Player

class TheGame():
    def __init__(self):
        pygame.init() # Initialize Pygame.

        self.screen = pygame.display.set_mode((C.screen["width"], C.screen["height"])) # Create the screen.
        pygame.display.set_caption("Don't touch my diamonds!") # Set the window title.

        self.clock = pygame.time.Clock() # Create a clock object.
        self.running = True # Create a variable to track if the game is running.

        self.player = Player(C.screen["width"] / 2, C.screen["height"] / 2, 0.5)

        self.gameCanvas = pygame.Surface((C.canvas["width"],C.canvas["height"]))
        self.backgroundImg = pygame.image.load("src/images/map/grass.png")

    def initializeNewFrame(self):
        self.gameCanvas.blit(self.backgroundImg, (0,0))

    def loadFrame(self):
        # frameScaled = 
        self.screen.blit(pygame.transform.scale(self.gameCanvas,(C.screen["width"], C.screen["height"])), (0,0))

        pygame.display.flip() # Flip to next frame
        self.clock.tick(60) # Wait for 1/60th of a second.

    def updateFrame(self):
        self.initializeNewFrame()

        self.player.movingHandler()
        self.player.render(self.gameCanvas)

    def stop(self):
        self.running = False