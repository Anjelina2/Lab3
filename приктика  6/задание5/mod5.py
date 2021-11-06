def matrix(M, N, matrixA, max_matrixA):
    row = 0
    column = 0
    for i in range(N):
        for k in range(M):
            matrixA[row][column] = matrixA[row][column] // max_matrixA[row]  # Деление каждого элемента строк матрицы на максимальное число в каждой строке
            column += 1
        column = 0
        row += 1
    return matrixA


def writing_matrix(matrixA, matrixB, matrix):
    file = open("output.txt", "w")

    file.write("Матрица A: " + "\n")
    for i in matrixA:
        file.write(" ".join(map(str, i)) + "\n")  # Вывод матрицы А

    file.write("Матрица A, деленная на максимальное число в каждой строке: " + "\n")
    for i in matrixA:
        file.write(" ".join(map(str, i)) + "\n")  # Вывод матрицы А деленной на максимальное число в каждой строке

    file.write("Матрица B: " + "\n")
    for i in matrixB:
        file.write(" ".join(map(str, i)) + "\n")  # Вывод матрицы В

    file.write("Матрица A*B: " + "\n")
    for i in matrix:
        file.write(
            " ".join(map(str, i)) + "\n")  # Вывод матрицы, получившейся в результате умножения матрицы А на матрицу В
    file.close()
