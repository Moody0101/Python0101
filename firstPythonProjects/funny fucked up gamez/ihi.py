class user:
    def __init__(self, email, passkey):
        self.email = email
        self.passkey = passkey


user1 = user("email@gmail.com", "hashadm2")
print(user1.passkey)
print(user1.email)
