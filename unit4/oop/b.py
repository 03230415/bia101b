input_str = '((())())()(((((()()(()())())(()((((((((()))()(())(()())((()))())(((()())))()))(((()))()())()((()(())))((())())())()))))(((())()))()(()((()))(())()())))()()())(()(())))()))((())())()(((()()()()(()(()(((())((((()))))))(())((()(()())())()(())))()()(((((()))))(()))()))(())())))((()))((())))()))()))()(()(()))(()()())(()((((()())((()((()(()))))(()))())((())(((()()()))((((((()()()(()(())(()()()))()()()((((((())()))())()())()))()(())()())(()())()((()))()))))((((())))))())(())((((())))())((())()))(()))())))((())))()))))))((())(())))((())))(())))(())()(()()))(((())()((()()(((()))((()(()))()))))))()))))(()()(((()()((((((())()))()(((((((())())))()()((()))())())(((()(())()((((((())))))))()))))(())((((()((()()(()(())))()((((((())(()))(()))))((()(((()))()))))))(((((())()))(((((((()(()()((()))(())((()())((((()(((()))((()(()))))())())))())())(()))))(())(((())))())))((()(()(((((())))()())()()(((()()))()(()(((((())(())(())))(()())()(()))()((()())))()))())())(()(())()))())(())))(((((()())))()(()))(()()(()(()'
s = input_str
num1 = 0
for i in s:
    if i == '(':
        num1 += 1
    elif i == ')':
        num1 -= 1
print("the final floor is", num1)
print("=====")

