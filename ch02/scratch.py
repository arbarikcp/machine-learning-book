import numpy as  np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

p = np.dot(a, b)

print(np.matmul(a,b))
print(a @ b)

print(p)

A = np.array([[1, 2],
              [3, 4],
              [5, 6]])
B = np.array([2,3])
p = np.dot(A, B)

print(p)
print(p.shape)
print(A @ B)

B_col = B.reshape(2, -1)
p = np.dot(A, B_col)

print(p)
print(p.shape)