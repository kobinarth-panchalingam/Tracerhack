def getText(file_name): #function to read input from file
    try:
        with open(file_name,'r') as fo:
            data = fo.read()
        if data == '':
            return 'No input data in file'
        global N,seq
        data = data.strip('\n')
        A,N = data.split('\n')
        N = int(N)
        A = A.split()
        seq = []
        for num in A:
            seq.append(int(num.strip()))
        if not(1<=len(seq)<=100 or N<len(seq)):
            return 'Input is out of range'
            
    except FileNotFoundError :
        return 'File is not found in folder'
    except ValueError:
        return 'Input must be integer'

def derivative(read_data): # function to find the derivative of N order
    if read_data == None:
        global N,seq
        for _ in range(N):
            list1 = []
            for i in range(len(seq)-1):
                diff = seq[i+1] - seq[i]
                list1.append(str(diff))
            seq = list1
        seq = ' '.join(seq)
        return seq
    else:
        return read_data

def show(write_data): #function to print and write output
    print(write_data)
    with open('result.txt','w') as fo:
        fo.write(write_data)

#Main Program    
input_data = getText('FileIn.txt')
output = derivative(input_data)
show(output)
            
            

