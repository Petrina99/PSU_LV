import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('D:\\Faks\\3.semestar\\strojno\\lv2\\tiger.png')
#povecanje svjetline
svjetlina = 2
novi_img = img * svjetlina

#rotacija
rotirana_img = np.rot90(novi_img, k = 3)

#zrcaljenje
flip_img = np.fliplr(rotirana_img)

print(novi_img.shape)

#smanjenje rezolucije
novi_img1 = novi_img[::3,::3]
print(novi_img1.shape)
plt.imshow(novi_img1, vmin=0, vmax=255)
plt.show()