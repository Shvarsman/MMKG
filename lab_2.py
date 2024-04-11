# Заданный базис векторного пространства U3
e1 = (0, 0, 1)
e2 = (0, 1, 0)
e3 = (1, 0, 0)

# Новый базис векторного пространства U3
e1_prime = (1, -1, 1)
e2_prime = (2, 0, -1)
e3_prime = (0, 1, 0)

# Матрица линейного оператора F в старом базисе
A = [[1, -1, 0], [2, 0, 1], [0, 2, 1]]

# Функция для нахождения матрицы перехода
def transition_matrix(basis, basis_prime):
    # Создаем пустую матрицу размерности len(basis) x len(basis)
    P = [[0 for _ in range(len(basis))] for _ in range(len(basis))]

    # Заполняем матрицу P
    for i in range(len(basis)):
        for j in range(len(basis)):
            P[i][j] = basis_prime[j][i]

    return P

# Функция для умножения матриц
def matrix_mult(A, B):
    # Проверяем корректность умножения матриц
    if len(A[0]) != len(B):
        raise ValueError("Несовместимые размерности матриц")

    # Создаем пустую матрицу размерности len(A) x len(B[0])
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Умножаем матрицы
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

# Находим матрицу перехода P
P = transition_matrix([e1, e2, e3], [e1_prime, e2_prime, e3_prime])

# Находим обратную матрицу P^(-1)
P_inverse = [[P[0][0], P[1][0], P[2][0]], [P[0][1], P[1][1], P[2][1]], [P[0][2], P[1][2], P[2][2]]]

# Находим матрицу оператора F в новом базисе
A_prime = matrix_mult(matrix_mult(P_inverse, A), P)

# Выводим матрицу оператора F в новом базисе
for row in A_prime:
    print(row)