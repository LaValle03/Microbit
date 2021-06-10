import pygame
import pygame_menu

modalita = 1

file = open("modalita.txt", "w")
file.write(str(1))
file.close()

file = open("difficolta.txt", "w")
file.write(str(1))
file.close()


def set_modalita(value, mod):
    file = open("modalita.txt", "w")
    file.write(str(mod))
    file.close()

def set_difficolta(value, mod):
    file = open("difficolta.txt", "w")
    file.write(str(mod))
    file.close()

def avviaGioco():
    if open("modalita.txt", "r").read()[0] == '1':
        import main
    if open("modalita.txt", "r").read()[0] == '2':
        import microbit
    if open("modalita.txt", "r").read()[0] == '3':
        import accellerometro
    pygame.quit()


def main():
    pygame.init()
    surface = pygame.display.set_mode((700, 500))

    menu = pygame_menu.Menu(500, 700, 'PONG', theme=pygame_menu.themes.THEME_BLUE)

    menu.add_button('Gioca', avviaGioco)
    menu.add_selector('Modalità :', [('Tastiera', 1), ('Pulsanti', 2), ('Inclinazione', 3)], onchange=set_modalita)
    menu.add_selector('Difficoltà :', [('Facile', 1), ('Difficile', 2)], onchange=set_difficolta)
    menu.add_button('Esci', pygame_menu.events.EXIT)

    menu.mainloop(surface)

main()
