from microbit import *

while True:
    motoreA = button_a.is_pressed()
    motoreB = button_b.is_pressed()
    print(str(motoreA) + "," + str(motoreB) + ",")
    sleep(10)
