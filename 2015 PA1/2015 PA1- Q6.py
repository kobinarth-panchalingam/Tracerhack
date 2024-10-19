try:
    n = int(input('Enter Input: '))   #taking input
except ValueError:
    print('Enter an integer')
else:
    if not( 10<n<10000):
        print('Enter an integer in between 10 and 10000')
    else:
        print('Output:')
        while True:
            remainder = n%3
            if remainder == 0:
                print(str(int(n)).rjust(5)+' - 0')
                n /= 3
            elif remainder == 1:
                print(str(int(n)).rjust(5)+' - -1')
                n = (n-1)/3
            else:
                print(str(int(n)).rjust(5)+' - 1')
                n = (n+1)/3
            if n == 1:
                print('1'.rjust(5))
                break
            
