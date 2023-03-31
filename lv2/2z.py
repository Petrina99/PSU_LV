import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open('D:\\Faks\\3.semestar\\strojno\\lv2\\mtcars.csv', "rb"), usecols=(1, 2, 3, 4, 5, 6), delimiter=",", skiprows=1)

# 0-ti stupac mpg, 3-ti stupac hp, 5-ti stupac tezina wt
plt.scatter(data[:, 0], data[:, 3], marker="D", c=data[:, 5], cmap='autumn')

print("Minimalna potrosnja:", np.min(data[:, 0]))
print("Maksimalna potrosnja:", np.max(data[:, 0]))
print("Prosjecna potrosnja:", np.mean(data[:, 0]))

cilindri = []

for i in range(data.shape[0]):
        if data[i][1] == 6:
            cilindri.append(data[i])

cilindri = np.array(cilindri)

print("Min potrosnja 6 cil:", np.min(cilindri[:, 0]))
print("Max potrosnja 6 cil:", np.max(cilindri[:, 0]))
print("Prosjecna potrosnja 6 cil:", np.mean(cilindri[:, 0]))

plt.show()