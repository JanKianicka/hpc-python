import numpy as np
import math
import matplotlib.pyplot as plt

dx = 0.1
input = np.arange(0., math.pi/2, dx)
print(input)

sinIn = np.sin(input)
print(sinIn)

# Derivative
# (x-1 .. Xi .. X+1 and devided by two dx) is the numerical derivaiton
dfi = (sinIn[2:] - sinIn[:-2]) / (2.0*dx)
print('Rezs', dfi)

# Compare to cos. Note that derivative was not defined in end points
f_ref = np.cos(input[1:-1])
print("Root mean squared difference:")
print(np.sqrt(np.mean((dfi - f_ref)**2)))
plt.plot(input[1:-1], dfi, label="sin'")
plt.plot(input[1:-1], f_ref, label="cos")
plt.legend()
plt.show()

exit(0)

diff1 = ((sinIn + dX) - (sinIn - dX))
print(diff1)
print(dX2)
print(diff1.shape)
print(dX2.shape)
diff1/dX2
diffrnc = diff1/dX2

print(diffrnc)



