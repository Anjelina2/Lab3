import random


def bubble(list):
    N = len(list)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


def the_Shell_method(list):
    inc = len(list) // 2
    while inc:
        for index, element in enumerate(list):
            while index >= inc and list[index - inc] > element:
                list[index] = list[index - inc]
                index -= inc
            list[index] = element
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return list


def Fast(list):
    if len(list) <= 1:
        return list
    else:
        q = random.choice(list)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in list:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return Fast(s_nums) + e_nums + Fast(m_nums)



