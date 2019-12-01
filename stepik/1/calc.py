# put your python code here


a = float(input())
b = float(input())
op = input()
res = ''

if op == '+':
    res = a + b
elif op == '-':
    res = a - b
elif op == '*':
    res = a * b
elif op == 'pow':
    res = a ** b
elif op == '/' or op == 'mod' or op == 'div':
    if b == 0:
        res = 'Деление на 0!'
    elif op == '/':
        res = a / b
    elif op == 'mod':
        res = a % b
    elif op == 'div':
        res = a // b

print(res)

