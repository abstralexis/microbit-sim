import sys

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
        Poll events to be called every frame
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

    def draw(self):
        """
        Draw pixel array to be called every frame
        """
        self.WIN.fill(BLACK)
        for i in range(5):
            for j in range(5):
                led = pygame.Surface((50, 50))
                led.fill(RED)
                led.set_alpha((255/9) * self.led_array[j][i])
                self.WIN.blit(led, (i*50, j*50))
        pygame.display.flip()