import pygame
NERO = (0,0,0)
 
class Giocatore(pygame.sprite.Sprite):
    def __init__(self, colore, lunghezza, altezza):
        super().__init__()
        self.dimensioni = [lunghezza, altezza]

        self.image = pygame.Surface([lunghezza, altezza])
        self.image.fill(NERO)
        self.image.set_colorkey(NERO)
 
        pygame.draw.rect(self.image, colore, [0, 0, lunghezza, altezza])
        
        self.rect = self.image.get_rect()
    

    def muoviSu(self, pixels):
        self.rect.y -= pixels

        if self.rect.y < 0:
          self.rect.y = 0
          
    def muoviGiu(self, pixels):
        self.rect.y += pixels

        if self.rect.y > 400:
          self.rect.y = 400

    def IA(self, y):
        print(open("difficolta.txt", "r").read())
        if self.rect.y + self.dimensioni[1] / 2 > y:
            if open("difficolta.txt", "r").read() == '1':
                self.muoviSu(2)
            else:
                self.muoviSu(5)

        if self.rect.y + self.dimensioni[1] / 2 < y:
            if open("difficolta.txt", "r").read() == '1':
                self.muoviGiu(2)
            else:
                self.muoviGiu(5)