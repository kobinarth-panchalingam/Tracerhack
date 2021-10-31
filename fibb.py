def getNum(file_name):
    '''It returns the input data in the given file name'''
    fo = open(file_name,'r')
    num = fo.read()
    fo.close()
    return int(num)
    
def fibonacci(n):
    '''It returns the n-th fibonacci number''' 
    fib = [0,1]
    for i in range(n-1):
        fib_value = fib[-1] + fib[-2]   #adding last two numbers in the list
        fib.append(fib_value)
    return fib[n]

def show(n):
    if 0<=n<=20 :
        result = 'Fibonacci(%d) = %d'%(n,fibonacci(n))
        print(result)
        return result
    else:
        print('Invalid input.')

def saveFile(data):
    '''It writes the given data to result.txt file'''
    fo = open('result.txt','w')
    fo.write(data)
    fo.close()
