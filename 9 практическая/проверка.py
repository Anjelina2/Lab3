def check():
    flag = True
    with open('result.txt', 'r') as f:
        a = list(map(int, f.readline().split()))
        print(len(a))
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                flag = False
                break
    if flag:
        print("Yes")

check()