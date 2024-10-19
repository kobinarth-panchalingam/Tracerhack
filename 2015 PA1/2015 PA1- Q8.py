#Input from user
word_1 = input('Enter word 1: ').lower() #input 1
word_2 = input('Enter word 2: ').lower() #input 2
word_3 = input('Enter word 3: ').lower() #input 3

#Checking whether the both words present in word 3
if word_1 in word_3 and word_2 in word_3:
    print('Output: NOT A SHUFFLE')
#Checking the first criteria
else:
    start = 0
    for i in word_1:
            a = word_3.find(i,start)
            if a == -1: 
                break
            else:
                start = a+1 #to check whether the words are in order
    
    start = 0
    for x in word_1:
            b = word_3.find(x,start)
            if b == -1:
                break
            else:
                start = b+1 #to check whether the words are in order

    if a>-1 and b>-1:
        print('Output: SHUFFLE')
