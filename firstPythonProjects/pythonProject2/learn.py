name = input("enter you name : ")
age = int(input("enter your age : "))
email = input("enter your email : ")
password = input("enter you password : ")
code = "hashadm2"
em = "ahbex@gmail.com"
count = 0
guess_limit = 3
while em != email:
    email = input(" enter email is wrong : ")
    count += 1
    if count == guess_limit:
        print("baraka 3lik")
    else:
       while password != code:
           print(" the password is wrong! ")
           password = input("enter password : ")
       else:
         print("hello " + name + str("!"))
         print("are you really " + str(int(age)) + str(" !, you look younger"))
         print("welcome to your account! sir")

