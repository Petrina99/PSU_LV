from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('example_grayscale.png')

X = img.reshape(-1, 1)

n_klaster = 10

kmeans = KMeans(n_klaster, random_state=0)
label = kmeans.fit_predict(X)
kvantizirana_img = np.reshape(kmeans.cluster_centers_[label], img.shape)

plt.figure()
plt.imshow(img, cmap='gray')
plt.title('Originalna slika')
plt.show()

plt.figure()
plt.imshow(kvantizirana_img, cmap='gray')
plt.title('Kvantizirana slika sa {} klastera'.format(n_klaster))
plt.axis('off')
plt.show()

# povecanjem broja klastera dobivamo bolju i kristalniju sliku koja je slicnija originalnu