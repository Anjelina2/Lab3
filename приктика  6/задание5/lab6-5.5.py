# Матрицы

import numpy as np
import random
from mod5 import matrix, writing_matrix

file = open("input.txt", "r")  # Считывание из файла размера матрицы А
N = int(file.read(1))
M = int(file.read(2))
file.close()

matrixA = np.random.randint(9, size=(N, M))  # Создание рандомной матрицы А размером NxM (использую цифры от 1...9)

file = open("output.txt", "w")

file.write("Матрица A: " + "\n")
for i in matrixA:
    file.write(" ".join(map(str, i)) + "\n")  # Вывод матрицы А

max_matrixA = np.max(matrixA, axis=1)  # Поиск максимального числа в каждой строке

K = random.randint(5, 15)
matrixB = np.random.randint(9, size=(M, K))  # Создание рандомной матрицы В размером MxK (использую цифры от 1...9)

matrix(M, N, matrixA, max_matrixA)  # Деление всех элементов каждой строки на максимальное число в ней

matrix = matrixA.dot(matrixB)  # Умножение матриц с пмощью numpy

writing_matrix(matrixA, matrixB, matrix)  # Запись матриц в файл
