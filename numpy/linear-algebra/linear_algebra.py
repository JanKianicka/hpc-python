import numpy

a = numpy.array([[2.3, 2.1],[4.2, 1.2]])
print(a)


b = a+numpy.transpose(a)
c = a.dot(b)

eig_vals = numpy.linalg.eigvals(c)
print(c)

eig_vector, eig_vals2 = numpy.linalg.eig(c)
print("\n")
print(eig_vector)
# Looks like this is eigen vector - not eigen values
print("eig_vals", eig_vals)

print("eig_vals2", eig_vals2)

u = eig_vals2[:,1]
print(u)
print("Verification: \n")

print(numpy.dot(c,u))
print(eig_vector[1]*u)



