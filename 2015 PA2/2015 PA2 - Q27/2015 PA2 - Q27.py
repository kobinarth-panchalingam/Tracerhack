def getText(file_name): #to read input from file
    try:
        fo = open(file_name,'r')
        data = fo.read()
        fo.close()

        sentence = data.split()
        global list1
        list1 = []
        for i in sentence:  #to remove non-alphabetical characters
            x = ''
            for j in i:
                if j.isalpha():
                    x += j
            if x:
                if len(x)<20:
                    list1.append(x)
                else:
                    return 'length of a word must be less than 20'
        if not(len(list1)<1000):
            return 'Number of words must be less than 1000'
        elif not(list1):    #if empty list
            return 'No input data in FileIn.txt'
        
    except FileNotFoundError as e:
        return str(e)
    

def inOrder(order_data): #to find the alphabetically ordered words
    n = len(list1)
    if order_data == None:
        result = []
        for i in list1:
            a = list(i.lower())
            b = a.copy()
            b.sort()
            if a == b:
                result.append(i)
        order_data = ' '.join(result)

    return order_data
    

def showResult(write_data): #to print and write output
    print(write_data)
    fo = open('result.txt','w')
    fo.write(write_data)
    fo.close()

#Main Program
input_data = getText('FileIn.txt')
output = inOrder(input_data)
showResult(output)



    
