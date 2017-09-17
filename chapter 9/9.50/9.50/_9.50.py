FirstWord = input("Введите первое слово: ")
SecondWord = input("Введите второе слово: ")
Fnumber = int(input("Введите начальную позицию: "))
Snumber = int(input("Введите конечную позицию: "))
x = SecondWord[0:Fnumber] + FirstWord + SecondWord[Snumber - 1 : ]
print(x)