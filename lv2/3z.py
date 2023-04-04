import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('D:\\Faks\\3.semestar\\strojno\\lv2\\tiger.png')

plt.figure(1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()

#povecanje svjetline
svjetlina = 2
psvjetlina_img = img * svjetlina
plt.figure(2)
plt.imshow(psvjetlina_img, cmap='gray', vmin=0, vmax=255)
plt.show()

#rotacija
rotirana_img = np.rot90(img, k = 3)
plt.figure(3)
plt.imshow(rotirana_img, cmap='gray', vmin=0, vmax=255)
plt.show()

#zrcaljenje
mirror_img = np.fliplr(img)

plt.figure(4)
plt.imshow(mirror_img, cmap='gray', vmin=0, vmax=255)
plt.show()

#smanjenje rezolucije
# svaki sesti element dohvati smanjujemo rezoluciju za 6
smanjena_rez = img[::6,::6]

plt.figure(5)
plt.imshow(smanjena_rez, cmap='gray', vmin=0, vmax=255)
plt.show()

# promjena slike
redovi = img.shape[0]
stupci = img.shape[1]
dg = stupci//4
gg = stupci//2

pr_img = img.copy()
for i in range(redovi):
    for j in range(stupci):
        if (j < dg or j > gg): 
            pr_img[i][j] = 0

plt.figure(6)
plt.imshow(pr_img, cmap='gray', vmin=0, vmax=255)
plt.show()