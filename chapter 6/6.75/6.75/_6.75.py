number = input("Введите число :")
i = 1
kol = len(number)
PrivNumber = number
SecondInFirst = 0
FirstInSecond = 0
while i <= 20 :
   kol = len(number)
   if kol == 1 :
      SecondInFirst = number[0]
   if kol == 2 :
      SecondInFirst = number[1]
   number = input("Введите число")
   FirstInSecond = number[0]
   print(FirstInSecond)
   if SecondInFirst != FirstInSecond :
      break
   else :
      i += 1
if i != 20:
   print("последоватедльность нарушается")
else:
   print("последовательность чисел  соответствует ряду костей домино")

