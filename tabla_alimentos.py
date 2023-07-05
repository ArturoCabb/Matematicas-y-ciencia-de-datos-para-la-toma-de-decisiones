# Arturo Caballero Ortega

from statistics import mode
import pandas as pd
import csv
import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

df = pd.read_csv("A01369947_EtiquetasNutrimentales.csv")

# Calcular la media de cada columna
print("Media")
mediacaloria = df['Calorias (kcal)'].mean()
print("Media de calorías      :", mediacaloria, sep=' ')
mediacarbohidratos = df['Carbohidratos (g)'].mean()
print("Medio de Carbohidratos :", mediacarbohidratos, sep=' ')
medialipidos = df['Lípidos (g)'].mean()
print("Media lipidos          :", medialipidos, sep=' ')
mediaproteina = df['Proteína (g)'].mean()
print("Media proteina         :", mediaproteina, sep=' ')
mediasodio = df['Sodio (mg)'].mean()
print("Media sodio            :", mediasodio, sep=' ')


# Calcular la mediana de cada columna
print("mediana")
calorias = df.sort_values(by=['Calorias (kcal)'], ascending=False)
calorias = calorias['Calorias (kcal)'].median()
print("Mediana calorias       :", calorias, sep=' ')

carbohidratos = df.sort_values(by=['Carbohidratos (g)'], ascending=False)
carbohidratos = carbohidratos['Carbohidratos (g)'].median()
print("Mediana carbohidratos  :", carbohidratos, sep=' ')

lipidos = df.sort_values(by=['Lípidos (g)'], ascending=False)
lipidos = lipidos['Lípidos (g)'].median()
print("Mediana lípidos        :", lipidos, sep=' ')

proteina = df.sort_values(by=['Proteína (g)'], ascending=False)
proteina = proteina['Proteína (g)'].median()
print("Mediana proteina       :", proteina, sep=' ')

sodio = df.sort_values(by=['Sodio (mg)'], ascending=False)
sodio = sodio['Sodio (mg)'].median()
print("Mediana sodio          :", sodio, sep=' ')

# Moda
print("Moda")
calorias = df['Calorias (kcal)']
calorias = mode(calorias)
print("Moda calorias          :", calorias, sep=' ')

# Carbohidratos tiene dos moda por lo que se comentará este codigo ya que es necesario correrlo en
# una version de python 3.8
#carbohidratos = df['Carbohidratos (g)']
#carbohidratos = mode(carbohidratos)
#print("Moda carbohidratos     :", carbohidratos, sep=' ')

lipidos = df['Lípidos (g)']
lipidos = mode(lipidos)
print("Moda lipidos           :", lipidos, sep=' ')

proteina = df['Proteína (g)']
proteina = mode(proteina)
print("Moda proteina          :", proteina, sep=' ')

sodio = df['Sodio (mg)']
sodio = mode(sodio)
print("Moda sodio             :", sodio, sep=' ')

#Rango
print("Rango")
calorias = df.sort_values(by=['Calorias (kcal)'], ascending=False)
calorias1 = calorias['Calorias (kcal)'].min()
calorias2 = calorias['Calorias (kcal)'].max()
rango = calorias2-calorias1
print("Rango calorias         :", rango, sep=' ')

carbohidratos = df.sort_values(by=['Carbohidratos (g)'], ascending=False)
carbohidratos1 = carbohidratos['Carbohidratos (g)'].min()
carbohidratos2 = carbohidratos['Carbohidratos (g)'].max()
rango=carbohidratos2-carbohidratos1
print("Rango carbohidratos    :", rango, sep=' ')

lipidos = df.sort_values(by=['Lípidos (g)'], ascending=False)
lipidos1 = lipidos['Lípidos (g)'].min()
lipidos2 = lipidos['Lípidos (g)'].max()
rango = lipidos2-lipidos1
print("Rango lipidos          :", rango, sep=' ')

proteina = df.sort_values(by=['Proteína (g)'], ascending=False)
proteina1 = proteina['Proteína (g)'].min()
proteina2 = proteina['Proteína (g)'].max()
rango = proteina2-proteina1
print("Rango proteina         :", rango, sep=' ')

sodio = df.sort_values(by=['Sodio (mg)'], ascending=False)
sodio1 = sodio['Sodio (mg)'].min()
sodio2 = sodio['Sodio (mg)'].max()
rango = sodio2-sodio1
print("Rango sodio            :", rango, sep=' ')

# Desviacion estandar
print("Desviacion estandar")

caloria = df['Calorias (kcal)'].std()
print("desviación calorias      :", caloria, sep=' ')

caloria = df['Carbohidratos (g)'].std()
print("desviación carbohidratos :", caloria, sep=' ')

caloria = df['Lípidos (g)'].std()
print("desviación lipidos       :", caloria, sep=' ')

caloria = df['Proteína (g)'].std()
print("desviación proteina      :", caloria, sep=' ')

caloria = df['Sodio (mg)'].std()
print("desviación sodio         :", caloria, sep=' ')

# Varianza
print("Varianza")

var = df["Calorias (kcal)"].var(ddof=0)
print("varianza calorias      :", var, sep=' ')

var = df["Carbohidratos (g)"].var(ddof=0)
print("varianza carbohidratos :", var, sep=' ')

var = df["Lípidos (g)"].var(ddof=0)
print("varianza lipidos       :", var, sep=' ')

var = df["Proteína (g)"].var(ddof=0)
print("varianza proteina      :", var, sep=' ')

var = df["Sodio (mg)"].var(ddof=0)
print("varianza sodio         :", var, sep=' ')

# Hacer grafica de regresion

x = df['Calorias (kcal)']
num_bins = 5
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
plt.title("Calorias")
plt.xlabel('Calorias')
plt.ylabel('kcal')
plt.show()

x = df['Carbohidratos (g)']
num_bins = 5
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
plt.title("Carbohirdratos")
plt.xlabel('Carbohidratos')
plt.ylabel('g')
plt.show()

x = df['Lípidos (g)']
num_bins = 5
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
plt.title("Lipidos")
plt.xlabel('Lipidos')
plt.ylabel('g')
plt.show()

x = df['Proteína (g)']
num_bins = 5
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
plt.title("Proteina")
plt.xlabel('Proteina')
plt.ylabel('g')
plt.show()

x = df['Sodio (mg)']
num_bins = 5
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
plt.title("Sodio")
plt.xlabel('Sodio')
plt.ylabel('mg')
plt.show()