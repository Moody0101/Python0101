from string import *
from dataclasses import dataclass
from typing import Union
from datetime import datetime
from json import dumps, loads
materials = {
			'digits': digits,
			'ascii_letters': ascii_letters,
			'punctuation': punctuation
}

def makeasciitable():
	"""
	function to make me an ascii table using the ord() built-in function.
	be cause obviously I don't want to memorize.
	"""
	table = {}
	for _ in materials['ascii_letters']:
		table[ord(_)] = _
	with open("ascii.json", "w+") as f:
		f.write(dumps(table, indent=4))
	

def tochar(i):
	"""
	uses the prev function's output to convert an int to a char
	prints not found and exists the whole program so you must be careful
	"""
	try:
		return loads(open("ascii.json", "r").read())[str(i)]
	except Exception as e:
		print("Not fount")
		exit()
class crypt:
	"""a class to encrypt and decrypt data using string manipulation."""
	
	def __init__(self, data: Union[str, int] = None, seed: int =None):
		self.data = data
		self.seed = seed
		self.setup()
	def __repr__(self):
		return '<encrypted data/>'
	def __str__(self):
		return 'encrypted data'
	def crypt_00(self):
		data = self.data
		edata = []
		i = 0
		for _ in data:
			if i > len(data):
				i = 0
			edata.append(str(int(ord(_)) + int(self.seed[i])))
		self.storeseed(key=edata)
		return edata
	def decrypt_00(self):
		
		seed, key = str(loads(open("seeds.json", "r").read())['seed']), loads(open("seeds.json", "r").read())['key']
		res = ''
		j = 0
		for i in key:
			if  j > len(key):
				j = 0
			res += tochar(int(i) - int(seed[j]))
		return res
	 	
	@property
	def getseed(self):
		return (self.seed, self.seedlength)
	def setup(self):
		if not self.seed:
			self.seed = str(datetime.now())[-6:]
		if isinstance(self.seed, int):
			self.seed = str(self.seed)
		if isinstance(self.data, int):
			self.data = str(self.data)
		self.seedlength = len(self.seed)
	def storeseed(self, key):
		data = dumps({'seed': self.seed, 'key':key})
		with open('seeds.json', "w+") as db:
			db.write(data)
			return 0
		return 1

# firstly tried to encrypt my name 
data = crypt("hossin") 
# it returns a seed: 239126 and
# an array of numbers [the key], that can be  used to retrieve the data
# which uses the to retreive the using the decrypt_00 function 

data00 = data.decrypt_00()

#Now let's use a text.

with open("dataStrcuctues.py", "r") as f:
	print([i for i in f.readlines()])
	#encrypting the file
	data2 = encrypt()