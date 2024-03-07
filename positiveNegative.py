# create a program that takes in user input and determine if its positive or negative or zero
# print "yournumber is positive" or "your number is negative"
# objectives
# if else:
# print()
# input()

# get user input

# break down the problem
# 1. take in user input
    # check the type of input
    # if the type of input is string how do you convert it to an int?
# 2. check if the number is positive or negative or zero
    # need to use if else statement
    # you will be comparing int not str
# 3. print the result

userinput = input()
userinputtype = type(userinput)
print(userinputtype)

userinputnumber = float(userinput)
print(type(userinputnumber))

if userinputnumber > 0:
    print("your number is positive", userinputtype)

elif userinputnumber < 0:
    print("your number is negative", userinputtype)

elif userinputnumber == 0:
    print("your number is zero",userinputtype)