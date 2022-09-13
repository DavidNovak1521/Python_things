import numpy as np

A = np.array((1, 2, 3))
B = np.array(((1, 2), (3, 4)))
C = np.zeros((100, 100, 3)) # vagy .ones()

print(A)
print(A.shape)
print(type(A))
print(type(A.dtype))
print(type(A[0]))
print(A[0])
print(A[-2])
print(A[0:2])

print()

print(B)
print(B.shape)
print(type(B))
print(type(B.dtype))
print(B[0][0])
print(type(B[0][0]))

print()

for i in range(A.shape[0]):
    print(i)
for i in A:
    print(i)
