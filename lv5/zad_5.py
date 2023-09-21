import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

img = plt.imread('example.png')

X = img.reshape(-1, 3)

n_klaster = 16

kmeans = KMeans(n_klaster, random_state=0).fit(X)

kvant_img_data = kmeans.cluster_centers_[kmeans.labels_]

# Preoblikujemo podatke natrag u oblik slike
kvant_img = kvant_img_data.reshape(img.shape)

plt.subplot(121)
plt.imshow(img)
plt.title('Originalna slika')
plt.axis('off')

# povecanjem broja klastera mjenjamo broj boja i kvalitetu slike
plt.subplot(122)
plt.imshow(kvant_img)
plt.title('Kvantizirana slika {} boja'.format(n_klaster))
plt.axis('off')

plt.show()


