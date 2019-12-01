# n = int(input())
for n in range(100):
    if n > 99:
        nm = n % 100
    else:
        nm = n
    # elif 10 <= n < 20:
    #     nm = 9
    # else:
    #     nm = n

    if 10 <= nm <= 20:
        nm = 9
    elif nm > 20:
        nm = nm % 10

    plural = 'программист'
    if 5 <= nm <= 9 or nm == 0:
        plural = 'программистов'
    elif 2 <= nm <= 4:
        plural = 'программиста'

    print(str(n) + ' ' + plural)
