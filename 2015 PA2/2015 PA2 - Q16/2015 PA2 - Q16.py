def getText(file_name): #function to read input from file
    try:
        with open(file_name,'r') as fo:
            data = fo.read()
            data = data.strip()
            data = data.splitlines()
        global coordinates
        coordinates = []
        for line in data:
            x = []
            line = line.split()
            for i in line:
                i = int(i)
                if i<=100:
                    x.append(i)
                else:
                    return 'Input co-ordinate is invalid'
            coordinates.append(x)
    except FileNotFoundError:
        return 'File not found in folder'
    except ValueError:
        return 'Input must be a intger'
        
def totalCells(read_data):  #function to calculate total cells
    if read_data == None:
        cells = set()
        for rect in coordinates:
            x1,y1 = rect[0], rect[1]
            x2,y2 = rect[2],rect[3]
            for i in range(x1,x2+1):
                for j in range(y1,y2+1):
                    cell = (i,j)
                    cells.add(cell)
        cell_count = str(len(cells))
        return cell_count
    else:
        return read_data

def show(write_data):   #function to print and write output
    with open('result.txt','w') as fo:
        fo.write(write_data)
    print(write_data)

#Main Program
input_data = getText('FileIn.txt')
output = totalCells(input_data)
show(output)
        
            
        
    
