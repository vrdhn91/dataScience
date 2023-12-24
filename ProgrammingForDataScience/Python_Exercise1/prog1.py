
import sys

firstNumber = int(sys.argv[1])
operator = sys.argv[2]
secondNumber = int(sys.argv[3])

if operator == '+':
    print(firstNumber + secondNumber)
elif operator == '-':
    print(firstNumber - secondNumber)
elif operator == '*':
    print(firstNumber * secondNumber)
elif operator == '/':
    if secondNumber == 0 :
        print('Error, no division by zero!')
    else:
        print(firstNumber / secondNumber)
elif operator == '**':
    print(firstNumber ** secondNumber)
else:
    print('Please enter a valid operator')

#selesai