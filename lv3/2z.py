import matplotlib.pyplot as plt
import pandas as pd

mtcars = pd.read_csv('D:\\Faks\\3.semestar\\strojno\\lv3\\mtcars.csv')

plt.subplot(2, 2, 1)

mpg_cyl = mtcars.groupby('cyl')['mpg'].mean()
plt.bar(mpg_cyl.index, mpg_cyl.values)
plt.xlabel('Broj cilindara')
plt.ylabel('Potrošnja goriva (mpg)')

plt.subplot(2, 2, 2)

##wt_cyl=mtcars.groupby('cyl')['wt']
wt_cyl = [mtcars[mtcars['cyl']==cyl]['wt'] for cyl in [4, 6, 8]]
plt.boxplot(wt_cyl, labels=[4, 6, 8])
plt.xlabel('Broj cilindara')
plt.ylabel('Težina (t)')

plt.subplot(2, 2, 3)
mjenjac_cars = mtcars.groupby('am')['mpg'].mean()
plt.bar(mjenjac_cars.index , mjenjac_cars.values)
plt.xlabel('Vrsta mjenjaca')
plt.ylabel('Potrošnja goriva (mpg)')

plt.subplot(2, 2, 4)
##???
omjer_cars = mtcars.groupby('hp','drat')
plt.show()