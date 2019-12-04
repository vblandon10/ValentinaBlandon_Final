import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, fftfreq

datos=np.genfromtxt('monthrg.txt')

anios=datos[:,0]
#print(anios)
mes=datos[:,1]
dias=datos[:,2]
promedio=datos[:,3]
#print(promedio)

def fft_propia(arreglo,tamano):
    exponentes=[-(2j*np.pi*i)/float(size) for i in range(tamano)]
    transformada=[]
    for k in range(tamano):
        transformada.append(np.absolute(sum([arreglo[i]*(np.exp(exponentes[i])**k ) for i in range(tamano)] )))
    return np.array(transformada)
