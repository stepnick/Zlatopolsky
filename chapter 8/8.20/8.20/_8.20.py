import random
N = 3 #Кол-во фирм
M = 3 #Кол-во дней
sum = 0
maxSum = 0
for shop in range(N):
    print("Фирма", shop+1)
    sum = 0
    for day in range(M):
        print("День", day+1, end=", ")
       # zar = random.randint(500,6000)
        zar = int(input("Введите доход: "))
      #  print("День", day+1, ", доход:", zar)
        sum += zar
    if sum > maxSum:
        maxSum = sum
  
print("Максимальный доход равен",maxSum)
