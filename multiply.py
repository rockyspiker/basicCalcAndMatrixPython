matrixOne = []
matrixTwo = []
matrixResult = []

def getMatrixOne():
    print('Enter a matrix a row at a time. End with a blank line.')
    getInput(1)

def getMatrixTwo():
    print('Enter a matrix. End with a blank line.')
    getInput(2)

def getInput(matrixNum):
    isValid = True
    inp = input(': ')
    if (inp):
        row = inp.split()
        for num in row:
            if not (num.isdigit()):
                print(num + ' is an invalid input. Please restart this row.')
                isValid = False
                getInput(matrixNum)
        if (isValid and validLen(matrixNum, len(row))):
            if (matrixNum == 1):
                matrixOne.append(row)
                getInput(matrixNum)
            elif (matrixNum == 2):
                matrixTwo.append(row)
                getInput(matrixNum)
            else:
                print('System error, "MATRIX NUMBER", line 30.')

def validLen(matrixNum, rowLen): # makes sure every row is the same length
    if (matrixNum == 1):
        if (len(matrixOne) == 0):
            return True
        elif (len(matrixOne[0]) == rowLen):
            return True
        else:
            print('All rows must be the same length. Please restart this row.')
            getInput(matrixNum)
            return False
    elif (matrixNum == 2):
        if (len(matrixTwo) == 0):
            return True
        elif (len(matrixTwo[0]) == rowLen):
            return True
        else:
            print('All rows must be the same length. Please restart this row.')
            getInput(matrixNum)
            return False
    else:
        print('System error, "MATRIX NUMBER", line 52.')

def multiply():
    if (len(matrixOne[0]) == len(matrixTwo)):
        print('They can be multiplied.')
        for rowOfOne in range(len(matrixOne)):
            row = []
            for colOfTwo in range(len(matrixTwo[0])):
                result = 0
                for rowOfTwo in range(len(matrixTwo)):
                    result += int(matrixOne[rowOfOne][rowOfTwo]) * int(matrixTwo[rowOfTwo][colOfTwo])
                row.append(result)
            matrixResult.append(row)
        for row in range(len(matrixResult)):
            for col in range(len(matrixResult[0])):
                print(matrixResult[row][col], end='\t')
            print('\n', end='')
    else:
        print('The first matrix must contain the same amount of columns as the second matrix has rows.')

getMatrixOne()
getMatrixTwo()
multiply()