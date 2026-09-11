import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader Project - Part 1")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Clock to control frame rate
clock = pygame.time.Clock()

# Global score variable
score = 0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Create a blue square for the player
        self.image = pygame.Surface((40, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
        self.speed = 5

    def update(self):
        # Basic movement controls (Arrow keys)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Create a red square for the enemy
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        # Position randomly across the screen
        self.rect.x = random.randint(0, SCREEN_WIDTH - 30)
        self.rect.y = random.randint(50, SCREEN_HEIGHT - 150)

    def respawn(self):
        # Move to a new random location after a collision
        self.rect.x = random.randint(0, SCREEN_WIDTH - 30)
        self.rect.y = random.randint(50, SCREEN_HEIGHT - 150)

# Create sprite groups
all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

# Instantiate player
player = Player()
all_sprites.add(player)

# Instantiate 7 enemies at random positions
for _ in range(7):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemy_group.add(enemy)

# Font for displaying the score
font = pygame.font.SysFont(None, 36)

# Main Game Loop
running = True
while running:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Update Sprites
    all_sprites.update()

    # 3. Collision Detection
    # Detect collisions between the player and any sprite in the enemy group
    # setting dokill=False so we can manually handle respawning them
    collided_enemies = pygame.sprite.spritecollide(player, enemy_group, False)
    
    for enemy in collided_enemies:
        score += 1         # Increase score by one
        enemy.respawn()    # Teleport enemy to a new random position

    # 4. Drawing / Rendering
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Render and display the score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    # Maintain 60 frames per second
    clock.tick(60)

pygame.quit()
