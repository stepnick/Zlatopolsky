s1 = input("Введите слово: ")
i = 1
s2 = ""
for i in range(0, len(s1), 2) : 
    s2 += s1[i]
print(s2)
