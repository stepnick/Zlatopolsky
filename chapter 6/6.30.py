number = int(input("a: "))
c = 10
d = 1 
current = (number % c) // d 
position = 1
while number > d and current != 8 :
    position += 1 
    c *= 10
    d *= 10
    current = (number % c) // d
if current == 8:
    print(position)
if current != 8:
    print(0)
input
