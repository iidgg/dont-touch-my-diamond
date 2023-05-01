def playerMovments(pygame, playerPOS, playerSpeed, WIDTH, HEIGHT, playerWidth, playerHeight):
    keys = pygame.key.get_pressed()

    # Check if the player is about to go off screen.
    if playerPOS.x < 0:
        playerPOS.x = 0
    elif playerPOS.x >= WIDTH - playerWidth:
        playerPOS.x = WIDTH - playerWidth
    
    if playerPOS.y < 0:
        playerPOS.y = 0
    elif playerPOS.y >= HEIGHT - playerHeight:
        playerPOS.y = HEIGHT - playerHeight

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        playerPOS.y -= playerSpeed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        playerPOS.y += playerSpeed
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        playerPOS.x -= playerSpeed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        playerPOS.x += playerSpeed