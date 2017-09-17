import math
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))
AC = math.fabs(a - c)
BD = math.fabs(b - d)

print("AC=", AC)
print("BD=", BD)

if (AC == 2 and BD == 1) or (AC == 1 and BD == 2):
    print("Конь угрожает полю (b,c)")
else:
    print("Конь не угрожает полю (b,c)")
input
