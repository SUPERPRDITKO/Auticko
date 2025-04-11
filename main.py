from microbit import *
import time
def joystickGetXY(pinX, pinY, screen):

    #pin2.set_pull(pin2.PULL_UP)
    #divide it to 5*5 range
    segmentSize = 1024 /5

    #X axes
    coordsX = pinX.read_analog()
    if screen:
        coordsX = int(coordsX / segmentSize)

    #Y axes
    coordsY = pinY.read_analog()
    if screen:
        coordsY = int(coordsY / segmentSize)
    return coordsX, coordsY

def driveServo(pin, num):
    if num > 1024 or num < 0:
        raise ValueError("Input value must be between 0 and 1024.")
    new_value = 8 + num * (134 - 8) / 1024
    pin.write_analog(new_value)
    return True

def controlPasswordSet():
    """ pause the cont. and search for password in all channels"""
    radio.on()
    password = 0
    chan = 0
    while True:
        display.show(password)
        chan += 1
        try: radio.config(channel= chan)
        except: chan = 0
            
        if button_b.was_pressed():
            password += 1
            if (password == 10):
                password = 0
        if (radio.receive() == str(password)):
            display.scroll("y")
            break

def carSet():
    """ pause the car and await the signal matching the password """
    radio.on()
    password = 0
    chan = 1
    while True:
        display.show(password)
        sleep(400)
        display.show(chan)
        sleep(400)
        display.show(Image.HEART)
        sleep(800)
        if button_a.was_pressed():

            password += 1
        elif button_b.was_pressed():
            chan += 1
            radio.config(channel= chan)
            
        radio.send(str(password))
        if (radio.receive() == str(password)):
            display.scroll("y")
            break


while True:
    x, y = joystickGetXY(pin0, pin1, False)
    driveServo(pin8, y)
    x, y = joystickGetXY(pin0, pin1, True)
    display.set_pixel(x, y, 9)
    #sleep(1)
    display.clear()

