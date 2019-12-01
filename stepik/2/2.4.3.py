#s = input()
s = 'aaaabbcaa'
r = ''
word = ''
for symbol in s:
    if len(word) == 0 or word[:1] == symbol:
        word += symbol
    else:
        r += word[:1] + str(len(word))
        word = symbol
r += word[:1] + str(len(word))
print(r)
