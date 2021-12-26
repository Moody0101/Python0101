"""
this module helps you draw cirlces in pygame.
"""


import pygame
from random import choice, randint, uniform
from BoilerPlate import code
from math import sin
from numpy import random
class circle:
    
    def __init__(self, win, x, y, color, radius):
        self.win = win
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.velocity = 2
        self.Ydirection = 1
        self.Xdirection = 1


    def draw(self):
        pygame.draw.circle(self.win, self.color, (self.x, self.y), self.radius)

    def move(self, w, h):
        print(self.x, self.y)
        if self.x >= w - 100:
            self.Xdirection = -1
        elif self.x <= 50:
            self.Xdirection = 1
        if self.x >= h - 100:
            self.Ydirection = -1
        elif self.y <= 50:
            self.Ydirection = 1
        
        self.y += self.Ydirection * self.velocity
        self.x +=  self.velocity * self.Xdirection


class BouncingCircles(code):
    """ A cirlce wrapper class that inherits from code. """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.circles = [
            circle(self.window, x, y, (255, 255, 255), 5) for x, y in zip([ i for i in range(10)], [ i for i in range(10)])
        ]
        self.run_()
    def draw(self) -> None:
        for i in self.circles:
            i.draw()
    def run_(self) -> None:
        self.clock.tick(30)
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            pygame.display.update()
            self.window.fill(self.Backgroundcolor)
            for i in self.circles:
                i.move(self.width, self.height)
            self.draw()
        pygame.quit()

if __name__ == "__main__":
    BouncingCircles("Circle", (0, 0, 0), 1000, 700)