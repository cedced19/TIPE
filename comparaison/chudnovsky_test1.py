
# https://en.wikipedia.org/wiki/Floating-point_arithmetic#Floating-point_numbers
# https://fr.wikipedia.org/wiki/Virgule_flottante

import sys
import math
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

def sqrt(a,one):
    '''
    Calcul de la racine pour `one` avec la méthode de Newton pour trouver des racines
    https://en.wikipedia.org/wiki/Newton's_method#Square_root_of_a_number
    '''
    float_lim=10**(sys.float_info.dig+1)
    x0 = a*one*one
    a_float = float((a * float_lim)) / float_lim
    x = int(float_lim * math.sqrt(a_float)) * one // float_lim
    while True:
        y = x
        x = (x + x0 // x) // 2
        if x==y:
            break
    return x


def chudnovski(one):
    # Au rang k=0
    ak=one
    a_sum=ak
    b_sum=0
    cste=640320**3//24 # précalcul de la constante qui intervient dans le calcul de ak
    
    k=1
    
    while 1:
        ak*=-(6*k-5)*(2*k-1)*(6*k-1)
        ak//=(k**3)*cste
        if ak==0:
            break
        a_sum+=ak
        b_sum+=ak*k
        k+=1
    denominator = 13591409*a_sum + 545140134*b_sum 
    numerator = sqrt(10005,one)*one*426880
    return numerator//denominator

def exec_and_save_method (digits):
    '''
    Execute la méthode passée en paramètre et sauvegarde le temps d'execution `time`
    '''
    one = 10**digits
    start=time()
    pi=chudnovski(one)
    stop=time()

    dt=stop-start
    correct=compare(pi,digits)

    # Création du dossier de sauvegarde
    date=str(round(time()))
    os.mkdir('tmp/'+date+'/')
    DictTime = {'Chudnovsky test 1': dt} 
    np.save('tmp/'+date+'/time_chudnovsky.npy', DictTime)
    DictCorrect = {'Chudnovsky test 1': correct} 
    np.save('tmp/'+date+'/correct_chudnovsky.npy', DictCorrect)
    
    print('Chudnovsky a été executé pour ' + str(digits) + ' décimales en ' + str(dt) + 's')
    print('Nombre de décimales justes: ' + str(correct))

exec_and_save_method(10**7)