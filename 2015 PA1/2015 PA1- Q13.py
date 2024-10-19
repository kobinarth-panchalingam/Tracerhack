try:
    N = int(input('Number dosplayed N: '))  #Taking input
    N = str(N)
except ValueError:
    print('Input an integer')
else:
    if not(3<=len(str(N))<=16) :            #Checking the number of digits is in the correct range
        print('length of number should be in the range of 3 and 16')
    else:
        num = []
        for i in range(len(N)-1,0,-1):
            if int(N[:i])%4 == 0:
                num.append(N[:i])
        print('Possible prefixes: ',','.join(num))  #Printing output
 
