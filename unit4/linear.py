# searching
# sorting

# !problem 1
# input
user_input = [1,2,3,4,5,6,7,8,9,11]
#?Q: check it to see if a certain number exist in the user input array
n = 14 


# if else, for loops, print, calculations(+,-)
# we can make use of if else if we want to find if one element is same to another

#######
# for loop
print("before")
for e in user_input:   #will go through each element
    if e == n:
        print("found")
print("after")
print ("not found")

for e in user_input:
    if e == n:
        print("found")
    else:
        print("not found")     #this will print many output

result = False
for e in user_input:
    if e == n:
        result == True
if result == True:
    print("found")
else:
    print("not found")

# time = O(n)
input = [1,2,3,4]
for i in input:
    print("hi")    #O(n)
    if i == 1:    #O(1) because this will run only once
        break

# O(n) * O(n)
for s in input:
    for k in input:
        print("-----")

  