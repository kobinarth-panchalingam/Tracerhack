while True:
    word = input()
    if word.lower() != 'bye':
        l = len(word)
        max = 0
        pali = None
        for i in range(0,l-2):
            a = word[i]
            n = word.count(a,i,l)
            end = l
            for j in range(n-1):
                x = word.rfind(a,i,end)+1
                word2 = word[i:x]
                if word2 == word2[::-1] and len(word2)> max:
                    pali = word2
                    max = len(word2)
                    break
                end = x-1
        if pali:
            print(pali)
        else:
            print('There are no palindromes')
    else:
        print('Bye!')
        break
