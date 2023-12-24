
import sys

firstNumber = int(sys.argv[1])
operator = sys.argv[2]
secondNumber = int(sys.argv[3])
result = {}

resultPlu = lambda x,y: x + y
result.update({'+': resultPlu(firstNumber, secondNumber)})

resultSub = lambda x,y: x - y
result.update({'-': resultSub(firstNumber, secondNumber)})

resultMul = lambda x,y: x * y
result.update({'*': resultMul(firstNumber, secondNumber)})

resultPow = lambda x,y: x ** y
result.update({'**': resultPow(firstNumber, secondNumber)})

try:
    resultDiv = lambda x,y: x / y
    result.update({'/': resultDiv(firstNumber, secondNumber)})
except (ZeroDivisionError) as err:
    print(err)

print(result.get(operator))

#selesai