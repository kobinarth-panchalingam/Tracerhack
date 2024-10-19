def getText(file_name):  #function to read input from FileIn.txt file
    try:
        with open(file_name,'r') as fo:
            data = fo.read()
        if data == '':
            return 'No data in input file'
        global FinalScore
        FinalScore = int(data.strip())
        
    except FileNotFoundError:
        return 'Input file is not found'
    except ValueError:
        return 'Input data must be an integer'
    else:
        if not(0<FinalScore<100):
            return 'final score must be in the range of 0 and 100'
        
        
def findScore(read_data): #function to find score
    if read_data == None:
        global Try,Conversions,PenaltyDropGoals
        Try = Conversions = FinalScore//7 #converted try
        PenaltyDropGoals = 0
        RemScore = FinalScore%7

        if RemScore%3 == 0:
            PenaltyDropGoals = int(RemScore/3)
        elif RemScore% 5 == 0:
            Try += 1
        else:
            return 'INVALID SCORE'
    else:
        return read_data

def showResult(write_data):  #function to print and write the output
    file2 = open('result.txt', 'w')
    if write_data == None:
        if Try > 0:
            print('Try : ',Try)
            file2.write('Try : %s\n'%Try)
        if Conversions > 0:
            print('Conversions : ',Conversions)
            file2.write('Conversions : %s\n'%Conversions)
        if PenaltyDropGoals > 0:
            print('Penalty/DropGoals : ',PenaltyDropGoals)
            file2.write('Penalty/DropGoals : %s\n'%PenaltyDropGoals)
    else:
        print(write_data)
        file2.write(write_data)
    file2.close()
    
#Main Program
input_data = getText('FileIn.txt')
output = findScore(input_data)
showResult(output)


