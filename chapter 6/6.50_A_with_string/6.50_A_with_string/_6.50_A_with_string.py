
number = input("Введите число")
a = input("Введите a")
i = 0
n = len(number)
numContainsA = false
while i != n :
    if number[i] == a :
        numContainsA = true
        break
    i += 1 
if numContainsA:
    print("Есть цифра a")
else :
    print("Нет цифры a")
input
