# копейка рубль бережет

def purchase(c):
    cop = c % 100  # Нахождим рубли
    rub = c // 100  # Находим копейки
    # выбираем склонение слов "РУБЛЬ" и "КОПЕЙКА" в соответсвии с условиями
    if (rub % 10 == 0) or (10 <= rub <= 20) or (5 <= rub % 10 <= 9):
        print(rub, 'РУБЛЕЙ')
    elif rub % 10 == 1:
        print(rub, 'РУБЛЬ')
    else:
        print(rub, 'РУБЛЯ')

    if (cop % 10 == 0) or (10 <= cop <= 20) or (5 <= cop % 10 <= 9):
        print(cop, 'КОПЕEK')
    elif cop % 10 == 1:
        print(cop, 'КОПЕЙКА')
    else:
        print(cop, 'КОПЕЙКИ')


# ввод данных
purchase(c=int(input("Введите сумму покупки в копейках")))
