import pandas as pd
import numpy as np

mtcars = pd.read_csv('D:\\Faks\\3.semestar\\strojno\\lv3\\mtcars.csv')

sortiraj_mpg = mtcars.sort_values(by=['mpg'])
print(sortiraj_mpg.tail(5))

print(sortiraj_mpg[(mtcars.cyl == 8)].head(3))

print(sortiraj_mpg[(mtcars.cyl == 6)]['mpg'].mean())

print(sortiraj_mpg[(mtcars.cyl == 4) & (mtcars.wt >= 2.) & (mtcars.wt <= 2.2)]['mpg'].mean())

print(len(mtcars[mtcars.am == 0]))
print(len(mtcars[mtcars.am == 1]))

print(len(mtcars[(mtcars.am == 1) & (mtcars.hp > 100)]))

mtcars['kg'] = mtcars.wt * 0.45 * 1000

print(mtcars[['car', 'kg']])