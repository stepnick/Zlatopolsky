a = int(input("Введите a:"))
a1 = a // 1000
b = a % 1000
a2 = b // 100
c = a % 100
a3 = c // 10
a4 = a % 10 
print("a)")
print(a4*1000 + a3*100 + a2*10 + a1)
print("б)")
print("было:",a,"стало:",a2,a1,a4,a3)
print("в)")
print(a1,a3,a2,a4)
print("г1)")
print(a3,a4,a1,a2)
print("г2)")
print(a % 100 * 100 + a // 100)
