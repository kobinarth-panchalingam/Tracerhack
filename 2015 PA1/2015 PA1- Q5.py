try:
    N = int(input('Enter the input: ')) #taking input from user
except ValueError:
    print('Enter an integer')
else:
    if not(1<=N<=10000):
        print('Input must be in the range of 1 and 10000')
    else:
        Rewards = 0
        for i in range (1, N+1):
            x = True
            for k in range(2,11):
                if i%k == 0:
                    x = False
                    
            if x == True:
                Rewards += 1
        print('Number of rewards: ',Rewards)
