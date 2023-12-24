import numpy as np

cb = np.array([1,0,1,0])
counter = range(len(cb))
checkerboard = np.array([])
checkerboard = np.vstack([cb[::-1],cb])
checkerBoard1 = np.vstack([checkerboard[:,:],checkerboard[:,:]])
print(checkerBoard1)


