massif = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in range(2,5):
    a = massif[i]
    massif[i] = massif[10-i]
    massif[10-i] = a
print(massif)
    
