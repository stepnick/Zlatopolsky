import math
x1 = int(input ("x1 "))
y1 = int(input ("y1 "))
x2 = int(input ("x2 "))
y2 = int(input ("y2 "))
x3 = int(input ("x3 "))
y3 = int(input ("y3 "))
AB = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print ("AB =", AB)
BC = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
print ("BC =", BC)
CA = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
print ("CA =", CA)
P = AB + BC + CA
print ("Pabc =", P)
p = P / 2
print ("Sabc =", math.sqrt(p * (p - AB) * (p - BC) * (p - CA)))# не всегда получаетя, т.к. d<0
input ("нажмите Enter, чтобы выйти")
