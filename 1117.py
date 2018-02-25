x = [1, 3, 5, 7, 9]
for i in range(0, len(x)):
    x[i] = x[i]*2
    print(x[i])

n = [1, 3, 5, 7, 9]
a = int(input("Введите число "))
for i in range(0, len(n)):
    n[i] = n[i]- a
    print(n[i])


r = [1, 3, 5, 7, 9]
for i in range(0, len(r)):
    r[i] = r[i]/r[0]
    print(r[i])
