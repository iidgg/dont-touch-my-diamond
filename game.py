import pygame

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
    screen.fill("purple")
    pygame.draw.circle(screen, "red", playerPOS, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        playerPOS.y -= playerSpeed
    if keys[pygame.K_s]:
        playerPOS.y += playerSpeed
    if keys[pygame.K_a]:
        playerPOS.x -= playerSpeed
    if keys[pygame.K_d]:
        playerPOS.x += playerSpeed

    pygame.display.flip()

    clock.tick(60)

pygame.quit()