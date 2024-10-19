try:
    user_input = input('Enter the sequence: ').split() #input from user
    sequence = [] #creating a list for sequence
    for i in user_input:
        x = int(i.strip())  #removes any extra spaces in the splitted input
        sequence.append(x)
except ValueError:
    print('Enter only integers')
else:
    a = len(sequence)
    if not( a>1 and a<10):
        print("Sequence must have atleast 2 integers and atmost 9 integers")
    else:
        b = True
        for i in range(0,a-1,2):
            if not(sequence[i] < sequence[i+1]):
                b = False
                break
        for j in range(1,a-1,2):
            if not(sequence[j] > sequence[j+1]):
                b = False
                break
        if b:
            print('nice')
        else:
            print('not nice')
                
