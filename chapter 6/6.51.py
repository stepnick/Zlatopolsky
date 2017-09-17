number = int(input("number"))
b = 10
c = 1
cur = (number % b ) // c
k = 1
number2 = 0
while number > c :
    cur2 = cur * k
    k *= 10
    b *= 10
    c *= 10
    cur = (number % b ) // c
    number2 += cur2

    
print(number2)
