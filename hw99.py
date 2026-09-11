import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Smart Traffic Signal Simulator")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define a custom event for changing colors/signal
CHANGE_SIGNAL_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_SIGNAL_EVENT, 3000)  # triggers every 3 seconds

# Car Sprite Class
class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Create a simple rectangular surface for the car
        self.image = pygame.Surface((50, 30))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT // 2
        self.velocity_x = 4
        self.signal_state = "GREEN"

    def update(self):
        # Move car if signal is green
        if self.signal_state == "GREEN":
            self.rect.x += self.velocity_x
        
        # Check boundary (e.g., reaching x = 600)
        if self.rect.right >= 600:
            self.velocity_x = 0  # Stop at boundary/signal

    def change_color(self):
        # Cycle car color or state
        colors = [RED, GREEN, BLUE]
        new_color = random.choice(colors)
        self.image.fill(new_color)

# Setup Sprite Groups
all_sprites = pygame.sprite.Group()
car = Car()
all_sprites.add(car)

# Game Loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = false
        elif event.type == CHANGE_SIGNAL_EVENT:
            car.change_color()
            if car.signal_state == "GREEN":
                car.signal_state = "RED"
            else:
                car.signal_state = "GREEN"
                car.velocity_x = 4

    # Update
    all_sprites.update()

    # Draw
    screen.fill(WHITE)
    all_sprites.draw(screen)
    
    # Draw a simple road boundary line
    pygame.draw.line(screen, (100, 100, 100), (600, 0), (600, SCREEN_HEIGHT), 5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
