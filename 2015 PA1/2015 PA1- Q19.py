word = input('Enter the input word: ').lower() #input
if word.isalpha():
    n = len(word)
    degree = 0
    for i in range(n-1,0,-2):
        if word[0:i] == word[n-i:n]:
            degree = i
            break
    print(degree)
else:
    print('Input must contain only alphabets')
