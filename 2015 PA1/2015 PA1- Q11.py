while True:
    try:
        n = int(input()) #input
        if (1<=n<=20):   # checking whether input is in correct range
            odds = []
            x = int((n*(n-1))/2+1)
            for i in range(x,x+n):
                odd = int(2*i-1)
                odds.append(str(odd))
            print('Odd number Sequence: ',' + '.join(odds))
        elif n == -1:    #Finishing point
            print('Bye!')
            break
        else:
            print('n is out of range')
    except ValueError: #handling invalid inputs
        print('Invalid Input')
