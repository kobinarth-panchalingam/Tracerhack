word = input()  #input
a = 0
vow = 'aeiouAEIOU'
result = ''

if len(word) <= 200:
    while a < len(word) :
        x = word[a]
        if x.isalpha() and x not in vow and a+2 < len(word):
            y, z = word[a+1], word[a+2]
            if x.lower() == z and y == 'o':
                result += x
                a += 3
            else:
                print('Input can not be decoded')
                break
        else:
            result += x
            a += 1
    else:
        print(result)
else:
    print('length of string exceeded the maximum limit')
