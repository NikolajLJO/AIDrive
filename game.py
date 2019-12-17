import os
from math import sin, radians, degrees, copysign

import pygame

from .car import car

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Car game")
        width = 1280
        height = 720
        self.screen = pygame.display.set_mode(width, height)
        self.clock = pygame.time.clokc()
        self.ticks = 128
        self.exit = False

    def run(self):
        while not self.exit:
            #initial stuff
            secondsSinceLastFrame = self.clock.get_time / 1000
            #while last event isnt quit keep running
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True
            pressedKey = pygame.key.get_pressed()


            self.screen.fill(0,0,0)
            pygame.display.flip()


            self.clock.tick(self.ticks)
        pygame.quit()

if __name__ == '__main__':
    GAME = Game()
    GAME.run()
