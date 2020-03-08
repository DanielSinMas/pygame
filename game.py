import pygame
from entities.player import *
from entities.enemy import *
from Constants import *

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 750)

# Run until the user asks to quit
clock = pygame.time.Clock()
running = True
player = Player()
enemy = Enemy()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
while running:

    pressed_keys = pygame.key.get_pressed()
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    player.update(pressed_keys)
    enemies.update()

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw the player on the screen
    screen.blit(player.surf, player.rect)
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.sprite.spritecollide(player, all_sprites, True)

    # Flip the display
    pygame.display.flip()
    clock.tick(60)

# Done! Time to quit.
pygame.quit()