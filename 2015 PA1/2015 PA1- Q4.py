original_string = input('Enter the input: ')        #taking input from user
original_string = original_string.replace(' ','')   #removing spaces
vowels = 'aeiou'
Disemvoweled_string = ''
rem_vowels = ''
if original_string.isalpha()== False:               #checking whether the input contains only alphabes
    print('Input a string with only alphabets')
else:
    for i in original_string:
        if i.lower() in vowels:
            rem_vowels += i
        else:
            Disemvoweled_string += i
    print('Disemvoweled string: ',Disemvoweled_string)
    print('Removed vowels: ',rem_vowels)
                    
