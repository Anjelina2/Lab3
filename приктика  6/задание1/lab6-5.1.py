# Прямоугольники и квадраты

import os
from mod import PrintRectangle
from mod import PrintSquare

t = input('Введите назвние файла с выходными данными прямоугольника')

if os.path.exists('C:/Users/User/Desktop/оп/питон/приктика  6/задание1/input1.txt'):  # проверка существования файла
    file = open('input6-5.1.txt', 'r')
    a, b = map(int, file.readline().split())  # считывание значений сторон
    PrintRectangle(a, b, t)  # вызов функции
    file.close()
else:
    f = open('%s.txt' % t, 'w')
    f.write('Файл с входными данными не обнаружен')
    f.close()

g = input('Введите назвние файла с выходными данными кввадрата')

if os.path.exists('C:/Users/User/Desktop/оп/питон/приктика  6/задание1/input2.txt'):  # проверка существования файла
    file = open('input6-5.2.txt', 'r')
    c = int(file.readline())  # считывание значения стороны
    PrintSquare(g, c)  # вызов функции
else:
    f = open('%s.txt' % g, 'w')
    f.write('Файл с входными данными не обнаружен')
    f.close()
