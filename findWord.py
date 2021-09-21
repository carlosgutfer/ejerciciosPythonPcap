import sys

text1 = input('Write your object word: ')
text2 = input('Write your target prhase: ')

if text1[0] in text2:
    x = text1.find(text1[0])
    for letter in text1:
        if   text2.find(letter, x) == -1:
            print('NO')
            sys.exit()
            break
        else:
            x = text2.find(letter, x)
    print('YES')
else:
    print('NO')
        