# Arturo Caballero Ortega
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0,10,0.2) # Establece el tiempo, el último valor es el intervalo

plt.subplot(221)
plt.plot(t, t, 'y-', t, t**3, 'b^', t, t**2, 'gs') # Realiza la grafica usando las diferentes figuras

#--------------------------------------------------------------
data = {'a': np.arange(50),                      #
        'c': np.random.randint(1, 80, 50),       # Crea el diccionario
        'd': np.random.randn(50)}                #
data['b'] = data['a'] + 10 * np.random.randn(50) 
data['d'] = np.abs(data['d']) * 100

plt.subplot(222)
plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')

#-----------------------------------------------------------
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 10.0, 0.1)
t2 = np.arange(0.0, 10.0, 0.02)

#plt.figure()
plt.subplot(223)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.subplot(224)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
