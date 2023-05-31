import matplotlib.pyplot as plt

xlist = []

for i in range(-100, 100):
    xlist.append(i/10.0)

a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

ylist = []

for x in xlist:
    ylist.append(a*x**2 + b*x + c)

plt.plot(xlist,ylist)
plt.show()
