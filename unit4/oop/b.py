input_str = '((())))(()(())())(()())))))((()())()))()()())())(())(()(())(())()(((()()(((((()(((()))()(()(())()))(((('
s = input_str
num1 = 0
for i in (s):
    if i == '(':
        num1 += 1

    if i == ')':
        num1 = num1 - 1
    print(num1) 
    print("======")


