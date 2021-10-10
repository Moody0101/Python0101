class account:
    def __init__(self, email_or_number, username, password):
        self.email_or_number = email_or_number
        self.username = username
        self.password = password

    def display_account_info(self):
        print(" you email is  :  " + self.email_or_number + "\n"
              + " your username is : " + self.username
              + "\n" + "your password is : " + self.password)
info = input("which account : ")
gmail = account("azmoudh@gmail.com", "hossin_azmoud", "azmoudhm2")
facebook = account("0621484074", "coma_sama", "XXX_123_kitten")
if info == gmail:
    gmail.display_account_info()
    hf = input()
elif info == facebook:
    facebook.display_account_info()
    hf = input()
else:
    gmail.display_account_info()
    facebook.display_account_info()
    hf = input()

