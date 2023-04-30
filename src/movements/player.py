def playerMovments(pygame, playerPOS, playerSpeed):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        playerPOS.y -= playerSpeed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        playerPOS.y += playerSpeed
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        playerPOS.x -= playerSpeed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        playerPOS.x += playerSpeed