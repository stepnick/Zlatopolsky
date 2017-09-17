y = int(input("Введите y (0 ≤ y < 360):"))
hours = y // 30
minutes =  (y % 30) *2
print("полное число часов:", hours,"полное число минут:", hours * 60 + minutes)
 
