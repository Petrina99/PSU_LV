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

X = generate_data(n_samples=500, flagc=3)
scores = []

for k in range(1, 21):
    kmeans = KMeans(n_clusters=k, random_state=42).fit(X)
    score = kmeans.score(X)
    scores.append(abs(score))

plt.plot(range(1, 21), scores, marker='o')
plt.xlabel('Broj klastera')
plt.ylabel('Vrijednost kriterijske funkcije')
plt.show()

# u ovom zadatku dobivamo lakat metodu, sto nam je vrijednost kriterijske funkcije manja to su klasteri gusce rasporedeni