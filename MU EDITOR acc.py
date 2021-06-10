from microbit import *

while True:
    acc = accelerometer.get_values()
    print(acc)
    sleep(20)
