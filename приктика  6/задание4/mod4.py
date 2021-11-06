def dotsCounter(radius):
    t = (2 * radius - 1) ** 2  # через площадь квадрата
    if t > 0:
        t += 4
        return (t)
    else:
        return ("Окружности нет")
