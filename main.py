a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
p = (a + b + c)/2
f = p * (p - a) * (p - b) * (p - c)
S = f ** (1/2)
print(S)
