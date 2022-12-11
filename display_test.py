import time

from src.microbit import Microbit
import src.patterns as pt

if __name__ == "__main__":
    mb = Microbit()
    running = True
    while running:
        mb.led_array = pt.SMILE
        mb.draw()
        time.sleep(1)

        mb.led_array = pt.SAD
        mb.draw()
        time.sleep(1)

        mb.led_array = pt.A
        mb.draw()
        time.sleep(1)

        mb.led_array = pt.B
        mb.draw()
        time.sleep(1)

        mb.led_array = [
            [0,2,4,6,8],
            [0,2,4,6,8],
            [0,2,4,6,8],
            [0,2,4,6,8],
            [0,2,4,6,8]
        ]
        mb.draw()
        time.sleep(1)


        mb.led_array = pt.BLANK
        mb.draw()
        time.sleep(1)

        mb.events()
        mb.draw()