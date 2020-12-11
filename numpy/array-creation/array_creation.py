import numpy as np

inList = [1,2.3,4,5.6,7]
outArr = np.array(inList)
print(outArr)

equalSpacedArr = np.arange(-2.0, 2.0, 0.2, dtype=np.float)
print(equalSpacedArr)

eaualSpaceArr2 = np.linspace(0.5, 1.5, 11)
print(eaualSpaceArr2)

inString = 'Take some Python string and construct from it NumPy array consisting of single characters (a character array).'

outString = np.array(inString, dtype='c')
print(outString)


