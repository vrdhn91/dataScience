import numpy as np

#Element in array presents in another one
inputA = np.array([ 0, 10, 20, 40, 60])
inputB = np.array([ 0, 30, 40])
compare = np.isin(inputA, inputB)
print(compare)

#Return the value that presents
print(np.intersect1d(inputA, inputB))