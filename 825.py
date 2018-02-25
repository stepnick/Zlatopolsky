number1 = 120
number2 =140
count = 0



for i in range(number1, number2 + 1):
    for n in range(1, i+1):
        if i % n == 0:
            count+= 1
            print(n)
print(count)

