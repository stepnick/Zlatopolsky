massif = [12,32,54,76,43,9,123,34,54,76,23,65,32,43,65,23,88,43,23,65,2,32,54,76,53,32,54,34,87,65]
max = massif[0]
min = massif[0]
for i in range(0, len(massif)):
    if massif[i] < min:
        min = massif[i]
    elif massif[i] > max:
        max = massif[i]
    else :
        continue
print("Максимальная разница в возрасте :", max - min)
