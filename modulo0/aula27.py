import matplotlib.pyplot as plt

a, b = -2.5, 2.5
n = 11
step = (b-a)/(n-1)

x = [a + step*i for i in range(0, n)]
y = [i**2 +2*i +3 for i in x]
print(x)
print(y)


plt.plot(x,y, 'g')
plt.legend()
plt.show()

