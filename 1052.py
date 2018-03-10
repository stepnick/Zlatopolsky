def F(x):
    global num
    if x> 0:
        print(x%10)
        F(x//10)



num = int(input("Введите число: "))
print(F(num))
