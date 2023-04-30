import pygame
from movements.player import playerMovments


pygame.init()
WIDTH, HEIGHT = 1080, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cats")
clock = pygame.time.Clock()
running = True

playerPOS = pygame.Vector2(WIDTH / 2, HEIGHT / 2)
playerSpeed = 3

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("blue")
    pygame.draw.circle(screen, "red", playerPOS, 40)

    playerMovments(pygame, playerPOS, playerSpeed)

    pygame.display.flip() # Flip to next frame
    clock.tick(60)

pygame.quit()