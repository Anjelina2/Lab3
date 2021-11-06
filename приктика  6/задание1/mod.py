def PrintRectangle(a, b, t):  # Функция которая выводит прямоугольник
    f1 = open("%s.txt" % t, 'w')
    f1.write('* ' * a + '\n')
    for i in range(b - 2):
        f1.write('*' + ' ' * (2 * a - 3) + '*' + '\n')
    f1.write('* ' * a)
    f1.close()


def PrintSquare(g, c):  # Функция которая выводит квадрат
    f1 = open("%s.txt" % g, 'w')
    f1.write("* " * c + '\n')
    for i in range(c - 2):
        f1.write("*" + " " * (2 * c - 3) + "*" + '\n')
    f1.write("* " * c)
    f1.close()
