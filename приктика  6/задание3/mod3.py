def prime_numbers(N):
    f = open("output.txt", "w")
    for l in range(2, N):  # проверка на простоту
        k = 0
        for i in range(2, (l // 2) + 1):
            if (l % i == 0):
                k = k + 1
        if (k <= 0):
            f.write(str(l) + ' ')
    f.close()
