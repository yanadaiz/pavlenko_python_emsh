a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
D = (b ** 2) - (4 * a * c)
f = D ** (1/2)
if D<0:
     print("Корней нет")
else:
     x1 = (-b + f) / (2 * a)
     x2 = (-b - f) / (2 * a)
     if x1<x2:
          print(x1, x2)
     else:
          print(x2, x1)
