number = input("Введите число :")
Nine = 0
Zero = 0

for x in number:
    if x == '0':
        Zero += 1
    if x == '9' :
        Nine += 1

if Nine > Zero :
    print("Девять")
elif Zero > Nine:
    print("Ноль")
elif Zero == Nine and Zero != 0 :
    print("Одинаково")
else:
    print("Нет ни девяток, ни нолей")

