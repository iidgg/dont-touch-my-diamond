def playerMovments(pygame, playerPOS, playerSpeed, WIDTH, HEIGHT):
    keys = pygame.key.get_pressed()

    # Check if the player is about to go off screen.
    if playerPOS.x < 0:
        playerPOS.x = 0
    elif playerPOS.x >= WIDTH - 10:
        playerPOS.x = WIDTH - 10
    
    if playerPOS.y < 0:
        playerPOS.y = 0
    elif playerPOS.y >= HEIGHT - 30:
        playerPOS.y = HEIGHT - 30

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        playerPOS.y -= playerSpeed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        playerPOS.y += playerSpeed
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        playerPOS.x -= playerSpeed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        playerPOS.x += playerSpeed