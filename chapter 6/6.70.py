number = int(input("Введите первое число"))
k = 0
n = 0
while number != 10000:
    k += 1
    a = number 
    number = int(input("Введите следующее число"))
    if a > number :
        print("последоватьльность нарушается на числе №",k)
        n += 1
if n >= 1 :
    print("последоватьность нарушена")
else :
    print("последоватьльность не нарушена")
input
