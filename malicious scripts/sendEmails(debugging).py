
import smtplib
from os import environ 
EMAIL_ADRESS = environ.get("EMAIL")
PASSWORD = environ.get("PASSWORD")

# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
with smtplib.SMTP('localhost', 1025) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.ehlo()
	smtp.login(EMAIL_ADRESS, PASSWORD)
	subj = 'Hello'
	body = " How are you !"
	msg = f'subject: {subj}\n\n{body}'
	smtp.sendmail(EMAIL_ADRESS, 'azmoudh@gmail.com', msg)	
	print('sent!!')

