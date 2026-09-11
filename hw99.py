import pygame
import random


pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Smart Traffic Signal Simulator")


WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

CHANGE_SIGNAL_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_SIGNAL_EVENT, 3000) 

class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface((50, 30))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT // 2
        self.velocity_x = 4
        self.signal_state = "GREEN"

    def update(self):
        
        if self.signal_state == "GREEN":
            self.rect.x += self.velocity_x
        
        
        if self.rect.right >= 600:
            self.velocity_x = 0 

    def change_color(self):
     
        colors = [RED, GREEN, BLUE]
        new_color = random.choice(colors)
        self.image.fill(new_color)


all_sprites = pygame.sprite.Group()
car = Car()
all_sprites.add(car)


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


    all_sprites.update()


    
   
    pygame.draw.line(screen, (100, 100, 100), (600, 0), (600, SCREEN_HEIGHT), 5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
