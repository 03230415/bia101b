                                            # #calculator application
                                            # #variables and if statement

                                            # #STEPS
                                            # #1. get input from the user
                                            # #2. do calculation based on user input
                                            # #3. give output to the user
# 1
print("above user input.....")
userInput = ""

print("above whatUserTyped")
whatUserTyped = input()

print("you typed", whatUserTyped)

#print("you typed:")
#print(whatUserTyped)
print("done with the program")


print('* for multipliocation')
print('+ for addition')
print('- for subtraction')
print('/ for division')

whatUserTyped = input()

print('User typed:', whatUserTyped)
print('user input-type', type(whatUserTyped))

print("================")
if whatUserTyped == "+":
    print("doing addition")
print("doing more addition")

if whatUserTyped == "-":
    print("doing subtraction")
    print("doing more subtraction")

                                                        # the outout will be
                                                        # -
                                                        # User typed: -
                                                        # user input-type <class 'str'>
                                                        # ================
                                                        # doing more addition
                                                        # doing subtraction
                                                        # doing more subtraction
                                                        # because of the indentations 
                                                        # print("doing more addtion") will be run by print("=========")


# Objective: a calculator application made using 
# variables and if statements

# STEPS
# 1. get input from user --> DONE

# 2. do calculation based on user input
# 2.1 check what string did user typed
# 2.2 if usser string == * then do multiplicatio and so on

# 3. give output to the user

print('* for multipliocation')
print('+ for addition')
print('- for subtraction')
print('/ for division')

whatUserTyped = input()

print('User typed:', whatUserTyped)
print('user input-type', type(whatUserTyped))

print('-------------------')
if whatUserTyped == "+":
    print('Doing Addition')
    if 'a' == 'b':
        print('a is not b')
    if 'b' == 'b':
        print('b is b')

print('doing more addition')

if whatUserTyped == "-":
    print('Doing Subtraction')
    print('doing more subtraction')