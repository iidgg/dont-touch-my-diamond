import pygame
from movements.player import playerMovments


pygame.init()
WIDTH, HEIGHT = 1080, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Don't touch my diamons!")
clock = pygame.time.Clock()
running = True

playerSkin = pygame.image.load("src/images/woodcutter/index.png")
playerPOS = oldPlayerPOS = pygame.Vector2(WIDTH / 2, HEIGHT / 2)
playerSpeed = 3

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("blue")
    screen.blit(playerSkin, playerPOS)

    oldPlayerPOS = playerPOS
    playerMovments(pygame, playerPOS, playerSpeed)

    pygame.display.flip() # Flip to next frame
    clock.tick(60)

pygame.quit()