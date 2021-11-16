from math import pi, sin, radians
from numpy import array
import numpy
import math

PI = 90

angels = [i*90 for i in range(10)]
print(angels)
def main():
	sinVals = array([sin(radians(i)) for i in angels])
	# print(sinVals[6])
	x_axis = array([i for i in range(10)])
	print([(x,y) for x,y in zip(x_axis, sinVals)])

if __name__ == '__main__':
	main()
	print(sin(180))