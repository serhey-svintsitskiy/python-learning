def get_input_data():
    data = []
    for i in range(0, int(input())):
        raw = input().strip().split()
        data.append(create_vector([raw[0], int(raw[1])]))
    return data


def multiply_vector(vector, value):
    return [vector[0] * value, vector[1] * value]


def sum_vectors(vectors_list):
    res_vector = [0, 0]
    for vector in vectors_list:
        res_vector = [res_vector[0] + vector[0], res_vector[1] + vector[1]]
    return res_vector


def create_vector(vdata):
    vectors = {'север': [0, 1], 'восток': [1, 0], 'юг': [0, -1], 'запад': [-1, 0]}
    if vdata[0] in vectors:
        return multiply_vector(vectors[vdata[0]], vdata[1])
    else:
        return [0, 0]


def main():
    data = get_input_data()
    print(' '.join(map(str, sum_vectors(data))))


main()
