import pandas as pd
import statistics as st
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
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
sys.exit()
plt.hist(data, bins=30, normed=True)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
y = norm.pdf(x, mean, std)
plt.plot(x, y)
plt.show()
