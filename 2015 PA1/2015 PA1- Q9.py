str1 = input().replace(' ','')
str2 = input().replace(' ','')
if str1.isalpha() and str2.isalpha():
    if len(str1) == len(str2):
        for i in set(str1):
            i = i.lower()
            x = str1.count(i) + str1.count(i.upper())
            y = str2.count(i) + str2.count(i.upper())
            if x == y:
                continue
            else:
                print('These are not anagrams')
                break
        else:
            print('These are anagrams')
    else:
        print('These are not anagrams')
else:
    print('Only alphabetical characters are allowed in a word')
