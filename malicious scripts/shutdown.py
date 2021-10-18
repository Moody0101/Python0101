"""
a script that shuts down the computer if it was run.... 
"""
from os import system


def shutdown():
	system("shutdown /s /t 1")

