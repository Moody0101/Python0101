print("rules : ")
print("- every answer should be in capital lette ")
print("- for every correct answer you get 10 points ")
print("- in order to win you gotta hae more than 70 point ")
points = 0
point = 0
rd = fx = 10  # made to collect points
guess_count = 0
guess_limit = 2  # THAT VARIABLE IS MADE TO limitize THE NUMBER OF GUESSES THAT THE PLAYER HAVE
out_of_guesses = False
A = "BLACK"
guess = input(" what is my favourite color : ")
while guess != A and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input(" wrong : ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses and guess != A:
    point = points
else:
    point = fx + points
B = ["LIL PEEP", "POLO G"]

guess = input(" WHAT IS MY FAVORITE ARTIST  : ")
guess_count = 0
guess_limit = 2
out_of_guesses = False
points = int(0)
while guess not in B and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input(" it is incorrect try again : ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses and guess not in B:
    point = fx + points
else:
    rd = 10
    point = fx + points + rd
c = "COMETHAZINE"
guess = input(" what is my second favorite artist : ")
guess_count = 0
guess_limit = 2
out_of_guesses = False
points = int(0)
while guess != c and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input(" it is incorrect try again : ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses and guess != c:
    point = fx + points + rd
else:
    point = fx + points + rd + fx
D = "BLACK METAL"
guess = input(" what is my favorite metal genre : ")
guess_count = 0
guess_limit = 2
out_of_guesses = False
points = int(0)
while guess != D and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input(" it is incorrect try again : ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses and guess != D:
    point = fx + points + rd + fx
else:
    point = fx + points + rd + fx + rd
F = "NO"
guess = input(" do I like being around girls : ")
guess_count = 0
guess_limit = 2
out_of_guesses = False
points = int(0)
while guess != F and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input(" it is incorrect try again : ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses and guess != F:
    point = fx + points + rd + fx + rd
else:
    point = fx + points + rd + fx + rd + fx
G = "COFFE"
guess = input(" what is my favorite drink : ")
guess_count = 0
guess_limit = 2
out_of_guesses = False
points = int(0)
while guess != G and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input(" it is incorrect try again : ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses and guess != G:
    point = fx + points + rd + fx + rd + fx
else:
    point = fx + points + rd + fx + rd + fx + rd
H = "MINECRAFT"
guess = input(" WHAT IS MY FAVORITE GAME : ")
guess_count = 0
guess_limit = 2
out_of_guesses = False
points = int(0)
while guess != H and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input(" it is incorrect try again : ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses and guess != H:
    point = fx + points + rd + fx + rd + fx + rd
else:
    point = fx + points + rd + fx + rd + fx + rd + fx
w = "NARUTO"
guess = input(" what is my favorite anime : ")
guess_count = 0
guess_limit = 2
out_of_guesses = False
points = int(0)
while guess != w and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input(" it is incorrect try again : ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses and guess != w:
    point = fx + points + rd + fx + rd + fx + rd + fx
else:
    point = fx + points + rd + fx + rd + fx + rd + fx + rd
k = "29/9"
guess = input(" when is my bd : ")
guess_count = 0
guess_limit = 2
out_of_guesses = False
points = int(0)
while guess != k and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input(" it is incorrect try again : ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses and guess != k:
    point = fx + points + rd + fx + rd + fx + rd + fx + rd
else:
    point = fx + points + rd + fx + rd + fx + rd + fx + rd + fx

Q = "PEWDIEPIE"
guess = input(" what is my favorite youtuber 'gamer' : ")
guess_count = 0
guess_limit = 2
out_of_guesses = False
points = int(0)
while guess != Q and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input(" it is incorrect try again : ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses and guess != Q:
    point = fx + points + rd + fx + rd + fx + rd + fx + rd + fx
else:
    point = fx + points + rd + fx + rd + fx + rd + fx + rd + fx + rd
    print("you have " + str(int(point)) + " points")
if point < 60:
    print("you lose , you dont know me that much ")
elif point == 0:
    print("fuck you")

else:
    print("ohh boi or girl I love you")
FUEL = input("bye")