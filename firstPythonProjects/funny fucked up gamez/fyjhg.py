try:
    x = 10/0
    number = int(input("enter a number"))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")
#with try except you can  catch any error and avoid breaking the whole program#
