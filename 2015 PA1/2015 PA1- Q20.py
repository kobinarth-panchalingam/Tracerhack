alpha = 'abcdefghijklmnopqrstuvwxyz'
word = input('Enter the input word: ').lower()                  #taking input

if word.isalpha() == False:                                     #checking all the characters are alphabets
    print('Enter a word with alphabets only')
    
elif len(word)<3:  
    print('Cannot be balanced!')                                #minimum length of word is 3 is needed in balancing
    
else:
    a = False
    
    for i in range (1,len(word)):                               #a word can not be balanced at its first letter 
        print(i)
        left_weight = 0
        right_weight = 0
        bal_letter = word[i]
        print(left_weight)
        for j in range(0,i):
            left_weight += (i-j)*(alpha.index(word[j])+1)       #(i-j) - position of letter from its balance letter, (alpha.index(word[j])+1) - weight of letter
            print((i-j)*(alpha.index(word[j])+1))
            
        for k in range(i+1,len(word)):
            right_weight += (k-i)*(alpha.index(word[k])+1)      #(k-i) - position of letter from its balance letter, (alpha.index(word[k])+1) - weight of letter

        if left_weight == right_weight:
            print(left_weight,right_weight)
            print('Balance point letter: %s, weight = %s'%(bal_letter,left_weight)) 
            a = True
    if a == False:
        print('Cannot be balanced!')

    
