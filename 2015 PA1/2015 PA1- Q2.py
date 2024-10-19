def check1(decimal):            #finding decimal number is in pallindrome
    if decimal == decimal[::-1]:
        return True
    else:
        return False
def check2(binary):             #finding binary number is in pallindrome
    if binary[2:]== binary[:1:-1]:
        return True
    else:
        return False

while True:
    try:
        Input = int(input('Enter input: '))  #Taking input
        if Input == -1:
            break                           #breaking the loop when user enters -1
        elif not(1<=Input<100000):
            print('Enter an integer between 1 and 100000')
            break
    except ValueError:                      #handling unexpected inputs
        print('Enter an integer number')
    else:
        x = check1(str(Input))
        y = check2(str(bin(Input)))
        if (x and y)== True:
            print('Yes')
        else:
            print('No')
                   
