# a = int(input())
# b = int(input())
a = 1
b = 10
l = []
delimiter = ''
for i in range(a, b + 1):
    if i % 3 == 0:
        l.append(i)
print(sum(l) / len(l))
