import numpy as np
#Solve all these problems without ever performing a loop explicitly! For most of them there exists a matching NumPy Function!

#a) Use NumPy to sort along the i-th axis of an array.
inputA = np.random.randint(0, 10, (8))
print('Input A: \n',inputA)
print('Sort 0 axis:\n', np. sort(inputA, axis=0))


#b) Use NumPy to to sort the rows of you 2D array according to the i-th column.
inputB = np.random.randint(0, 10, (3, 3))
print('\nInput B: \n',inputB)
print('Sort 1 axis:\n', np. sort(inputB, axis=1))


#c) Use NumPy to to remove single-dimensional entries from a specified shape (e.g. specified shape: (3, 1, 4) → (3, 4)).
inputC = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print('\nInput C: \n',inputC)
outputC = np.delete(inputC, 8)
print('Remove one element:', outputC, '\n')


#d) Use NumPy to to create a 5x5 matrix with row values ranging from 0 to 4.
inputD = np.random.randint(0, 4, (5,5))
print('Input D: \n',inputD)


#e) Use NumPy to to calculate the sum of all the multiples of 7 or 11 below 200.
inputE = np.arange(1, 200)
outputE = inputE[(inputE % 7 == 0) | (inputE % 11 == 0)]
print('\nInput E: \n',inputE)
print('Sum: ',outputE.sum())


#f) Use NumPy to to join a sequence of arrays along a new axis.
inputF1 = np.random.randint(0, 10, (3, 3))
inputF2 = np.random.randint(0, 10, (3, 3))
print('\nInput F1: \n',inputF1)
print('\nInput F2: \n',inputF2)
outputF = np.stack((inputF1, inputF2), axis = 1 )
print('\nOutput F: \n',outputF)


#g) Use NumPy to to get the row numbers in given array where at least one item is larger
#than a specified value.
inputG1 = np.array([7, 0, 9, 2, 7, 6, 2, 3])
print('\nInput G1: \n',inputG1)
print(np.any(inputG1>8, axis=0))
outputG = np.where(np.any(inputG1>8, axis=0))
print('\nOutput G: \n',outputG)


#h) Use NumPy to to partition a given array in a specified position and move all the smaller
#elements values to the left of the partition, and the remaining values to the right, in
#arbitrary order (based on random choice).
inputH = np.random.randint(0, 10, (6, 6))
print('\nInput H1: \n',inputH)
indexPartition = 3
#sort and flatten first
flatten = np.sort(inputH, axis=None)
#split the result into 2 parts
tmp = int(len(flatten)/2)
leftPart = flatten[:tmp].reshape(6,indexPartition)
rightPart = flatten[tmp:].reshape(6,indexPartition)
outputH = np.hstack([leftPart,rightPart])
print('\nOutput H: \n',outputH)  


#i) Use NumPy to to sort the n smallest elements of a given array (without sorting the
#complete array!).
inputI = np.random.randint(0, 10, (4, 3))
n = 6
print('\nInput I: \n',inputI)
print('N : ',n)
outputI = np.sort(inputI, axis=None)[:n]
print('\nOutput I: \n',outputI)  


#j) (optional) Use NumPy to to compute a histogram for a given array using functions
#linspace, searchsorted, unique,