number = input("Введите число: ")
count = len(number)
x = 0
L = number[x]
R = number[count - 1 - x]
middle =  count // 2

while x != middle:
    if L != R :
        break
    x += 1
    L = number[x]
    R = number[count - 1 - x]

if L != R :
    print("Число не является полиндромом")
else :
    print("Число является полиндромом")

