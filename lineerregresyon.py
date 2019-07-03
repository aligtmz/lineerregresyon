import numpy as np
import matplotlib.pyplot as plt

x=[2017,2010,2000,1990,1960]
y=[80.810525,72.137546,63.174483,53.994605,27.553280]

plt.scatter(x,y)


topx=sum(x)
topy=sum(y)
n=len(x)
yort=sum(y)/n
xort=sum(x)/n

topxycarpim=topx*topy

topxkare=topx**2

karextop=0
for i in range(0,n):
    karextop+=x[i]**2

xycarpimtoplam=0
for i in range(0,n):
    xycarpimtoplam+=x[i]*y[i]


B1=(xycarpimtoplam-(topxycarpim/n))/(karextop-(topxkare/n))
B0=yort-B1*xort
print(B1,B0)
a=np.arange(3000)
plt.scatter(x,y)
plt.plot(B1*a+B0)

kac=int(input("yıl gir"))
tahmin=B1*kac+B0

print("girilen yıl için nüfus tahmini: ",tahmin)
plt.scatter(kac,tahmin,c="red",marker=">")
plt.show()



