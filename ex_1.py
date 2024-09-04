import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
C = np.array([[2, 4, 6], [8, 1, 3], [5, 7, 9]])
I = np.eye(3) 


#task 1
result_task_1 = A + B - 2 * C
print(f'\nresult_task_1(A+B-2*C):\n {result_task_1}')

#task 2
result_task_2 = A @ B
print(f'\nresult_task_2 (A*B):\n {result_task_2}\n')

#task 3
result_task_3 = C @ C
print(f'\nresult_task_3 (C^2):\n {result_task_3}\n')

#task 4
det_B = np.linalg.det(B)
if int(det_B) == 0.0:
    print("Matrix B is singular, so it does not have an inverse.")
    B_inv = "Do not exist"
else:   
    B_inv = np.linalg.inv(B)

result_task_4 = B_inv
print(f'\nresult_task_4 (B^(-1)):\n {result_task_4}\n')

#task 5
det_A = np.linalg.det(A)
det_B = np.linalg.det(B)

print(f'\nresult_task_5:')
print(f'Determinant of A: {det_A:.3f}')
print(f'Determinant of B: {det_B:.3f}')

#task 6

eigenvalues_A = np.linalg.eigvals(A)
eigenvalues_B = np.linalg.eigvals(B)
eigenvalues_C = np.linalg.eigvals(C)

print(f'\nresult_task_6 (C^2):')
print(f"Eigenvalues of A: {eigenvalues_A}")
print(f"Eigenvalues of B: {eigenvalues_B}")
print(f"Eigenvalues of C: {eigenvalues_C}")

#task 7
#A^2 - B = X - I => X = A^2 - B + I
X1 = A@A - B + I
result_task_7 = X1
print(f'\nresult_task_7 (X):\n {result_task_7}')

#task 8
#CX + X = B  =>  (C + I)X = B  =>  X = inv(C + I) * B
X2 = np.linalg.inv(C + I) @ B
result_task_8 = X2
print(f'\nresult_task_8 (X):\n {result_task_8}')

#task 9

def is_symmetric(matrix):
    return np.allclose(matrix, matrix.T)

# Проверяем симметричность X1, X2, A, B, C
result_task_9 = {
    "X1": is_symmetric(X1),
    "X2": is_symmetric(X2),
    "A": is_symmetric(A),
    "B": is_symmetric(B),
    "C": is_symmetric(C)
}
print(f'\nresult_task_9 (X):\n {result_task_9}')

