import math
y = int(input("y"))
x = int(input("x"))
v = int(input("v"))
i = 1
b = y
while math.fabs(y ** 2 - b ** 2) < v:
    b = y
    y = (b + x / (b - 1)) / 2
print(y)
input
