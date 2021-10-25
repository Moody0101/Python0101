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
	letters = [i for i in materials['digits'] + materials['ascii_letters'] + materials['punctuation']]
	table = {}
	for _ in letters:
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
		print(f"{i} was Not fount")
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
			edata.append(str(ord(_) + int(self.seed[i])))
		self.storeseed(key=edata)
		return ''.join(edata)
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
		data = dumps({'seed': self.seed, 'key':key}, indent=4)
		with open('seeds.json', "w+") as db:
			db.write(data)
			return 0
		return 1

text: str = """
    This module scraps all the company names from a website called clutch.co (it is a website
    for findind jobs) then generates all the possible valid emails, then puts everything in a csv file
code proto:
    funcList = [scrap, scrapPages, extractAllcompanyNames, EmailGenerator]
    => we have here three funcs, each function serves some purpose.
    scrap: - takes a url then returns the content of the web page.
           - serves scrapPages with the content to scrap every page.
    scrapPages: - uses scrap() to get data from multiple pages.
                - returns a list containing the data from each pages 
                - takes n, the pages number => {the number of pages to be scrapped}
                - takes firtOne, the first page so it can go to other pages easily.
    extractAllcompanyNames: flattens the 2D array that gets returned from scrapPages()
    EmailGenerator: takes the output of extractAllcompanyNames then generates possible valid emails
    using 
    Hierarchy:
    scrap() => scrapPages() => extractAllcompanyNames() => EmailGenerator()
    content => <= pagesNumber | 2D list => 1D list => EmailList

class prototype:
    # I do this every time I will make a class for design purpose
    constructure = {
        urlFirstPages: str = {url}?page=;
        PagesCount: int = 1;
        EmailPrefixes: list[str] = [];
        CompanyNames: list[str] = []
        Emails: list[str] = []
        }
note: clutch is using captcha, so m pretty much fucked up, so.. but I will try another sulotion.
""" 

def test():
	data = crypt() 
	data00 = data.decrypt_00()
	print(data00)
test()
