# Внешняя сортировка

from external_sorts import merge_sort
import os
import random


def write_seg(f_ind, alist):
    """
    Записывает отсортированный отрезок в файл с опредленным индексом
    """
    with open(f'fl{f_ind}.txt', 'a') as out_file:
        merge_sort(alist, 0, len(alist))
        print(*alist, file=out_file)


def segment_sort(path, m):
    """
    Открывает файл с исходгыми данными и разбивает их на отрезки по 30 элементов
    """
    file_ind = 0
    with open(path, 'r') as inp_file:
        arr = []
        num = inp_file.readline()
        while num:
            arr.append(int(num))

            if len(arr) == m:
                write_seg(file_ind % 3, arr)
                arr.clear()
                file_ind += 1

            num = inp_file.readline()

        if len(arr) > 0:
            write_seg(file_ind % 3, arr)


def my_any(arr):
    """
    Возвращает истину, когда слияние завершено, а ложь в противном случае
    """
    cnt_normal = 0
    cnt_None = 0
    for i in arr:
        if i is None:
            cnt_None += 1
        else:
            cnt_normal += 1
    if cnt_None == 3 or cnt_normal == 0:
        return False
    return True


def write(arr, ind):
    """
    Осуществляет слияние с помощью генераторов
    """
    with open(f"fl{ind}.txt" if ind != 6 else 'result.txt', 'a') as out_f:
        g = tuple((int(x) for x in y.split() if x != '\n') for y in arr if y)
        values = []

        for i in range(len(g)):
            try:
                values.append(g[i].__next__())
            except StopIteration:
                values.append(None)

        ind_min = None
        while my_any(values):
            try:
                min_v = min(x for x in values if x is not None)
                ind_min = values.index(min_v)
                out_f.write(f'{min_v} ')
                values[ind_min] = g[ind_min].__next__()
            except StopIteration:
                values[ind_min] = None

        if ind_min is not None:
            out_f.write('\n')


def check_str():
    """
    Проверка окончания внешней сортировки
    """
    lines = []
    for i in range(6):
        if os.path.exists(f"fl{i}.txt"):
            cnt = 0
            with open(f'fl{i}.txt', 'r') as curr_f:
                curr_line = curr_f.readline()
                while curr_line:
                    cnt += 1
                    if cnt > 1:
                        return False
                    lines.append(curr_line)
                    curr_line = curr_f.readline()
    write(lines, 6)
    return True


def merge():
    """
    Осуществляет внешнию сортировку
    """
    m = 3  # Режим считывания и записи
    while True:
        if check_str():
            break
        # открываем файлы для чтения
        with open(f"fl{(m + 3) % 6}.txt") as f0, open(f"fl{(m + 4) % 6}.txt") as f1, open(f"fl{(m + 5) % 6}.txt") as f2:
            lines = [
                f0.readline(),
                f1.readline(),
                f2.readline()
            ]
            f_ind = m

            while any(lines):
                write(lines, f_ind)
                f_ind = m + (f_ind + 1) % 3

                lines = [
                    f0.readline(),
                    f1.readline(),
                    f2.readline()
                ]

        for j in range(3, 6):
            f = open(f"fl{(m + j) % 6}.txt", 'w')
            f.close()

        m = 0 if m == 3 else 3


N = 55000  # Количество чисел в массиве

list_ = []  # создание рандомной последовательности
for i in range(N):
    list_.append(random.randint(-10000, 10000))

# Заполняем файл случайными числами
file = open("inp_2.txt", "w")
for line in list_:
    file.write(str(line) + '\n')
file.close()

# запуск внешней сортировки
segment_sort('inp_2.txt', 30)
merge()
