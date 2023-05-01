import pygame
from constants import *
from utils.movements.player import playerMovments # Define a function to move the player.


pygame.init() # Initialize Pygame.
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Create the screen.
pygame.display.set_caption("Don't touch my diamons!") # Set the window title.
clock = pygame.time.Clock() # Create a clock object.
running = True # Create a variable to track if the game is running.

playerSkin = pygame.image.load("src/images/woodcutter/walk.png") # Load the player image. a.k.a Skin
playerPOS = oldPlayerPOS = pygame.Vector2(WIDTH / 2, HEIGHT / 2) # Create a variable to store the player's position.
playerSpeed = 0.5 # Create a variable to store the player's speed.

playerWidth = playerSkin.get_width()
playerHeight = playerSkin.get_height()
walkingFrame = 0

while running:
    # Get all events that happened since the last frame.
    for event in pygame.event.get():
        # If the user closed the window, quit the game.
        if event.type == pygame.QUIT:
            running = False

    screen.fill("blue") # Fill the screen with blue.
    # screen.blit(playerSkin, playerPOS) # Draw the player on the screen.
    if walkingFrame % 1 == 0:
        subsurface = playerSkin.subsurface((walkingFrame * 48, 0, 48, 48))

    screen.blit(subsurface, playerPOS)
    if walkingFrame >= (6 - 0.1):
        walkingFrame = 0
    else:
        walkingFrame = round(walkingFrame + 0.1, 2)
    
    oldPlayerPOS = playerPOS
    playerMovments(pygame, playerPOS, playerSpeed, WIDTH, HEIGHT, playerWidth, playerHeight)

    pygame.display.flip() # Flip to next frame
    clock.tick(60) # Wait for 1/60th of a second.

pygame.quit() # Quit Pygame.