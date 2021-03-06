import numpy as np

A = np.array([[6, 4, 1],
              [1, 8, -2],
              [3, 2, 0]])
b = np.array([7, 6, 8])

Ainv = np.linalg.inv(A)         # A の逆行列を計算
x = np.dot(Ainv, b)             # A の逆行列と b の内積

print(x)