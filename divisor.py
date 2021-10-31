while True:
    n = int(input()) #input
    if (1<=n<=100000):
        divisors = []
        for i in range(1,int(n**0.5+1)):
            if n%i == 0:
                divisors.extend((i,n//i))
        divisors = set(divisors)
        diff = 2*n-sum(divisors)
        if diff > 0:
            print(n,'is abundant by',diff)
        elif diff < 0:
            print(n,'is deficent by',abs(diff))
        else:
            print(n,'is perfect')
    else:
        print('Input is out of range')
