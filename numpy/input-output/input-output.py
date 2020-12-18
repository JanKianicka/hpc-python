import numpy as np

a = np.loadtxt('xy-coordinates.dat')
print(a)

a[:,1:] = a[:,1:]*2.5
print(a)
args = {'header': 'XY coordinates', 'fmt': '%7.3f', 'delimiter': ','}

np.savetxt('xy-coordinates_out.txt', a, **args)
