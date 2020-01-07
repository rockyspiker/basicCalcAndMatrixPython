inputs = []

def getInput():
    inp = input('Enter an integer (Return to quit): ')
    if(inp):
        if(inp.isdigit()):
            inputs.append(int(inp))
            getInput()
        else:
            print(inp + " is an invalid entry... Enter a number or leave blank and press Return to quit.")
            getInput()

def median():
    inputs.sort()
    if(len(inputs)%2 == 0):
        return ((inputs[len(inputs)//2] + inputs[(len(inputs)//2) - 1])/2)
    else:
        return inputs[len(inputs)//2]

def printResults():
    average = sum(inputs)/len(inputs)
    if(average == round(average)): # gets rid of useless decimal places if applicable
        average = round(average)
    print('Numbers:', inputs)
    print('sum: ' + str(sum(inputs)) + ', min: ' + str(min(inputs)) + ', max: ' + str(max(inputs)) +
          ', average: ' + str(average) + ', median: ' + str(median()))

getInput()
printResults()