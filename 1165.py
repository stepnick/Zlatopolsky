massif = [12,0,56,43,2,0,67,23,56,7,0,45,12,0,56,0,0,54,23,12,0,67,0,5,0,76,0]
days = 0
for i in range(0,len(massif)):
    if massif[i] == 0:
        days+= 1
print(days)
