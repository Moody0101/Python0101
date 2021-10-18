

"""
lib description:
	Email => we only imported the EmailMessage to handle our whole email message with any messy code
	smtplib => the lib that helps us login to our email server example: gmail, hotmail, yahoo....
	os => commands and system stuff handler.
	

"""


from email.message import EmailMessage
from os import environ 
import smtplib
# from multiprocessing import prp

# if you wanna set your credentials in your machine go to the env variables 
# so the script can grab them and keeps  them secure 

class MessageSettingError(Exception):
	pass

DEBUG_MODE = {
	'port': 1025,
	'server': "localhost:1025"
}

EMAIL_ADRESS = environ.get("EMAIL")
PASSWORD = environ.get("PASSWORD")

class EmailSender:
	"""
	note: if debug=True then you should go type this command before running the script to
	debug:
	python -m smtpd -c DebuggingServer -n localhost:1025
	if you change the port in the command then you should change it in your script too.

	"""
	def __init__(self, 
		address,
		password,
		msg: EmailMessage = EmailMessage(), PORT: int = 456,
		agent: str = 'smtp.gmail.com', 
		Debug: bool = False
		) -> None:

		self.address = address
		self.password = password
		self.PORT = PORT
		self.msg = msg
		self.agent = agent

		if Debug == False:
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
	""")		elif self.msg['To'] is None || is None self.msg['Subject']:
					print("check your setMessage() functions seems like you have not set important headers")
				else:
					raise messageSettingError("you have forgotten to set some important data in the setMessage function")
			 # Message was sent
		return False # message was Not sent
# test



def test():
	email = EmailSender(EMAIL_ADRESS, PASSWORD,Debug=True) # constructing the instance, you can change the PORT and the agent tho
	print(email)
	email.setMessage('Hello', 'Mohamed@gmail.com', 'I just wanted to check on you')
	print(email)
	
	
	

if __name__ == '__main__':
	test()