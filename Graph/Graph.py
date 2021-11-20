# Drowin x_axis
		# 	    def line(
		#     surface: Surface,
		#     color: _ColorValue,
		#     start_pos: _Coordinate,
		#     end_pos: _Coordinate,
		#     width: Optional[int] = 1,
		# ) -> Rect: ...

import pygame
from math import sin, cos, tan, e, prod




class Graph:
	clock = pygame.time.Clock()
	pygame.init()
	pygame.display.set_caption("GRAPH")

	def __init__(self, height, width, Backgroundcolor: tuple):
		self.height = height
		self.width = width
		self.Backgroundcolor = Backgroundcolor
		self.window = pygame.display.set_mode((self.height, self.width))
		self.window.fill(self.Backgroundcolor)
		self.run = True
	def draw(self):
		# 
		pygame.draw.line(self.window, (0, 0, 0), (0, self.height/2), (self.width, self.height/2)) # x
		pygame.draw.line(self.window, (0, 0, 0), (self.width/2, 0), (self.width/2, self.height)) # y
		# for i in range(100):
		# 	pygame.draw.circle(self.window, (0, 0, 100), (self.width/2, -1 * (i)), 3) 
		# for i in range(100):
		# 	pygame.draw.circle(self.window, (0, 0, 100), (i/30, self.height/2), 3)
		pygame.display.update()
	def run_(self):
		self.clock.tick(30)
		while self.run:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.run = False
			pygame.display.update()
			self.draw()
		pygame.quit()
	@property
	def origin(self):
		return {
		'x': self.width/2,
		'y': self.height/2,
		}
	def PlotF(self, Func, Percision, ZOOM=1):
		ZOOM *= 30
		self.O = self.origin
		for i in [i*Percision for i in range(-1000000, 1000000)]:
			try:
				pygame.draw.circle(self.window, (150, 0, 0), ((self.O['x'] + i*ZOOM), (self.O['y'] + (Func(i)*-1)*ZOOM)), 1)
			except Exception as e:
				pass
	def plot(self, x_axis: list, y_axis: list, ZOOM=1):
		data = zip(x_axis, y_axis)
		ZOOM *= 30
		self.O = self.origin
		for x, y in data:
				pygame.draw.circle(self.window, (0, 0, 0), ((self.O['x'] + x *ZOOM), (self.O['y'] + y*ZOOM)), 5)
def Function(x):
	return x**2

def division(x):
	return 1/sin(x)

def Euler(x):
	return x**e




graph = Graph(700, 700, (255, 255, 255))
# graph.PlotF(division, .001, .1)
graph.plot([i for i in range(10)], [i*.10 for i in range(10)])
graph.run_()


# from time import sleep
# for i in range(40):
# 	print(i + 100,cos(i)*100)
# 	sleep(1)