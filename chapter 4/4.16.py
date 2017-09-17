import math
Skv = float(input("Введите S квадраа: "))
Skr = float(input("Введите S круга: "))
pi = 3.14
r = (Skr / pi)
a = (Skv)
d = (2 * a**2)
if r <= a:
    print("Круг умещается в квадрате")
elif r >= d:
    print("квадрат умещается в круге")
else:
    print("ни одно из условий не выполняется")
