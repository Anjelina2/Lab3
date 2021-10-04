surname = input('Введите фамилию')
name = input('Введите имя')
patronymic = input('Введите отчество')
year = input('Введите год рождения')
zabolevanie = input('Введите заболевание')
book = {'Фамилия': surname, 'Имя': name, 'Отчество': patronymic, 'Год рождения': year, 'Заболевание': zabolevanie}
for i in book:
    print(i, book[i])
