
c = 5
d = 10
a = 1
b = 4

c = int(input())
d = int(input())
a = int(input())
b = int(input())

b += 1
d += 1

print('\t', end='')
for i in range(a, b):
    print(i, end='')
    print('\t', end='')
print()

for j in range(c, d):
    print(j, end='\t')
    for i in range(a, b):
        print(i * j, end='')
        print('\t', end='')
    print()
