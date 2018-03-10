mas = [9,8,7,6,5,4,3,2,1]
min = int(input("Введите число: "))
rem = 0
for i in range(0, len(mas)-1):
    if mas[i] < min:
        rem = i
        break
    
if rem == 0:
    print("такого числа нет")
else :
    print(rem)
