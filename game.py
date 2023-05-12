import pygame
import src.constants as C
from src.utils.player import Player


pygame.init() # Initialize Pygame.
screen = pygame.display.set_mode((C.screen["width"], C.screen["height"])) # Create the screen.
pygame.display.set_caption("Don't touch my diamonds!") # Set the window title.
clock = pygame.time.Clock() # Create a clock object.
running = True # Create a variable to track if the game is running.

player = Player(C.screen["width"] / 2, C.screen["height"] / 2, 0.5)

while running:
    # Get all events that happened since the last frame.
    for event in pygame.event.get():
        # If the user closed the window, quit the game.
        if event.type == pygame.QUIT:
            running = False

    screen.fill("blue") # Fill the screen with blue.

    player.render(screen, True)
    

    pygame.display.flip() # Flip to next frame
    clock.tick(60) # Wait for 1/60th of a second.

pygame.quit() # Quit Pygame.