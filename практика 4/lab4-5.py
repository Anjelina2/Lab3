from prettytable import PrettyTable # импорт установленного модуля
book = PrettyTable() # создание экземпляра

number = 0 # счётчик

book.field_names = ["Номер призывника", "Фамилия", "Имя", "Отчество", "Год рождения", "Заболевание"]  # имена полей таблицы
for i in range(1, 6):
    number += 1
    inform = {} # создание словаря
    # заполненеи словаря
    inform["Фамилия"] = input("Введите фамилию призывника №%d: " % number)
    inform["Имя"] = input("Введите имя призывника №%d: " % number)
    inform["Отчество"] = input("Введите отчество призывника №%d: " % number)
    inform["Год рождения"] = input("Введите год рождения призывника №%d: " % number)
    inform["Заболевание"] = input("Введите заболевание призывника №%d: " % number)

    book.add_row([i, inform["Фамилия"], inform["Имя"], inform["Отчество"], inform["Год рождения"], inform["Заболевание"]])  # добавление списка

print(book) # вывод таблицы
