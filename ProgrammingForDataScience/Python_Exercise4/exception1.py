import sys

param = [sys.argv[x] for x in range(len(sys.argv)) if x>0]

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
        errInvalidOperator()
    return result

def errInvalidOperator():
    raise TypeError('invalid operator symbol')
    
try:
    resultNumber = calc(param)
    print(resultNumber)
except (ValueError, ZeroDivisionError, IndexError) as err:
    print(err)
    if isinstance(err, ValueError):
        print('invalid operand (not a number, e.g. "hello + 5")')


#selesai