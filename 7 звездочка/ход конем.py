# Задача: Ход конем

def table(matrix):  # Переделываем двумерный список board в таблицу
    A = len(matrix)
    B = len(matrix[0])
    output = ""
    for i in range(A):
        output += ("{:<3} " * B).format(*matrix[i]) + "\n"
    return output.rstrip()


motion = [[2, 1], [2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]  # Ходы  шахматного коня


def allowed_moves(x, y):  # Доступные пути из точки x, y
    possible = []
    for m in motion:
        if (0 <= x + m[0] < N) and (0 <= y + m[1] < M) and (board[y + m[1]][x + m[0]]) == 0:
            possible.append(m)
    return possible


def decision():  # решение задачи с помощью правила Варнсдорфа (при обходе доски коню надо следовать в то поле, из которого существует минимальное число ходов)
    x = X - 1
    y = Y - 1
    for i in range(1, M * N + 1):
        board[y][x] = i
        next_move = []
        min = 9
        for move in allowed_moves(x, y):
            count = len(allowed_moves(x + move[0], y + move[1]))
            if count < min and (count != 0 or i == N * M - 1):
                min = count
                next_move = move
        if len(next_move) == 0:
            break
        x = x + next_move[0]
        y = y + next_move[1]
    if i != M * N:
        print(f"Маршрут не построен. Остановлен на x: {x}, y: {y}. i = {i}")


# осовная программа

file = open("input.txt", "r")  # Считывание из файл
s = file.read().split()  # считываем значения
M = int(s[0])
N = int(s[1])  # Чтение размера доски
X = int(s[2])
Y = int(s[3])  # Чтение начальной позиции
file.close()

board = [[0 for j in range(N)] for i in range(M)]  # создаме доску
decision()
print(table(board))
