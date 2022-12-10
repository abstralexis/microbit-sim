import sys

import numpy

import pygame

COLOURS = (
    RED := (255, 0, 0),
    BLACK := (0, 0, 0)
)

class Microbit:
    def __init__(self):
        pygame.init()
        self.WIN = pygame.display.set_mode((250,250))
        pygame.display.set_caption("MicroBit Simulator")
        self.px_array = numpy.zeros((5, 5))
        
        self.main()

    def main(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

            self.draw()

    def draw(self):
        self.WIN.fill(BLACK)
        for i in range(5):
            for j in range(5):
                px_rect = pygame.rect.Rect(
                    i*50, 
                    j*50,
                    50,
                    50
                )
                pygame.draw.rect(
                    self.WIN,
                    RED,
                    px_rect,
                )
        pygame.display.flip()
    
if __name__ == "__main__":
    Microbit()