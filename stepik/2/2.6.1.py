l = []
while len(l) == 0 or sum(l) != 0:
    l.append(int(input()))
print(sum(list(map(lambda x: x ** 2, l))))
