from microbit import *  # noqa: F403

class TM1637:
    def __init__(self, clk, dio):
        self.clk = clk
        self.dio = dio
        self.clk.write_digital(1)
        self.dio.write_digital(1)

    def start(self):
        self.dio.write_digital(1)
        self.clk.write_digital(1)
        self.dio.write_digital(0)
        self.clk.write_digital(0)

    def stop(self):
        self.clk.write_digital(0)
        self.dio.write_digital(0)
        self.clk.write_digital(1)
        self.dio.write_digital(1)

    def write_byte(self, b):
        for i in range(8):
            self.clk.write_digital(0)
            self.dio.write_digital((b >> i) & 1)
            sleep(1)
            self.clk.write_digital(1)
            sleep(1)
        # ACK bit
        self.clk.write_digital(0)
        self.dio.write_digital(1)
        self.clk.write_digital(1)
        sleep(1)
        self.clk.write_digital(0)

    def set_brightness(self, brightness):
        brightness = max(0, min(7, brightness))
        self.start()
        self.write_byte(0x88 | brightness)
        self.stop()

    def show(self, data):
        self.start()
        self.write_byte(0x40)  # Auto increment
        self.stop()
        self.start()
        self.write_byte(0xC0)  # Start address
        for b in data:
            self.write_byte(b)
        self.stop()

class joystick:

    def GetXY(pinX, pinY, screen):

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

class laser:
    class Laser:
        def __init__(self, pin=pin0, power=512):
            self.pin = pin
            self.power = power

        def on(self):
            self.pin.write_analog(self.power)

        def off(self):
            self.pin.write_digital(0)

        def shoot(self, duration=500):
            self.on()
            sleep(duration)
            self.off()

class segment:
    class Segment:
        digit_map = {
            '0': 0x3F, '1': 0x06, '2': 0x5B, '3': 0x4F,
            '4': 0x66, '5': 0x6D, '6': 0x7D, '7': 0x07,
            '8': 0x7F, '9': 0x6F, 'A': 0x77, 'B': 0x7C,
            'C': 0x39, 'D': 0x5E, 'E': 0x79, 'F': 0x71,
            'G': 0x3D, 'H': 0x76, 'I': 0x30, 'J': 0x1E,
            'L': 0x38, 'N': 0x54, 'O': 0x3F, 'P': 0x73,
            'Q': 0x67, 'R': 0x50, 'S': 0x6D, 'T': 0x78,
            'U': 0x3E, 'Y': 0x6E, 'Z': 0x5B, ' ': 0x00
        }

        def __init__(self, clk=pin0, dio=pin1):
            self.disp = TM1637(clk, dio)
            self.disp.set_brightness(7)
            self.buffer = [' '] * 4

        def display(self, text):
            padded = (text.upper() + "    ")[:4]
            self.buffer = list(padded)
            self._update()

        def _update(self):
            data = [self.digit_map.get(c, 0x00) for c in self.buffer]
            self.disp.show(data)

        def scroll(self, text, speed=50):
            padded = "    " + text.upper() + "    "
            for i in range(len(padded) - 3):
                self.buffer = list(padded[i:i+4])
                t = 0
                while t < speed:
                    self._update()
                    sleep(5)
                    t += 5


