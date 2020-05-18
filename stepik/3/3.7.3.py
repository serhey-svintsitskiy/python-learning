def checktext(text, dictionary):
    errors = []
    for ln in text:
        for w in ln.lower().split():
            if w not in dictionary and w not in errors:
                errors.append(w)
    return errors


def getdata():
    d = {'dict': [], 'text': []}
    for i in range(0, int(input())):
        d['dict'].append(input().strip().lower())
    for i in range(0, int(input())):
        d['text'].append(input().strip().lower())
    return d
    # return {
    #     'dict': ['champions', 'we', 'are', 'stepik'],
    #     'text': ['We are the champignons', 'We Are The Champions', 'stepic']
    # }


def outputres(res):
    for ln in res:
        print(ln)


def main():
    data = getdata()
    res = checktext(data['text'], data['dict'])
    outputres(res)


main()
