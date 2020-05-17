

def get_input_data():
    return {
        'encoding_alphabet': input().strip(),
        'decoding_alphabet': input().strip(),
        'message1': input().strip(),
        'message2': input().strip()
    }


def get_data():
    return {
        'encoding_alphabet': 'abcd',
        'decoding_alphabet': '*d%#',
        'message1': 'abacabadaba',
        'message2': '#*%*d*%'
    }


def my_encode(raw_string, dictionary):
    lst = list(raw_string)
    for i, s in enumerate(lst):
        if s in dictionary:
            lst[i] = dictionary[s]
    return ''.join(lst)


def main():
    d = get_data()
    d['enc_dict'] = dict(zip(d['encoding_alphabet'], d['decoding_alphabet']))
    d['dec_dict'] = dict(zip(d['decoding_alphabet'], d['encoding_alphabet']))

    s1 = my_encode(d['message1'], d['enc_dict'])
    s2 = my_encode(d['message2'], d['dec_dict'])
    print(s1)
    print(s2)


main()
