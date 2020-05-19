def parse_user(dataline):
    return {
        'class': int(dataline[0]),
        'name': dataline[1],
        'length': int(dataline[2]),
    }


def get_input_data():
    d = {}
    with open('3.7.5.txt', 'r') as inf:
        for line in inf:
            u = parse_user(line.strip().split())
            if u['class'] not in d:
                d[u['class']] = []
            d[u['class']].append(u)
    return d


def calc(dlist):
    res = {}
    for i in dlist:
        sum = 0
        for item in dlist[i]:
            sum = sum + item['length']
        res[i] = sum / len(dlist[i])
    return res


def output_data(data):
    for i in range(1, 12):
        if i not in data:
            print(str(i) + " -")
        else:
            print(str(i) + " " + str(data[i]))

data = calc(get_input_data())
output_data(data)
