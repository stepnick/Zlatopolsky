A = False
B = False
C = True
a = (not A or not B) and not C
b = (not A or not B) and (A or B)
c = A and B or A and C or not C
print("a)",a)
print("б)",b)
print("c)",c)
