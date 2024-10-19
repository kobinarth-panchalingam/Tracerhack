word  = input('Enter a word: ').lower()     #taking inputs
if word.isalpha() == False:         #checking whether the input contains only alphabets
    print('Input a word with only alphabets')
elif len(word) == 1:
    print('No order for single character')
else:
    def check_order(input):     #function for checking the letters are in alphabetical order
        i = 0
        while i < len(input)-1:
            if ord(input[i]) <= ord(input[i+1]):
                i = i + 1
                x = True
            else:
                x = False
                break
        if x == True:
            return True

    rev_word = word[::-1]
    if check_order(word) == True:
        print('Output: %s IN ORDER'%(word))
    elif check_order(rev_word) == True:
        print('Output: %s IN RIVERSE ORDER'%(word))
    else:
        print('Output: %s NOT IN ORDER'%(word))
