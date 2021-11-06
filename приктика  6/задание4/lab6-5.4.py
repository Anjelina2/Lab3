#  Особые точки

from datetime import datetime
import time
from mod4 import dotsCounter

file = open("input.txt", "r")
s = file.read().split()  # считываем значения
radius = int(s[0])
x = int(s[1])
y = int(s[2])
file.close()

file1 = open("output.txt", "w")  # Вывод текущего времени
file1.write(str(datetime.now()))

dotsAmount = dotsCounter(radius)  # Вызов модуля, который считает количество точек с целочисленными координатами, попадающими в круг радиуса radius
file1.write("\n" + str(dotsAmount))

leadTime = time.process_time()  # Вывод времени выполнения программы
file1.write("\n" + str(leadTime))

file1.close()
