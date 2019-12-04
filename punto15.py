import matplotlib.pyplot as plt
import numpy as np

x=np.genfromtxt("valores.txt")
#print(x)
#sigma=(1/sigma*np.sqrt(2*np.pi))*np.exp((-(1/2)(x**2/sigma**2)))

def algoritmometropolis():
    numactual=np.random.random()*500
    m=[]
    m.append(numactual)
    for i in range(N):
        propuesta=numactual+np.random.normal()*500
        propuesta2=min()
        alpha=np.random.random()
        if(alpha<propuesta2):
            numactual=propuesta2 #se acepta el cambio
            m.append(numactual)
        else:
            m.append(numactual) #se rechaza el cambio
    return m
