import sys

import numpy

import pygame

COLOURS = (
    RED := (255, 0, 0),
    BLACK := (0, 0, 0)
)

class Microbit:
    """
    Microbit simulation class with API
    """
    def __init__(self):
        """
        Initialise Microbit simulator
        """
        pygame.init()
        self.WIN = pygame.display.set_mode((250,250))
        pygame.display.set_caption("MicroBit Simulator")
        self.led_array = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]
        ]

    def events(self):
        """
        Main
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self):
        """
        Draw pixel array
        """
        self.WIN.fill(BLACK)
        for i in range(5):
            for j in range(5):
                led = pygame.Surface((50, 50))
                led.fill(RED)
                led.set_alpha((255/9) * self.led_array[j][i])
                self.WIN.blit(led, (i*50, j*50))
        pygame.display.flip()
    
if __name__ == "__main__":
    mb = Microbit()
    running = True
    while running:
        mb.led_array = [
            [0,9,0,9,0],
            [0,9,0,9,0],
            [0,0,3,0,0],
            [9,0,3,0,9],
            [0,9,9,9,0]
        ]

        mb.events()
        mb.draw()