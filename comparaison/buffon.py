
# Voir http://dictionnaire.sensagent.leparisien.fr/Aiguille%20de%20Buffon/fr-fr/
# https://en.wikipedia.org/wiki/Pi#/media/File:Comparison_pi_infinite_series.svg

import numpy.random as rd
from math import pi,cos


import matplotlib.pyplot as plt
import numpy as np


def calcul (N):
    l=1 # longueur de l'aiguille
    e=1 # écart entre les lammes du parquet
    # on prend l <= e
    result=[]
    succes=1
    for i in range (2,N):
        x=rd.random()*e/2
        t=rd.random()*pi*1/2
        if(cos(t)*l/2>x):
            succes+=1
        r=2*l/(e*succes/i)
        result.append(r)
    return result


def show(N):
    fig, main_ax = plt.subplots()
    main_ax.set_ylim(2.8, 3.5)
    main_ax.set_xlim(N/10, N)
    main_ax.set_title('Aiguille de Buffon')
    main_ax.set_xlabel('Nombre d\'aiguilles lancées')
    main_ax.set_ylabel('Approximation')
    X = [ i for i in range (2,N)]
    for i in range(5):
        Y = calcul(N)
        plt.plot(X, Y)
    
    plt.plot(X, [ pi for i in range (2,N)],  '-r+', label='π')
    plt.legend()
    plt.savefig('buffon.png')
    plt.show()
    

show(20000)