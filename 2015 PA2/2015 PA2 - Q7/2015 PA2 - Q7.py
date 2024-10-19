def getText(file_name): #function to read input from file
    try:
        with open(file_name,'r') as fo:
            data = fo.read()
        data = data.strip('\n')
        if not(1<len(data)<1000000):
            return 'INVALID input'
        else:
            global q
            q = int(data)
        
    except FileNotFoundError as e:
        return str(e)
    except ValueError as e:
        return str(e)
    

def findNumber(number): #function to find the n
    if number == None:
        range_list = {1:(2,10),2:(12,101),3:(103,1002),4:(1004,10003),5:(10005,100004),6:(100006,1000000)}
        l = len(str(q))
        N = 0 #length of n
        for i,j in range_list.items():
            if j[0]<= l <= j[1]:
                N = str(l - i)
        list1 = list(str(q))
        for k in N:
            list1.remove(k)
        list1.sort()
        number = ''.join(list1)
    return number

def show(write_data): #function to print and write output
    print(write_data)
    with open('result.txt','w') as fo:
        fo.write(write_data)

#Main Program    
input_data = getText('FileIn.txt')
output = findNumber(input_data)
show(output)
