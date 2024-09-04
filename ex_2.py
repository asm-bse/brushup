import numpy as np

# Определение матрицы D
D = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, -1]
])

# Вычисление D^2
D_squared = D@D

n = np.random.randint(3,999) 
D_n = np.linalg.matrix_power(D, n)

# Вывод результатов
print("D^2:")
print(D_squared)

print(f"\nD^{n}:")
print(D_n)
