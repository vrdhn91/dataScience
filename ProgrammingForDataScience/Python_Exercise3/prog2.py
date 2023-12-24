import random

randomA = random.sample(range(0, 10), 5)
randomB = random.sample(range(0, 5), 3)

listResult = []
#result = [ x**y for x in randomA for y in randomB]
result = [[x**y for x in randomA] for y in randomB]

print('Random number A:' ,randomA)
print('Random number B:', randomB)
print(result)