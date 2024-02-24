a, b = -2.5, 2.5
n = 11

x = []
step = (b-a)/(n-1)

for i in range(0, n):
    x.append(a + step*i)
print(x)

