data = input('Input: ') #taking series of numbers from user in space seperated manner
list1 = list(map(int, data.split())) #mapping the elements as integers
count = 0
#Method 1

for i in list1:
    while i >= 2:
        if i%2 == 0:  
            if i == 2:
                count +=1   # if the number can be written in the power of 2 one increment in the count
            i = i//2
        else:
            break

##Method 2

##def divide(a):
##    if a%2 == 0:
##        if a==2:
##            global count
##            count +=1
##        else:
##            a = a//2
##            divide(a)
##
##for i in list1:
##    if i>0:
##        divide(i)
        
print('Number of powers of two: ',count)
            
