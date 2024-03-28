# read input.txt and file and put it to an array
with open("input.txt") as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]    #python list comprehension

print(len(lines))
print(lines(1))
print(lines(2))
print(lines(3))

# solve using just if else and for loops
