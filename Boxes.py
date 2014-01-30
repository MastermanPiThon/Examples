import pygame
import sys

from pygame.locals import *
from pygame import *

class Boxes:
    def __init__ (self):
        self.displaySize = (640, 480)
        pygame.init()
        display.set_caption ("Boxes")

        self.clock = pygame.time.Clock ()
        self.display = display.set_mode (self.displaySize)
        mouseTracker = Box ((10, 10), (255, 255, 255), (100, 45))
        self.Boxes = [mouseTracker]
        self.Background = Box (self.displaySize, (0,0,0), (0,0))

    def run (self):
        while True:
            self.handleEvents ()
            
            self.Background.draw (self.display)
            for box in self.Boxes:
                box.update ()
                box.draw (self.display)

            display.update ()
            self.clock.tick (30)
            

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP:
                newBox = Box ((10,10), (255,255,255), (0,0))
                self.Boxes.append (newBox)

class Box:
    def __init__ (self, displaySize, color, position):
        self.box = Surface (displaySize)
        self.box.fill (color)
        self.position = position
        self.rect = self.box.get_rect ()

    def draw (self, display):
        display.blit (self.box, self.position)

    def update (self):
        self.position = mouse.get_pos ()
        self.rect.center = self.position

if __name__ == '__main__':
	game = Boxes()
	game.run()
