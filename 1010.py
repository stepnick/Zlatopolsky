import math
def S(x,y,z):
    p = (x + y + z)/2
    s = math.sqrt(p*(p-x)*(p-y)*(p-z))
    return s








a = int(input("Введите a"))
b = int(input("Введите b"))
c = int(input("Введите c"))
d = int(input("Введите d"))
e = int(input("Введите e"))
f = int(input("Введите f"))
g = int(input("Введите g"))
print("S пятиугольника равно ",S(a,b,g)+S(g,f,c)+S(e,d,f))
