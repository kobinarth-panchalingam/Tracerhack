try:
    heights = input('Enter the heights: ').split() #input from user
    list1 = []
    for i in heights:
        i = int(i.strip()) #removing extra spaces
        if (100<=i<=200):
            list1.append(i)
        else:
            raise Exception('Input out of range')      
    pairs = 0
    for j in set(list1):
        pairs += list1.count(j)//2
    print('Number of Dancing Pairs',pairs)
    
except ValueError:
    print('Invalid inputs')
