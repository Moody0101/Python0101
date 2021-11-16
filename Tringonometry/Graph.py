
import numpy as n
import pygame
from math import sin, pi, radians
from random import randint
pygame.init()
window = pygame.display.set_mode((1000, 700))
window.fill((19, 19, 19))
pygame.display.set_caption('circles')
Clock = pygame.time.Clock()


class Circle(object):
	def __init__(self, x: int, y: int, color: tuple, radius: int):
		self.x = x
		self.y = y
		self.color = color
		self.radius = radius
		self.vel = 50
		self.dx = 1
		self.dy = 1
		self.velocity = 3
	def spawn(self, window):
		try:
			pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)
		except:
			pygame.draw.circle(window, (0, 0, 0), (self.x, self.y), self.radius)

	def draw(self):
		self.spawn(window)
		
	def Move(self):
		if self.x > 900:
			self.dx = -1
		if self.x < 40:
			self.dx = 1
		if self.y == 300:
			self.dx = -2/3
		self.x += self.velocity*self.dx*randint(0, 5)
		
		if self.y > 700:
			self.dy = -1
		if self.y < 40:
			self.dy = 1
		if self.y == 300:
			self.dy = -2/3
		self.y += self.velocity*self.dy*randint(0, 5)
		# print(self.y, self.dy)
		# print(self.x, self.dx)


			

angels = [i*90 for i in range(20)]
ydata = [sin(radians(i))*30+500 for i in angels]
xdata = [i/3+100 for i in angels]
data = zip(xdata, ydata)
circles = [Circle(x, y,(255,255,255), 5) for x,y in data]

# for i in circles:
# 	print(i.x, i.y)
run = True
while run:
    Clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for circle in circles:
    	circle.draw()
    	circle.Move()
    pygame.display.update()
    window.fill((19,19,19))

pygame.quit()




"""
I was trying to make a graph using Matplotlib but I Had some problems in importing the lib
so it is better to make a new mechanism to plot using numpy, pygame.

class Grapher(p):
	def __init__(self, x_axis: list, y_axis: list, x_label:str="x", y_label: str="y") -> None:
		
		self.x_axis = x_axis
		self.y_axis = y_axis
		self.y_label = y_label
		self.x_label = x_label
		p.ylabel(self.y_label)
		p.xlabel(self.x_label)
		if self.y_axis and self.x_label:
			p.plot(self.x_axis, self.y_label)
		else:
			p.plot(self.x_axis)
		p.show()

def main(x=None, y=None):
	if x and y:
		Grapher(x, y)
	else:
		Grapher(x)


if __name__ == '__main__':
	main([i for i in range(100)], [i for i in range(100)])
import pandas as pd
data = pd.read_csv("C:\\Users\\pc\\Documents\\survey_results_public.csv")
print(data.info())
"""