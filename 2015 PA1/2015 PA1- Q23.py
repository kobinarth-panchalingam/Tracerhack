try:
    p = int(input('Number of players, p: ')) #taking input from user
except ValueError:
    print('Input a number')
else:
    if not(2<=p<=1000):
        print('Number of of players must be in the range of 2<=p<=1000') #checking whether p is in correct range
    else:
        rounds = 0
        matches = 0
        n = p # at round 1 all players enter the match
        while n >= 2:
            m = 1
            while m * 2 <= n: #finding the maximum possible value for m
                m *= 2
            matches += m/2
            rounds +=1
            n = (n-m) + (m/2) #finding the no.of players entering the next round
            
        print('number of rounds = %d, matches = %d'%(rounds, matches))
