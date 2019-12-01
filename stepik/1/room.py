roomType = input()

a = int(input())
s = 0
if roomType == 'круг':
    s = 3.14 * a ** 2
elif roomType == 'прямоугольник':
    b = int(input())
    s = a * b
elif roomType == 'треугольник':
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print(s)
