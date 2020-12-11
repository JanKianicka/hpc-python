import numpy as np

emptyArr = np.empty([4,4], dtype=np.float)
print(emptyArr)

secondRow = emptyArr[1,:]
print('Second row',secondRow)

thirdCol = emptyArr[:,2]
print('Third col', thirdCol)

emptyArr[:2,:2] = 0.21
print('Upper window', emptyArr)

checker = np.zeros((8,8))
checker[::2, ::2] = 1
checker[1::2, 1::2] = 1
print(checker)
