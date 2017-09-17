a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
d = int(input("D: "))
DL1 = a // c
SH1 = b // d
DL2 = a // d
SH2 = b // c
if DL1 * SH1 > DL2 * SH2:
    print("при размещении длинной стороной вдоль длинной стороны стола")
else :
    print("вдоль короткой")
