code: str = "hashadm2"
fr = "azmoudh@gmail.com"
email = input("enter email : ")
password = input("enter password : ")
guess_count = 0
guess_limit = 4
out_of_guess = False
while not out_of_guess:
    if fr != email and code == password or fr == email and code != password and not out_of_guess:
        # if the email is wrong :
        print("the password does not match the email! \n  try again : ")
        email = input(" enter email : ")
        password = input(" enter password : ")
        guess_count += 1
    elif fr != email and code != password and not out_of_guess:
        # if both are false :
        print("the password and the email are false try again")
        email = input("enter email : ")
        password = input("enter password : ")
        guess_count += 1
    elif guess_count > guess_limit:
        out_of_guess = True
        print("you are out of guesses")

    elif email == fr and password == code and out_of_guess:
        # if the password and the email are correct:
        age = int(input(" age  : "))
        phone = input(" enter you phone number : ")
        full_name = input(" enter your full name : ")
        city = input("city : ")
        print("age " + ":" + str(age) + "\n" + "phone " + ":" + str(phone) + "\n"
              + "name " + ":" + str(full_name) + "\n"
              + "city" + " : " + str(city)
              )
        print("welcome to your account!")