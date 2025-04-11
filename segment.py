# python
from microbit import sleep

class Segment:
    digit_map = {
        '0': [1,1,1,1,1,1,0],
        '1': [0,1,1,0,0,0,0],
        '2': [1,1,0,1,1,0,1],
        '3': [1,1,1,1,0,0,1],
        '4': [0,1,1,0,0,1,1],
        '5': [1,0,1,1,0,1,1],
        '6': [1,0,1,1,1,1,1],
        '7': [1,1,1,0,0,0,0],
        '8': [1,1,1,1,1,1,1],
        '9': [1,1,1,1,0,1,1],
        'A': [1,1,1,0,1,1,1],
        'B': [0,0,1,1,1,1,1],
        'C': [1,0,0,1,1,1,0],
        'D': [0,1,1,1,1,0,1],
        'E': [1,0,0,1,1,1,1],
        'F': [1,0,0,0,1,1,1],
        'G': [1,0,1,1,1,1,0],
        'H': [0,1,1,0,1,1,1],
        'I': [0,0,0,0,1,1,0],
        'J': [0,1,1,1,0,0,0],
        'L': [0,0,0,1,1,1,0],
        'N': [1,1,1,0,1,1,0],
        'O': [1,1,1,1,1,1,0],
        'P': [1,1,0,0,1,1,1],
        'Q': [1,1,1,0,0,1,1],
        'R': [1,1,0,0,1,1,0],
        'S': [1,0,1,1,0,1,1],
        'T': [0,0,0,1,1,1,1],
        'U': [0,1,1,1,1,1,0],
        'Y': [0,1,1,1,0,1,1],
        'Z': [1,1,0,1,1,0,1],
        ' ': [0,0,0,0,0,0,0]
    }

    def __init__(self, pins_list):
        self.digits = []
        for pins in pins_list:
            self.digits.append(pins)

    def set_char(self, idx, char):
        char = char.upper()
        data = self.digit_map.get(char, self.digit_map[' '])
        for pin, val in zip(self.digits[idx], data):
            pin.write_digital(val)

    def clear(self):
        for digit in self.digits:
            for seg in digit:
                seg.write_digital(0)

    def display(self, text):
        self.clear()
        for i in range(min(4, len(text))):
            self.set_char(i, text[i])

    def scroll(self, text, delay=400):
        padded = "    " + text.upper() + "    "
        for i in range(len(padded) - 3):
            self.display(padded[i:i+4])
            sleep(delay)
