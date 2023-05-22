import pygame
import src.utils.constants as C
from src.models.character import Character
from src.models.diamonds import Diamonds
from src.models.player import Player
from src.models.ghost import Ghost


class TheGame():
    def __init__(self):
        pygame.init()  # Initialize Pygame.

        # Create the screen.
        self.screen = pygame.display.set_mode(
            (C.screen["width"], C.screen["height"]))
        self.score = 0
        # Set the window title.
        pygame.display.set_caption("Don't touch my diamonds!")

        self.clock = pygame.time.Clock()  # Create a clock object.
        # Create a variable to track if the game is running.
        self.running = True

        self.player = Player(
            C.screen["width"] / 2, C.screen["height"] / 2, 0.5)
        self.diamonds = Diamonds()
        self.ghost = Ghost()

        self.gameCanvas = pygame.Surface(
            (C.canvas["width"], C.canvas["height"]))
        self.backgroundImg = pygame.image.load(
            "src/assets/images/map/grass.png")

    def initializeNewFrame(self):
        self.gameCanvas.blit(self.backgroundImg, (0, 0))

    def loadFrame(self):
        self.screen.blit(pygame.transform.scale(
            self.gameCanvas, (C.screen["width"], C.screen["height"])), (0, 0))

        pygame.display.flip()  # Flip to next frame
        self.clock.tick(60)  # Wait for 1/60th of a second.

    def updateFrame(self):
        self.initializeNewFrame()

        if len(self.diamonds.allDiamonds) < 1:
            self.diamonds.generateDiamonds(self.gameCanvas, 1)
        self.diamonds.blitAll(self.gameCanvas)

        touchingDiamond = self.player.isTouchingRect(
            self.diamonds.allDiamonds[0])
        if touchingDiamond:
            self.diamonds.allDiamonds.remove(self.diamonds.allDiamonds[0])
            self.score += 1

        self.ghost.follow(self.player.pos)
        self.ghost.render(self.gameCanvas)

        scoreText = pygame.font.Font("src/assets/fonts/main.ttf", 8).render(
            f"Score: {self.score}", True, (255, 255, 255))
        self.gameCanvas.blit(scoreText, (10, 10))

        self.player.movingHandler()
        self.player.render(self.gameCanvas)

    def stop(self):
        self.running = False
