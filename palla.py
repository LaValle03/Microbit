import pygame
from random import randint
 
NERO = (0, 0, 0)

class Palla(pygame.sprite.Sprite):
    def __init__(self, colore, lunghezza, altezza):
        super().__init__()
        self.image = pygame.Surface([lunghezza, altezza])
        self.image.fill(NERO)
        self.image.set_colorkey(NERO)
 
        pygame.draw.rect(self.image, colore, [0, 0, lunghezza, altezza])
        
        self.velocita = [randint(4,8),randint(-8,8)]
        
        self.rect = self.image.get_rect()
    
    def getY(self):
        return self.rect.y
    
    def update(self):
        self.rect.x += self.velocita[0]
        self.rect.y += self.velocita[1]
          
    def rimbalza(self):
        self.velocita[0] = -self.velocita[0]
        self.velocita[1] = randint(-8,8)

    def reset(self):
        self.rect.x = 345
        self.rect.y = 195