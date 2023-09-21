import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

# ucitavanje ociscenih podataka
df = pd.read_csv('cars_processed.csv')
print(df.info())

sortirani_df = df.sort_values(by=['selling_price'])
print('NAJSKUPLJI:', sortirani_df.tail(1))
print('NAJJEFTINIJI:', sortirani_df.head(1))

proizvedeni_2012 = df[(df.year == 2012)]

print('broj proizvedenih 2012. :',len(proizvedeni_2012))

sortiraj_km = df.sort_values(by=['km_driven'])

print('NAJVISE KM:', sortiraj_km.tail(1))
print('NAJMANJE KM:', sortiraj_km.head(1))

print('Prosjecan broj sjedala:', df['seats'].mean())

print('PROSJECNA KM (DIZEL):', df[(df.fuel == 'Diesel')]['km_driven'].mean())
print('PROSJECNA KM (BENZIN):', df[(df.fuel == 'Petrol')]['km_driven'].mean())

# razliciti prikazi
sns.pairplot(df, hue='fuel')

sns.relplot(data=df, x='km_driven', y='selling_price', hue='fuel')
df = df.drop(['name','mileage'], axis=1)

obj_cols = df.select_dtypes(object).columns.values.tolist()
num_cols = df.select_dtypes(np.number).columns.values.tolist()

fig = plt.figure(figsize=[15,8])
for col in range(len(obj_cols)):
    plt.subplot(2,2,col+1)
    sns.countplot(x=obj_cols[col], data=df)

df.boxplot(by ='fuel', column =['selling_price'], grid = False)

df.hist(['selling_price'], grid = False)

x = df.drop(['name'])
y = df['selling_price']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print("Veličina trening skupa:", X_train.shape)
print("Veličina testnog skupa:", X_test.shape)

plt.show()


tabcorr = df.corr()
sns.heatmap(df.corr(), annot=True, linewidths=2, cmap= 'coolwarm') 


