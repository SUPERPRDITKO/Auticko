from microbit import *
import time
from easymb import joystick as joy
import random
import radio

while True:
    x, y = joy.joystickGetXY(pin0, pin1, True)
    display.set_pixel(x, y, 9)
    #sleep(1)
    sleep(40)
    display.clear()
