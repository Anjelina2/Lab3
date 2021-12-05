from datetime import datetime
from prettytable import PrettyTable
import random
import sorts

N = int(input("Введите число элементов последовательностей: "))
list = []  # создание рандомной последовательности
for i in range(N):
    list.append(random.randint(-100000, 100000))


def s(list):  # функция, котороя считает время выполнения различных сортировок
    start = datetime.now().timestamp()
    sorts.bubble(list)
    b = str(datetime.now().timestamp() - start)

    start = datetime.now().timestamp()
    sorts.the_Shell_method(list)
    t = str(datetime.now().timestamp() - start)

    start = datetime.now().timestamp()
    sorts.Fast(list)
    f = str(datetime.now().timestamp() - start)

    pyar = list.copy()
    start = datetime.now().timestamp()
    pyar.sort()
    p = datetime.now().timestamp() - start

    return b, t, f, p


b, t, f, p = s(list)  # случайная
list.sort()
b1, t1, f1, p1 = s(list)  # отсортированная
list.reverse()
b2, t2, f2, p2 = s(list)  # отсортированная в обратном порядке

# заполняем таблицу
text = PrettyTable()
text.add_column("Метод", ["Метод пузырька", "Метод Шелла", "Быстрая сортировка", "Встроенная функция"])
text.add_column("Случайная", [b, t, f, p])
text.add_column("Отсортированная", [b1, t1, f1, p1])
text.add_column("Отсортированная в обратном порядке", [b2, t2, f2, p2])

# переносим данные в файл
file = open("output.txt", "w")
text_txt = text.get_string()
file.write("Число элементов последовательностей: " + str(N) + '\n')
file.write(text_txt)
file.close()
