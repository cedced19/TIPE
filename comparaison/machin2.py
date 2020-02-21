

from time import time
import os
import matplotlib.pyplot as plt
import numpy as np

def compare (calculated, prec):
    filename = os.path.abspath('../y-cruncher/10K/pi-dec-chudnovsky.txt')
    f = open(filename, "r")
    test=True 
    calculated=str(calculated)
    i=0
    while test and i<prec:
        ref = str(f.read(1))
        if (ref == '.'):
            ref = str(f.read(1))
        if(calculated[i]!=ref):
            test=False
        else:
            i+=1
    f.close()
    return i

def arctan(x, one):
    """
    Calcul de arctan(1/x)

    arctan(1/x) = 1/x - 1/3*x³ + 1/5*x⁵ - ... (x > 1)

    Calcul en décalant la virgule en utilisant `one` comme `1` de référence
    """
    term = one // x      # correspond au terme +/- 1/x**n 
    total = term               
    x2 = x * x           # calcul de x**2 (permet de passer d'un terme à l'autre)
    denominator = 1      # coefficient au dénominateur
    while 1:
        term = - term // x2
        denominator += 2
        #term += denominator // 2   possibilité d'ajouter cela pour obtenir de meilleurs résultats
        delta = term // denominator
        if delta == 0:
            break
        total += delta
    return total



def arctan_euler(x, one):
    """
    Calcul de arctan(1/x) avec la méthode dite d'Euler

    arctan(1/x) =                   x / (1+x²)
                + (2/3)           * x / (1+x²)²
                + (2*4/(3*5))     * x / (1+x²)³
                + (2*4*6/(3*5*7)) * x / (1+x²)⁴
                + ...

    Calcul en décalant la virgule en utilisant `one` comme `1` de référence
    """
    x2_1 = x * x + 1
    term = (x * one) // x2_1 # correspond au terme 1/(1+x²)**n 
    total = term
    two_n = 2 # 2n au numérateur
    while 1:
        denominator = (two_n+1) * x2_1
        term *= two_n
        #term += denominator // 2   possibilité d'ajouter cela pour obtenir de meilleurs résultats
        term = term // denominator
        if term == 0:
            break
        total += term
        two_n += 2
    return total


# Formules de Machin https://fr.wikipedia.org/wiki/Formule_de_Machin
def machin(one):
    return 4*(4*arctan(5, one) - arctan(239, one))
def machin_euler(one):
    return 4*(4*arctan_euler(5, one) - arctan_euler(239, one))

def gauss(one):
    return 4*(12*arctan(18, one) + 8*arctan(57, one) - 5*arctan(239, one))

def gauss_euler(one):
    return 4*(12*arctan_euler(18, one) + 8*arctan_euler(57, one) - 5*arctan_euler(239, one))

def ferguson(one):
    return 4*(3*arctan(4, one) + arctan(20, one) + arctan(1985, one))

def ferguson_euler(one):
    return 4*(3*arctan_euler(4, one) + arctan_euler(20, one) + arctan_euler(1985, one))

def hutton(one):
    return 4*(2*arctan(3, one) + arctan(7, one))

def hutton_euler(one):
    return 4*(2*arctan_euler(3, one) + arctan_euler(7, one))


list_methods = ['machin','gauss','ferguson','hutton','machin_euler','gauss_euler','ferguson_euler','hutton_euler']

def exec_method (name,n):
    '''
    Execute la méthode passée en paramètre et retourne le nombre de décimales `digits`, le temps d'execution `time`, et le nombre de décimales "juste" 
    '''
    digits = 10**n
    one = 10**digits
    start=time()
    pi=eval(name + '(' + str(one) +  ')')
    stop=time()
    return (digits,stop-start,compare(pi,digits))


def lint_name(name):
    return name.capitalize().replace('_e', ' E')

def graph(N):
    fig, main_ax = plt.subplots()
    main_ax.set_title('Méthodes de Machin et autres')
    main_ax.set_xlabel('Nombre de décimales')
    main_ax.set_ylabel('Temps de calcul')
    X = [ 10**i for i in range (1,N)]
    for method in list_methods:
        time_list=[]
        for i in range (1,N):
            (digits,time,check)=exec_method(method,i)
            time_list.append(time)
        plt.plot(X,time_list,'o-', label=lint_name(method))
    plt.legend(loc='upper left')
    plt.savefig('machin2.png')
    plt.show()

graph(5)