import pygame
from src.theGame import TheGame

game = TheGame()

while game.running:
    # Get all events that happened since the last frame.
    for event in pygame.event.get():
        # If the user closed the window, quit the game.
        if event.type == pygame.QUIT:
            game.stop()

    game.updateFrame()
    game.loadFrame()
    
pygame.quit() # Quit Pygame.
exit() # Exit life.