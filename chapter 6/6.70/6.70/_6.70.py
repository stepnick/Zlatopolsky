number = int(input("Введите первое число"))
k = 0
n = -1
while number != 10000:
    k += 1
    a = number 
    number = int(input("Введите следующее число"))
    if a > number :
        if n == -1:
            n = k
if n != -1 :
    print("последоватьльность нарушается на числе №", n + 1)
else :
    print("последоватьльность не нарушена")
input
