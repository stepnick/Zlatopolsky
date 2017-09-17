a = int(input("a"))
n = 0
b = a 
while a != 0:
    a = int(input("a"))
    if a < 0 and b > 0 or a > 0 and b < 0:
        n += 1
    b = a
print(n)
