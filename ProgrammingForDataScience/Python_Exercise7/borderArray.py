import numpy as np

#The Border Array
ba = np.ones((3,3), dtype=int)
borderArr = np.pad(ba, (1, 1), 'constant', constant_values=(0))
print('Using function: \n', borderArr, '\n')

#Using stack & slice
zeroVertical = np.zeros(5, dtype=int).reshape(5,1)
zeroHorizontal = np.zeros(3, dtype=int)

newBorderArr = np.vstack([zeroHorizontal, ba[0:3,:]])
newBorderArr = np.vstack([newBorderArr,zeroHorizontal])

newBorderArr = np.hstack([zeroVertical, newBorderArr])
newBorderArr = np.hstack([newBorderArr, zeroVertical])
print('Using stack & slice: \n',newBorderArr)