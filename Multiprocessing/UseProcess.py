"""
Using Multiple processes in python
"""

from multiprocessing import Pool


def main():

	def f(x):
	    return x*x
	
	with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
	
if __name__ = "__main__":
	main()