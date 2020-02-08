
# Voir http://dictionnaire.sensagent.leparisien.fr/Aiguille%20de%20Buffon/fr-fr/
# https://en.wikipedia.org/wiki/Pi#/media/File:Comparison_pi_infinite_series.svg

import numpy.random as rd
from math import pi,cos


import matplotlib.pyplot as plt
import numpy as np


def calcul (N, draw):
    result=[]
    succes=1
    for i in range (2,N):
        x = rd.random()
        y = rd.random()
        if(x * x + y * y <= 1):
            succes+=1
        r=(4*succes)/i
        result.append(r)
    return result


def show1(N):
    fig, main_ax = plt.subplots()
    main_ax.set_ylim(3, 3.2)
    main_ax.set_xlim(N/10, N)
    main_ax.set_title('Méthode de Monte Carlo')
    main_ax.set_xlabel('Nombre de points')
    main_ax.set_ylabel('Approximation')
    X = [ i for i in range (2,N)]
    for i in range(5):
        Y = calcul(N, False)
        plt.plot(X, Y)
    
    plt.plot(X, [ pi for i in range (2,N)],  '-r', label='π')
    plt.legend(loc='upper right')
    plt.savefig('monte_carlo.png')
    plt.show()
    

def show2(N):
    fig, main_ax = plt.subplots()
    main_ax.set_ylim(3, 3.2)
    main_ax.set_xlim(N/100, N)
    main_ax.set_title('Méthode de Monte Carlo')
    main_ax.set_xlabel('Nombre de points')
    main_ax.set_ylabel('Approximation')
    X = [ i for i in range (2,N)]
    for i in range(5):
        Y = calcul(N, False)
        plt.plot(X, Y)
    
    plt.plot(X, [ pi for i in range (2,N)],  '-r', label='π')
    plt.legend(loc='upper right')
    plt.savefig('monte_carlo_2.png')
    plt.show()
    

show1(20000)
show2(100000)