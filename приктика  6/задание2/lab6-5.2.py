# Все о цифрах в числе
import  os
from mod2 import numbers

if os.path.exists('C:/Users/User/Desktop/оп/питон/приктика  6/задание2/input.txt'):  # проверяет существует ли файл
    file = open('input.txt', 'r')
    Number = file.readline().split() # считывает значения
    Number = int(Number[0])
    numbers(Number)
    file.close()
else:
    f1 = open("output.txt", "w")
    f1.write("Файл с входными данными не обнаружен")
    f1.close()