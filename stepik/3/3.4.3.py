def parse_user(user_data):
    l = user_data.split(';')
    return {'name': l[0], 'math': int(l[1]), 'phys': int(l[2]), 'lang': int(l[3])}

def calc(user_list):
    res = []
    m = 0
    p = 0
    l = 0
    c = 0
    for u in user_list:
        c += 1
        m += u['math']
        p += u['phys']
        l += u['lang']
        res.append((u['math'] + u['phys'] + u['lang']) / 3)
    res.append(str(m / c) + ' ' + str(p / c) + ' ' + str(l / c))
    return res


l = []
with open('3.4.3.txt', 'r') as inf:
    for line in inf:
        l.append(parse_user(line.strip()))

for r in calc(l):
    print(r)
