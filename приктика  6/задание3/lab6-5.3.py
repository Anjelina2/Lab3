# Генератор простых чисел

import os
from mod3 import prime_numbers

if os.path.exists("C:/Users/User/Desktop/оп/питон/приктика  6/задание3/input.txt"): # проверяет существует ли файл
    f = open("input.txt", 'r')
    N = int(f.readline()) # считывает значения
    prime_numbers(N)
    f.close()
else:
    f1 = open("output.txt", "w")
    f1.write("Файл с входными данными не обнаружен")
    f1.close()
