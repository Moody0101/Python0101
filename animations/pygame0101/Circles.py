"""
this module helps you draw cirlces in pygame.
"""

import pygame
from random import choice, randint
def PygameInitializer(title):
    pygame.init()
    pygame.display.set_caption(title)
PygameInitializer("circles")

class Circle(object):
    
    def __init__(self, w, x: int, y: int, color: tuple, radius: int):
        self.w = w
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius

    def draw(self):
        try:
            pygame.draw.circle(self.window, self.color, (self.x, self.y), self.radius)
        except:
            pygame.draw.circle(self.window, (0, 0, 0), (self.x, self.y), self.radius)
        pygame.display.update()        

if __name__ == "__main__":
    Circle(250, 250, (10, 10, 10), 20)