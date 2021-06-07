import sys
import serial, time
import pygame as pg
import threading, queue
import time
import pygame

#pygame config
width = 1200
height = 800
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()
ball = pg.image.load("C:\\Users\\rosse\\OneDrive\\Desktop\\Nuova cartella\\intro_ball.gif")
ballrect = ball.get_rect()
ballrect.centerx = width//2
ballrect.centery = height//2


black = 0, 0, 0
dt = 1
gamma = 0.05
q = queue.Queue()

#importo delle classi utilizzate nel gioco
from giocatore import Giocatore
from palla import Palla

q = queue.Queue()

#COLORI
NERO = (0,0,0)
BIANCO = (255,255,255)




class Read_Microbit(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._running = True
      
    def terminate(self):
        self._running = False
        
    def run(self):
        #serial config
        port = "COM7"
        s = serial.Serial(port)
        s.baudrate = 115200
        while self._running:
            data = s.readline().decode() 
            acc = [float(x) for x in data[1:-3].split(",")]
            q.put(acc)
            time.sleep(0.01)


def main():
    pygame.init()
    clock = pygame.time.Clock()
    
    thread = Read_Microbit()
    thread.start()

    #inizializzazione dello schermo
    dimensioni_schermo = (700, 500)
    screen = pygame.display.set_mode(dimensioni_schermo)

    #dichiarazione dei giocatori
    giocatore1 = Giocatore(BIANCO, 10, 100)
    giocatore1.rect.x = 20
    giocatore1.rect.y = 200

    giocatore2 = Giocatore(BIANCO, 10, 100)
    giocatore2.rect.x = 670
    giocatore2.rect.y = 200

    #dichiarazione della palla
    palla = Palla(BIANCO,10,10)
    palla.rect.x = 345
    palla.rect.y = 195

    #lista degli oggetti del gioco(giocatori e palla)
    oggetti = pygame.sprite.Group()

    oggetti.add(giocatore1)
    oggetti.add(giocatore2)
    oggetti.add(palla)

    #punteggio dei giocatori
    punteggio1 = 0
    punteggio2 = 0


    gioco = True


    pygame.font.init() 
    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    while gioco:
        #chiusura pulita del gioco
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gioco = False

        #uso della tastiera per muovere il giocatore 1
        keys = (q.get()).split(",")

        if keys[0] == "True":
            giocatore1.muoviSu(5)
        if keys[1] == "True":
            giocatore1.muoviGiu(5)

        #uso dell'intelligenza artificiale per muovere il giocatore 2
        giocatore2.IA(palla.getY())

        oggetti.update()

        #controlla se la palla rimbalza contro un muro
        if palla.rect.x>=690:
            punteggio1+=1
            palla.velocita[1] = 0
            palla.reset()
        if palla.rect.x<=0:
            punteggio2+=1
            palla.velocita[1] = 0
            palla.reset()
        if palla.rect.y>490:
            palla.velocita[1] = -palla.velocita[1]
        if palla.rect.y<0:
            palla.velocita[1] = -palla.velocita[1]

        #controlla se la palla colpisce altri oggetti
        if pygame.sprite.collide_mask(palla, giocatore1) or pygame.sprite.collide_mask(palla, giocatore2):
            palla.rimbalza()


        #aggiornamento dello schermo
        screen.fill(NERO)
        pygame.draw.line(screen, BIANCO, [349, 0], [349, 500], 5)
        oggetti.draw(screen)

        #visualizzazione del punteggio
        font = pygame.font.Font(None, 74)
        text = font.render(str(punteggio1), 1, BIANCO)
        screen.blit(text, (250,10))
        text = font.render(str(punteggio2), 1, BIANCO)
        screen.blit(text, (420,10))

        pygame.display.flip()

        clock.tick(60)

        if punteggio2 == 5:
            screen.fill(NERO)
            textsurface = myfont.render('HAI VINTO', False, (255, 255, 255))
            screen.blit(textsurface,(0,0))
            gioco = False
            time.sleep(1000)
    pygame.quit()
'''
running = True
rm = Read_Microbit()
rm.start()
pg.init()
speed = [0, 0]
while running:
    acc = q.get()
    speed[0] = (1.-gamma)*speed[0] + dt*acc[0]/1024.
    speed[1] = (1.-gamma)*speed[1] + dt*acc[1]/1024.
    q.task_done()
    ballrect = ballrect.move(speed)
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(black)
    screen.blit(ball, ballrect)
    pg.display.flip()
    clock.tick(10)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
    
rm.terminate()
rm.join()

'''