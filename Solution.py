def convert_postfix_LHS(leftHandSide):
    postfix = []
    stack = []

    for char in leftHandSide:
        if char.isdigit():
            postfix.append(char)
        else:
            while len(stack) > 0 and stack[-1] in precedence and precedence[char] <= precedence[stack[-1]]:
                postfix.append(stack.pop())
            stack.append(char)

    while (len(stack) > 0):
        postfix.append(stack.pop())

    return postfix


def evaluate_LHS(postfix_form_LHS):
    stack = []
    for char in postfix_form_LHS:
        if char in precedence_list:
            element2 = stack.pop()
            element1 = stack.pop()
            match char:
                case '/':
                    stack.append(element1 / element2)
                case '*':
                    stack.append(element1 * element2)
                case '+':
                    stack.append(element1 + element2)
                case '-':
                    stack.append(element1 - element2)
        else:
            stack.append(float(char))

    return stack[0]


inputFile = open('input.txt', 'r')
outputFile = open('output.txt', 'w')

conversionDict = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'plus': '+',
    'substract': '-',
    'multiple': '*',
    'division': '/',
    'equals': '='
}

precedence_list = ['+', '-', '*', '/']

precedence = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1
}

testCase = int(inputFile.readline())

for i in range(testCase):

    # Taking input line by line and adding in line.
    inputData = []
    for itr in inputFile.readline().split():
        if itr in conversionDict:
            inputData.append(conversionDict[itr])
        else:
            inputData.append(itr)

    leftHandSide = inputData[:-2]
    rightHandside = float(inputData[-1])
    postfix_form_LHS = convert_postfix_LHS(leftHandSide)
    eval_LHS = evaluate_LHS(postfix_form_LHS)

    if eval_LHS == rightHandside:
        outputFile.write(f'Case #{i+1}: true\n')
    else:
        outputFile.write(f'Case #{i+1}: false\n')
