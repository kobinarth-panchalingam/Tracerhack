word = input()
vowels = 'aeiouAEIOU'
for i in set(word):
    if i not in vowels and i.isalpha():
        x = i+'o'+i.lower()
        word = word.replace(i,x)
print('Output (Encoded):',word)
        
