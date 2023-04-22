# Largest product in a grid
# 70600674
# ugly

import numpy as np

matrix = np.genfromtxt("11.txt").astype(int)
adjacents = 4
greatest_product = 0

# horizontal check
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]-adjacents+1):
        if greatest_product < matrix[i, j] * matrix[i, j+1] * matrix[i, j+2] * matrix[i, j+3]:
            greatest_product = matrix[i, j] * matrix[i, j+1] * matrix[i, j+2] * matrix[i, j+3]
# vertical check
for i in range(matrix.shape[0]-adjacents+1):
    for j in range(matrix.shape[1]):
        if greatest_product < matrix[i, j] * matrix[i+1, j] * matrix[i+2, j] * matrix[i+3, j]:
            greatest_product = matrix[i, j] * matrix[i+1, j] * matrix[i+2, j] * matrix[i+3, j]
# \ check
for i in range(matrix.shape[0]-adjacents+1):
    for j in range(matrix.shape[1]-adjacents+1):
        if greatest_product < matrix[i, j] * matrix[i+1, j+1] * matrix[i+2, j+2] * matrix[i+3, j+3]:
            greatest_product = matrix[i, j] * matrix[i+1, j+1] * matrix[i+2, j+2] * matrix[i+3, j+3]
# / check
for i in range(matrix.shape[0]-adjacents+1):
    for j in range(adjacents-1, matrix.shape[1]):
        if greatest_product < matrix[i, j] * matrix[i+1, j-1] * matrix[i+2, j-2] * matrix[i+3, j-3]:
            greatest_product = matrix[i, j] * matrix[i+1, j-1] * matrix[i+2, j-2] * matrix[i+3, j-3]

print(greatest_product)