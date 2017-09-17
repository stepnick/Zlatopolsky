akv = int(input("Введите сторону квадрата: "))
Rkr = int(input("Ввеите радиус круга: "))
if akv * akv > 3.14 * Rkr * Rkr:
    print("S квадрата > S круга")
else:
    print("S круга < S квадрата")
