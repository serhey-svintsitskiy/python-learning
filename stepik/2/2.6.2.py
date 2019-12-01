x = int(input())
'''calculate discriminant'''
D = 1 + 8 * x
'''calculate minimal number which will be printed n times'''
n = int(((D ** 0.5) - 1) // 2)
'''calculate count times for last number '''
f = int(x - n * (n + 1) / 2)
l = []
for i in range(n + 1):
    l.append(' '.join([str(i)] * i))
l.append(' '.join([str(n + 1)] * f))
print(' '.join(l))
