"""
this module helps you draw cirlces in pygame.
"""

import pygame
from random import choice, randint
def PygameInitializer():
    pygame.init()
    pygame.display.set_caption('circles')
PygameInitializer()

class Circle(object):
    clock = pygame.time.Clock()
    def __init__(self, x: int, y: int, color: tuple, radius: int):
        self.window = pygame.display.set_mode((500, 500))
        self.window.fill((255, 255, 255))
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.vel = 50
        self.dx = 1
        self.dy = 1
        self.velocity = 3
        self.run = True
    def spawn(self, window):
        try:
            pygame.draw.circle(self.window, self.color, (self.x, self.y), self.radius)
        except:
            pygame.draw.circle(self.window, (0, 0, 0), (self.x, self.y), self.radius)

    def draw(self):
        self.spawn(self.window)
        
    def Move(self):
        pass
        # print(self.y, self.dy)
        # print(self.x, self.dx)        
    def draw(self):
        self.spawn(self.window)
        pygame.display.update()    
    def run_(self):
        self.clock.tick(30)
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.Move()
            self.draw()
        pygame.quit()

    
Circle(250, 250, (10, 10, 10), 20).run_()