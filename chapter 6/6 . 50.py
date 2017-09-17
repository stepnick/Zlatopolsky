number = int(input('number = '))
a = int(input("a = "))
b = int(input("b = "))
k = int(input("k = "))
c = 10
d = 1
current = (number // c ) % d
position = 0
position_b = 0
while number > d :
    if current == a:
        position += 1
    if current == b:
        position_b += 1
    c *= 10
    d *= 10
    current = (number // c ) % d
print("а)")
if position >= 1:
    print("есть цифра а")
else :
    print("нет цифры а")
print("б)")
if position_b < 1 :
    print("нет цифры b")
else :
    print("есть цифра b")
print("в)")
if position <= k:
    print("верно")
else:
    print("не верно")
print("г)")
if position >= 1 and position_b >= 1 :
    print("есть цифры a и b")
else :
    print("нет цифр a и b")
input
