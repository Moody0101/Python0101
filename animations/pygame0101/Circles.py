import pygame
from random import choice

pygame.init()
window = pygame.display.set_mode((500, 500))
window.fill((255, 255, 255))
pygame.display.set_caption('circles')
Clock = pygame.time.Clock()


class Circle(object):
    def __init__(self, x: int, y: int, color: tuple, radius: int):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.vel = 50
    def spawn(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)
    def move(self):
        # direction = choice([1, -1])
        if 50 < self.x < 450 and 50 < self.y < 450: 
            self.x += 1
            self.y += 1
        elif self.x > 400:
            self.x -= 1
        elif self.y > 400:
            self.y -= 1
        elif self.x < 50:
            self.y += 1
        elif self.y < 50:
            self.x -= 1
        else:
            pass
        print(self.x, self.y)
        
        
        
def draw():
    circle.spawn(window)
    pygame.display.update()
circle = Circle(250, 250,(19, 19, 19), 20)
run = True
while run:
    Clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    circle.move()
    draw()
pygame.quit()
