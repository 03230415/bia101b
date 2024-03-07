# ! check if user can vote
# get user age from input
userinput = input("please type your age: ")

# ! convert user input to number
userAge = int(userinput)

# ifelse statement to check if they can vote
if userAge >= 18:
    print("can vote")
else:
    print("cannot vote")