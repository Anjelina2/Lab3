# Получить из 1 число N
def function(N):
    if N <= 0:
        return 'No'
    if N == 1:
        return 'Yes'
    else:
        if (function(N - 5)) == 'Yes':
            return (function(N - 5))
        else:
            return (function(N - 3))


N = int(input("Введите натуральное число N, не превышает 200: "))

print(function(N))
