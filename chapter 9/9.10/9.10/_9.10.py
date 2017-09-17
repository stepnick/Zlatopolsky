a = input("Введите название первого города: ")
b = input("Введите название второго города: ")
c = input("Введите название третьего города: ")
max = a
min = a
if (len(b) > len(max)):
    max = b

if (len(c) > len(max)):
    max = c

if (len(b) < len(min)):
    min = b

if (len(c) < len(min)):
    min = c
print('Самое длинное', max)
print('Самое короткое', min)
input
