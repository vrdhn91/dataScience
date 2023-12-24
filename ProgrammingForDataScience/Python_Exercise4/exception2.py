import sys

def calc(param1):
    result = 0
    if param1[1] == '+':
        result = int(param1[0]) + int(param1[2])
    elif param1[1] == '-':
        result = int(param1[0]) - int(param1[2])
    elif param1[1] == '*':
        result = int(param1[0]) * int(param1[2])
    elif param1[1] == '/':
        result = int(param1[0]) / int(param1[2])
    elif param1[1] == '**':
        result = int(param1[0]) ** int(param1[2])
    else:
        errInvalidOperator(param1[1])
    return result

def errInvalidOperator(opr):
    raise TypeError('Invalid operator', opr, 'Try again!')

loop = True
while loop:
    try:
        form = input('Please input a formula: ')
        param = form.split(' ')
        resultNumber = calc(param)
        print(resultNumber)
        loop = False
    except (ValueError, ZeroDivisionError, IndexError) as err:
        if isinstance(err, ValueError):
            print('could not convert string to int \nTry again!')
        elif isinstance(err, ZeroDivisionError):
            print('float division by zero \nTry again!')
            

