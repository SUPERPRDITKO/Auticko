from microbit import *
def joystickGetXY(pinX, pinY):
    
    #pin2.set_pull(pin2.PULL_UP)
    #divide it to 5*5 range
    segmentSize = 1024 /5
    
    #X axes
    coordsX = pinX.read_analog()
    coordsX = int(coordsX / segmentSize)

    #Y axes
    coordsY = pinY.read_analog()
    coordsY = int(coordsY / segmentSize)

    return coordsX, coordsY

    
#scanning for radio and connection + str or int conversion
while True:
    x, y = joystickGetXY(pin0, pin1)
    display.set_pixel(x, y, 9)
    sleep(1)
    display.clear()
