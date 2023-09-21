from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage

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

n = 20
mode = 1
x = generate_data(n, mode)

# Računanje poveznica između klastera
Z = linkage(x, method='ward')

# Prikazivanje dendrograma
plt.figure(figsize=(10, 5))
dendrogram(Z)
plt.show()

# Dendrogram se može vizualizirati uz pomoć matplotlib biblioteke, a koristimo funkciju dendrogram iz modula scipy.cluster.hierarchy. 
# Podešavanjem argumenta method u funkciji linkage možemo mijenjati korištenu metodu za određivanje povezanosti između klastera. 
# Na primjer, ako postavimo method='single', koristit ćemo metodu jedne veze za određivanje povezanosti između klastera i to se jos zove nearest point algoritam
# Ovisno o odabranoj metodi i skupu podataka, dendrogram može prikazati različite strukture klastera. 
# U slučaju Zadatka 1, korištenje metode 'ward' (što je pretpostavljena vrijednost ako ne navedemo method argument) 
# daje jasnu strukturu s pet klastera. Međutim, korištenje druge metode poput 'single' ili 'complete' može dovesti 
# do nejasne strukture ili "zamršenog" dendrograma.
# Dakle, odabirom prave metode moguće je dobiti jasnu i korisnu strukturu klastera iz dendrograma.