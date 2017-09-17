import math
V = int(input("Введите объем прямоугольника"))
maxZ = round(math.exp(math.log(V)/3))

for x in range(27+1)  :
    for y in range(9+1):
        for z in range(3):
            if x * y * z == V :
                print("Размер прямоугольнка",(x,y,z))
input
