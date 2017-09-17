a = input("Введите название первого города: ")
b = input("Введите название второго города: ")
c = input("Введите название третьего города: ")
kola = len(a)
kolb = len(b)
kolc = len(c)
if kola > kolb > kolc : 
    print('Самое длинное', a)
if kola < kolb < kolc:
    print('Самое короткое', a)
if kolb > kola > kolc:
    print("Самое длинное", b)
if kolb < kola < kolc:
    print("Самое короткое", b)
if kolc < kola < kolb:
    print("Самое короткое", c)
if kolc > kola > kolb:
    print("Самое длинное", c)
input
