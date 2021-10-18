# копейка рубль бережет

def purchase(c):
    cop = c % 100  # Нахождим рубли
    rub = c // 100  # Находим копейки
    if rub > 0:  # выбираем склонение слов "РУБЛЬ" и "КОПЕЙКА" в соответсвии с условиями
        if (rub % 10 == 1) and (not (10 < rub < 20)):
            print(rub, 'РУБЛЬ')
        elif (rub % 10 == '0', '5', '6', '7', '8', '9') or (10 < rub < 20):
            print(rub, 'РУБЛЕЙ')
        elif (rub % 10 == "2", "3", "4") and (not (10 < rub < 20)):
            print(rub, 'РУБЛЯ')
    if cop > 0:
        if (cop % 10 == 1) and (not (10 < cop < 20)):
            print(cop, 'КОПЕЙКА')
        elif (cop % 10 == '0', '5', '6', '7', '8', '9') or (10 < cop < 20):
            print(cop, 'КОПЕEK')
        elif (cop % 10 == "2", "3", "4") and (not (10 < cop < 20)):
            print(cop, 'КОПЕЙКИ')


# ввод данных
purchase(c=int(input("Введите сумму покупки в копейках")))
