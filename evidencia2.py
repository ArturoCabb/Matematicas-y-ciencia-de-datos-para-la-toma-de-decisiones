import pandas as pd                    
import statsmodels.api as sm           
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

import statistics as st
import numpy as np
import matplotlib.mlab as mlab
from scipy.stats import norm
import sys

df = pd.read_csv("A01369947_residuo.csv")
df.head(5)
data = df['Residuos'].values.tolist()
print(data)
mean,std=norm.fit(data)
print(mean,std)
plt.hist(data, bins=20, density=True, alpha=0.6, color='g')
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean, std)
plt.plot(x, p, 'k', linewidth=2)
title = "Fit results: mu = %.2f,  std = %.2f" % (mean, std)
plt.title(title)
print(x)
plt.show()
#sys.exit()
#plt.hist(data, bins=30, normed=True)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
y = norm.pdf(x, mean, std)
plt.plot(x, y)
plt.show()

#-----------------------------------------------------------------------------#

dt = pd.read_csv("A01369947_EtiquetasNutrimentales.csv")
calorias = dt["Calorias (kcal)"]                             
carbohidratos = dt["Carbohidratos (g)"]  
lipidos = dt["Lípidos (g)"]    
proteina = dt["Proteína (g)"]  
#sodio = dt["Sodio (mg)"]
                            
mod = smf.ols('calorias ~ carbohidratos + lipidos + proteina', data=dt).fit()  
print(mod.summary())

# Para predecir el comportamiento de los Carbohidratos
x = carbohidratos.values.reshape(-1, 1)
y = calorias.values.reshape(-1, 1)

linear_regression = LinearRegression().fit(x,y)
pred = linear_regression.predict(x)
m = linear_regression.coef_[0][0]
c = linear_regression.intercept_[0]
label = r'Y = %0.4f*Carbohidratos + %0.4f'%(m,c)
print(label)
plt.scatter(carbohidratos,calorias)
#plt.plot(carbohidratos, calorias, label = "Calorias")
plt.plot(x, pred, color = 'red', label = label)
plt.xlabel("Carbohidratos")
plt.ylabel("Calorias")
plt.legend()
plt.show()

# Para predecir el comportamiento de los Lípidos
x = lipidos.values.reshape(-1, 1)
y = calorias.values.reshape(-1, 1)

linear_regression = LinearRegression().fit(x,y)
pred = linear_regression.predict(x)
m = linear_regression.coef_[0][0]
c = linear_regression.intercept_[0]
label = r'Y = %0.4f*Lípidos + %0.4f'%(m,c)
print(label)
plt.scatter(lipidos,calorias)
#plt.plot(lipidos, calorias, label = "Calorias")
plt.plot(x, pred, color = 'red', label = label)
plt.xlabel("Lípidos")
plt.ylabel("Calorias")
plt.legend()
plt.show()

# Para predecir el comportamiento de la Proteína
x = proteina.values.reshape(-1, 1)
y = calorias.values.reshape(-1, 1)

linear_regression = LinearRegression().fit(x,y)
pred = linear_regression.predict(x)
m = linear_regression.coef_[0][0]
c = linear_regression.intercept_[0]
label = r'Y = %0.4f*Proteína + %0.4f'%(m,c)
print(label)
plt.scatter(proteina,calorias)
#plt.plot(proteina, calorias, label = "Calorias")
plt.plot(x, pred, color = 'red', label = label)
plt.xlabel("Proteína")
plt.ylabel("Calorias")
plt.legend()
plt.show()
