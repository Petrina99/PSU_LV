from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def generate_data(n_samples, flagc):

    if flagc == 1:
        random_state = 365
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)

    elif flagc == 2:
        random_state = 148
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
        X = np.dot(X, transformation)

    elif flagc == 3:
        random_state = 148
        X, y = datasets.make_blobs(n_samples=n_samples,
        centers=4,
        cluster_std=[1.0, 2.5, 0.5, 3.0],
        random_state=random_state)

    elif flagc == 4:
        X, y = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.05)

    elif flagc == 5:
        X, y = datasets.make_moons(n_samples=n_samples, noise=.05)

    else:
        X = []

    return X


# Generiranje umjetnih podataka
# modovi 4 i 5 nam daju nekakvu vrstu oblika tj. mode 4 nam da oblik dvije kruznice, mode 5 nam da oblik 2 banane koje su obrnuto okrenute jedna prema drugoj
# mode 1 najpravilnije rasporeduje podatke
# mode 2 daje podatke koji su jako zgusnuti
num_samples = 500
mode = 3
data = generate_data(num_samples, mode)

# Vizualizacija podataka
plt.scatter(data[:, 0], data[:, 1], s=10)
plt.title('Generirani podaci')
plt.show()

# Primjena k-means algoritma
#povecavanjem broja clustera dobivamo vise centara
num_clusters = 5
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(data)

# Vizualizacija klastera
plt.scatter(data[:, 0], data[:, 1], c=kmeans.labels_, s=10)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='x', s=100, linewidths=3, color='r')
plt.title('Klasteri')
plt.show()
