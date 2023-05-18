import pygame
import src.utils.constants as C
from src.player import Player
from src.models.diamonds import Diamonds


pygame.init() # Initialize Pygame.
screen = pygame.display.set_mode((C.screen["width"], C.screen["height"])) # Create the screen.
pygame.display.set_caption("Don't touch my diamonds!") # Set the window title.
clock = pygame.time.Clock() # Create a clock object.
running = True # Create a variable to track if the game is running.

diamonds = Diamonds()
allDiamonds = diamonds.allDiamonds
player = Player(C.screen["width"] / 2, C.screen["height"] / 2, 0.5)


while running:
    # Get all events that happened since the last frame.
    for event in pygame.event.get():
        # If the user closed the window, quit the game.
        if event.type == pygame.QUIT:
            running = False

    allDiamonds = diamonds.allDiamonds
    game_canvas = pygame.Surface((C.canvas["width"],C.canvas["height"]))
    game_canvas.fill("blue")
    grass_img = pygame.image.load("src/images/map/grass.png")
    game_canvas.blit(grass_img, (0,0))

    if len(diamonds.allDiamonds) < 5:
        diamonds.generateDiamonds(game_canvas, 5)

    diamonds.blitAll(game_canvas)

    player.updatePlayer()
    player.render(game_canvas, False)


    screen.blit(pygame.transform.scale(game_canvas,(C.screen["width"], C.screen["height"])), (0,0))

    pygame.display.flip() # Flip to next frame
    clock.tick(60) # Wait for 1/60th of a second.

pygame.quit() # Quit Pygame.