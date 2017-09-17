number = 4321
b = 10
c = 1
curRight = (number % b ) // c
kol = 1 

while kol < number:
    kol *= 10
kol //= 10

while number > 0:
    R = number % 10
    number //= 10
    kol //= 10
    print("number =", number, "R =", R)
    L = int(number // kol)
    number %= kol
    print("number =", number, "L =", L)
    kol /= 10
if R != L :
    print("слово не является палиндромом")
print()
        
