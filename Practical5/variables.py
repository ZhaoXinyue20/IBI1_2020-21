# task3.1
a = 131201
b = 190784
c = 90321
d = abs(a - c)
e = abs(a - b)
if d>e:
  print("d",d)
elif d==e:
  print("d = e")
else:
  print("e",e)

# task3.2
print("set X as True or False")
X = input()
print("set Y as True or False")
Y = input()
Z = (X and not Y) or (Y and not X)
W = X!=Y
print("Z", Z)
print("W", W)
