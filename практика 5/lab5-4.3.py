""" Время прибытия """


def time(Hotp, Motp, Hp, Mp):
    hours = (Hotp + Hp) % 24  # ищем часы прибытия(остаток  от деления сумму часов на количество часов в сутках)
    days = Hp // 24  # считаем количество часов в пути
    if Motp + Mp >= 60:  # складываем минуты и проверяем
        minutes = Motp + Mp - 60  # если минут больше 60, то вычитаем из количества минут час и этот час добавляем в количество часов
        hours += 1
    else:
        minutes = Motp + Mp  # если сумма минут меньше 60 то просто их складваем

    # выводим ответ
    if minutes < 10:
        if hours < 10:
            print("0" + str(hours) + " hours :", "0" + str(minutes) + " minutes")
            print(str(days) + " days")
        else:
            print(str(hours) + " hours :", "0" + str(minutes) + " minutes")
            print(str(days) + " days")
    elif hours < 10:
        print("0" + str(hours) + " hours :", str(minutes) + " minutes")
        print(str(days) + " days")
    else:
        print(str(hours) + " hours :", str(minutes) + " minutes")
        print(str(days) + " days")


# ввод данных
time(Hotp=int(input('Часы отправления: ')), Motp=int(input('Минуты отпрвления: ')), Hp=int(input('Часы в пути: ')), Mp=int(input('Минуты в пути: ')))
