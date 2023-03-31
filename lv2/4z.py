import numpy as np
import matplotlib.pyplot as plt

def polje(x, visina, sirina):
    bijele = np.ones((x, x), dtype=int) * 255
    crne = np.zeros((x, x), dtype=int)

    red1 = np.hstack([crne, bijele] * int(sirina/2))
    red2 = np.hstack([bijele, crne] * int(sirina/2))

    polje = np.vstack([red1, red2] * int(visina/2))
    return polje

img = polje(50, 25, 3)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)

plt.show()