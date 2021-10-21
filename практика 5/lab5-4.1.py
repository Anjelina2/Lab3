# Вид треугольника

# проверяем, существует ли треугольник
def triangle():
    if (a + b) > c and (a + c) > b and (b + c) > a:
        return True
    else:
        return False


# проверяет вид треугольника
def type():
    if (a == b) or (b == c) or (a == c):
        return 1
    elif (a == b) and (b == c):
        return 2
    else:
        return 3


# вводим данные
a = float(input("Введите длину первой стороны "))
b = float(input("Введите длину второй стороны "))
c = float(input("Введите длину третьей стороны "))
# сама программа
if triangle() == True:
    if type() == 1:
        print("Треугольник равнобедренный")
    elif type() == 2:
        print("Треугольник равносторонний")
    elif type() == 3:
        print("Треугольник общего вида")
else:
    print("Треугольник не существует")
