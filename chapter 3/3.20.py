X = True
Y = True
print("a)")
print(not(not X or Y) or not X)
print(not(not X and not Y) and X)
print(not(X or not Y) or not Y)
X = False
Y = False
print("б)")
print(not(not X or Y) or not X)
print(not(not X and not Y) and X)
print(not(X or not Y) or not Y)
X = True
Y = False
print("в)")
print(not(not X or Y) or not X)
print(not(not X and not Y) and X)
print(not(X or not Y) or not Y)
X = False
Y = True
print("г)")
print(not(not X or Y) or not X)
print(not(not X and not Y) and X)
print(not(X or not Y) or not Y)
