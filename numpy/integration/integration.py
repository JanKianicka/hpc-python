import numpy as np

dx = 0.01
input = np.arange(0., np.pi/2, dx)
print('input',input)

xi = (input[1:] + input[:-1])/2
print('xi',xi)

inForSum = np.sin(xi)*dx
print('inForSum', inForSum)

res = np.sum(inForSum)
print(res)





