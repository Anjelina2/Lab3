def move(n, start, finish):
    if n == 1:
        print("Перенести диск 1 со стержня", start, "на стержень", finish)
    else:
        temp = 6 - start - finish  # Средний стрежень
        move(n - 1, start, temp)
        print("Перенести диск", n, "со стержня", start, "на стержень", finish)
        move(n - 1, temp, finish)


n = int(input("Введите количество дисков: "))
move(n, 1, 3)
