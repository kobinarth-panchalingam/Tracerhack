try:
    bread_prices = input().split() # input
    prices = []
    for i in bread_prices:
        prices.append(int(i.strip())) # removing extra spaces
    if (5<=len(prices)<=20):
        for j in range(len(prices)-4):
            list1 = prices[j:j+6]       #taking 5 sucessive input
            list2 = []
            for k in range(4):
                diff = list1[k+1]-list1[k] #finding the difference between two sucessive elements
                list2.append(diff > 0)     #finding fifferece is negative or positive

            if all(list2):                  #if all the differences are positive trend is upward
                print('upward',end=' ')
            elif not any(list2):            #if all the differences are negative trend is downward
                print('downward',end=' ')
            else:
                print('Unpredictable',end=' ')
    else:
        print('Number of inputs are out of range')
except ValueError:
    print('Input only intgers')
    
