

from time import time
import os


def compare (calculated, prec):
    filename = os.path.abspath('../y-cruncher/10K/pi-dec-chudnovsky.txt')
    f = open(filename, "r")
    test=True 
    calculated=str(calculated)
    i=0
    while test and i<prec:
        ref = f.read(1)
        if (ref == '.'):
            ref = f.read(1)
        if(calculated[i]!=ref):
            test=False
        else:
            i+=1
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
def pi_machin(one):
    return 4*(4*arctan(5, one) - arctan(239, one))
def pi_machin_euler(one):
    return 4*(4*arctan_euler(5, one) - arctan_euler(239, one))

def pi_gauss(one):
    return 4*(12*arctan(18, one) + 8*arctan(57, one) - 5*arctan(239, one))
def pi_gauss_euler(one):
    return 4*(12*arctan_euler(18, one) + 8*arctan_euler(57, one) - 5*arctan_euler(239, one))


for log10_digits in range(1,7):
    digits = 10**log10_digits
    one = 10**digits

    start =time()
    pi = pi_machin(one)
    print(compare(pi,digits))
    print("machin: digits",digits,"time",time()-start)

    start =time()
    pi = pi_machin_euler(one)
    #print(pi)
    print("machin euler: digits",digits,"time",time()-start)

    start =time()
    pi = pi_gauss(one)
    print("gauss: digits",digits,"time",time()-start)

    start =time()
    pi = pi_gauss_euler(one)
    #print(pi)
    print("gauss euler: digits",digits,"time",time()-start)
    #print(pi_ferguson(one))
    #print(pi_hutton(one))
    #print(pi_gauss(one))