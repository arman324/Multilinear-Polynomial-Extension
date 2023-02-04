import math

def binary_numbers(n):
    binary_numbers = []
    for i in range(2**n):
        binary = bin(i)[2:].zfill(n)
        binary_numbers.append(binary)
    return binary_numbers

def MultilinearPolynomialExtension(numberOfVariates, inputs):
    x = []
    print('Your multilinear polynomial extension has {} inputs'.format(numberOfVariates))

    for i in range(numberOfVariates):
        inputOfVariables = input('Please enter your inputs for your multilinear polynomial extension: ')

        x.append(int(inputOfVariables))

    e = binary_numbers(numberOfVariates)
    print(e)
    finalResult = 0
    for i in range(0,len(inputs)):
        for j in range(0, numberOfVariates):
            if j == 0:
                result = x[j] * int(e[i][j]) + (1 - x[j]) * (1 - int(e[i][j]))
            else: 
                result *= x[j] * int(e[i][j]) + (1 - x[j]) * (1 - int(e[i][j]))

        finalResult += int(inputs[i]) * result

    return finalResult

def creatMultilinearPolynomialExtension(inputs):
    numberOfVariates = math.log2(len(inputs))
    if numberOfVariates > int(numberOfVariates):
        numberOfVariates = int(numberOfVariates)+1
    else:
        numberOfVariates = int(numberOfVariates)

    while True:
        finalResult = MultilinearPolynomialExtension(numberOfVariates, inputs)

        print("your inputs: ", inputs)
        print('Final result: ', finalResult)
        print('\"Final result\" mod \"group order\" = ', finalResult % int(groupOrder))

        tryOtherInputs = input('Are there any other inputs you would like to try? (y/n)\n')
        if tryOtherInputs == 'y':
            continue
        else:
            break

groupOrder = input('Please specify the group order: ')
inputs = []
while True:
    userInput = input('Please enter your inputs, then type "end" when you\'re done: ')
    if userInput == "end":
        break
    else:
        print(userInput)
        inputs.append(userInput)

creatMultilinearPolynomialExtension(inputs)

