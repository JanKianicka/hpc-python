import numpy as np
import matplotlib.pyplot as plt

a = np.random.random(1000)
a_mean = np.mean(a)
a_std = np.std(a)

print("Mean and standard deviation are: %.3f, %.3f"%(a_mean, a_std))

c = np.random.exponential(scale=1, size=1000)
c_mean = np.mean(c)
c_std = np.std(c)

print("Mean and standard deviation of exponential dist are: %.3f, %.3f"%(c_mean, c_std))

d = np.random.normal(size=1000)
d_mean = np.mean(d)
d_std = np.std(d)

print("Mean and standard deviation of normal dist are: %.3f, %.3f"%(d_mean, d_std))

plt.hist(a)
plt.show()

plt.hist(c)
plt.show()

plt.hist(d)
plt.show()
