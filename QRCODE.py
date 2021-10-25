from qrcode import make
from dataclasses import dataclass

class _Qrmaker:
	
	def __init__(self, content, ext: str = 'PNG', output:str = 'Output.png'):
		self.content = content
		self.ext = ext
		self.output = output
		try:
			self.img = make(self.content)
			self.img.save(self.output, self.ext)
		except:
			print('something went wrong')