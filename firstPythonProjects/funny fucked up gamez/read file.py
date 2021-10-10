answers = open("file.txt", "r") # storing the file in a variable # "r" is refering to readable, if yo wanna write another file "w' and if yoou and if u wanna add something write "a"
print(answers.readline()) # this readline() is allowing us to ead just one line of code but readlines() is allowing us to read the whole lines of the code
#answers.close() #this close() allows us to close the file
# if we want to read a particular line we need just to instead of writing readline() we write readline() followed by the index which is the position of the line exmple readline()[]
# using it with a for loop
for goom in answers.readlines():
    print(goom)
    #how easy
answers.close()
g = open("fileSDS.txt", "w")# adding a file procces
g.write("user {"
        "password: masogi"
        "email: xxxtentacion"
        "}")
