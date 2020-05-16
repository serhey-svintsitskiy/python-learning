def get_input_data():
    inpdata = []
    c = int(input())
    for i in range(0, c):
        raw = input().split(';')
        inpdata.append({
            'team1': raw[0],
            'team2': raw[2],
            'count1': int(raw[1]),
            'count2': int(raw[3])
        })
    return inpdata


def get_data():
    return [
        {'team1': 'Локомотив', 'team2': 'Зенит', 'count1': 12, 'count2': 3},
        {'team1': 'Спартак', 'team2': 'Зенит', 'count1': 9, 'count2': 10},
        {'team1': 'Спартак', 'team2': 'Локомотив', 'count1': 8, 'count2': 15}
    ]


def new_res():
    return {'games': 0, 'wins': 0, 'dead': 0, 'fails': 0, 'total': 0}


def calc(data):
    r = {}

    for el in data:
        team1 = el['team1']
        team2 = el['team2']
        count1 = el['count1']
        count2 = el['count2']

        if team1 not in r:
            r[team1] = new_res()
        if team2 not in r:
            r[team2] = new_res()

        r[team1]['games'] = r[team1]['games'] + 1
        r[team2]['games'] = r[team2]['games'] + 1

        if count1 > count2:
            r[team1]['wins'] = r[team1]['wins'] + 1
            r[team2]['fails'] = r[team2]['fails'] + 1
            r[team1]['total'] = r[team1]['total'] + 3
        elif count2 > count1:
            r[team2]['wins'] = r[team2]['wins'] + 1
            r[team1]['fails'] = r[team1]['fails'] + 1
            r[team2]['total'] = r[team2]['total'] + 3
        else:
            r[team2]['dead'] = r[team2]['dead'] + 1
            r[team1]['dead'] = r[team1]['dead'] + 1
            r[team1]['total'] = r[team1]['total'] + 1
            r[team2]['total'] = r[team2]['total'] + 1
    return r


def print_res(res):
    for i in res:
        print(
            i +
            ':' +
            str(res[i]['games']) +
            ' ' +
            str(res[i]['wins']) +
            ' ' +
            str(res[i]['dead']) +
            ' ' +
            str(res[i]['fails']) +
            ' ' +
            str(res[i]['total'])
        )


def start():
    data = get_input_data()
    r = calc(data)
    print_res(r)


start()
