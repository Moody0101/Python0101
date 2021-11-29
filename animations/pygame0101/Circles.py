"""
this module helps you draw cirlces in pygame.
"""

import pygame
from random import choice, randint
from BoilerPlate import code
from math import sin
from numpy import random 





class Circle(code):
    """ A cirlce wrapper class that inherits from code. """
    def __init__(self, x, y, color, radius,MovinFunction=None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.MovinFunction = MovinFunction
        self.velocity = 1
        self.Xdirection, self.Ydirection = 1, 1
        self.run_()
    
    def draw(self) -> None:
        try:
            pygame.draw.circle(self.window, self.color, (self.x, self.y), self.radius)
        except:
            pygame.draw.circle(self.window, (0, 0, 0), (self.x, self.y), self.radius)
    
    def move(self):
        if not self.MovinFunction:
            
            if self.x > 450:
                self.Xdirection *= -1
            
            if self.x < 5:
                self.Xdirection *= -1
            
            if self.y > 450:
                self.Ydirection *= -1


            if self.y < 5:
                self.Ydirection *= -1

            self.x += (self.velocity*self.Xdirection)*random.uniform()*randint(0, 2)
            self.y += (self.velocity*self.Ydirection)*random.uniform()*randint(0, 3)

        else:
            self.x, self.y = self.MovinFunction(self.x, self.y)
    def addObject(self) -> None:
        pass
    def run_(self) -> None:
        self.clock.tick(30)
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.move()
            pygame.display.update()
            self.window.fill(self.Backgroundcolor)
            self.draw()
        pygame.quit()
def Moving(x, y):
    """suppose that sin(alpha) is the velocity and by mutiplying by a constant we increase the velocity of the circle. """
    return x + sin(x)*3, y + sin(y)*3

if __name__ == "__main__":
    Circle(250, 250, (255, 255, 255), 20 ,Title="Circle", Backgroundcolor=(19, 19, 19))