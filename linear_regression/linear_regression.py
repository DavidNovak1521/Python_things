from numpy import *
from matplotlib import pyplot as plt

# adat beolvasása .txt fájlból, egy 2D tömbbe, ahol a "," jel az elválasztó
data = genfromtxt('baseball.txt', delimiter=',')

# x és y tengelyek adatai, a párok első és második tagja
x = data[:, 0]
y = data[:, 1]
print()
print('x')
print(x)
print(type(x))

plt.plot(x, y, marker='o', ls='')

# átlag számítás mind2 tengely adataira
xmean = x.mean()
ymean = y.mean()
print()
print('xmean')
print(xmean)
print(type(xmean))

# minden adatból ki kell vonni az átlagot
xm = x - xmean
ym = y - ymean
print()
print('xm')
print(xm)
print(type(xm))

# optimális modellparaméter meghatározása
# @ mátrix szorzás
w = (xm @ ym) / (xm @ xm)
print()
print('w')
print(w)
print(type(w))
print()

xx = []
yy = []
for i in range(165, 230):
    xx.append(i)
    yy.append((i - xmean) * w + ymean)

plt.plot(xx, yy, linewidth=3)

plt.title('Linear Regression')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.grid(True)

#plt.show()

# tesztelés
height = int(input('Magasság -> '))
weight = (height - xmean) * w + ymean
print(f'Becsült súly -> {weight}')
