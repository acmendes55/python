import math as m
x = [1,2,3,4,5,6,7,8,9]


y = []
for i in x:
    y.append(i**2 + 2*i + 3)

z = []
for k in x:
    z.append(m.sin(k)+m.pi)

print(x)
print(y)
print(z)