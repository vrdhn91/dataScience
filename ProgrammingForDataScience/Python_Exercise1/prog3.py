#Write a python program thats is called with some integer n and prints out all prime numbers
#in the range [2,n]. Implement the Sieve of Eratosthenes (see e.g. wikipedia) algorithm to
#obtain the prime numbers.

import sys

primeList = list(range(2,int(sys.argv[1])))

for number in primeList:
    index = 1
    while index <= len(primeList):
        if index+1 < len(primeList) and primeList[index+1] != number and primeList[index+1] % number ==0:
            primeList.remove(primeList[index+1])
        index += 1

print('prime number: ',primeList)