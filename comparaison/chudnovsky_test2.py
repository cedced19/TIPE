
# https://en.wikipedia.org/wiki/Floating-point_arithmetic#Floating-point_numbers
# https://fr.wikipedia.org/wiki/Virgule_flottante

import sys
import math
from time import time
import os
import matplotlib.pyplot as plt
import numpy as np


filename = os.path.abspath('../y-cruncher/10K/pi-dec-chudnovsky.txt')
f = open(filename, "r")
ref=f.read().replace('.', '')
f.close()

def compare (i, calculated, prec):
    test=True 
    calculated=str(calculated)
    while test and i<prec:
        if(calculated[i]!=ref[i]):
            test=False
        else:
            i+=1
    
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


def chudnovsky(one,digits):
    print('Calcul des constantes')
    start_cste=time()
    # Au rang k=0
    ak=one
    a_sum=ak
    b_sum=0
    cste=640320**3//24 # précalcul de la constante qui intervient dans le calcul de ak
    numerator = sqrt(10005,one)*one*426880
    totalTime_cste = time()-start_cste
    print('Calcul des constantes effectué')

    k=1

    checked=0
    start=time()
    totalTime=0
    
    while True:
        ak*=-(6*k-5)*(2*k-1)*(6*k-1)
        ak//=(k**3)*cste
        if ak==0:
            break
        a_sum+=ak
        b_sum+=ak*k
        k+=1
        dt=time()-start
        totalTime+=dt
        denominator = 13591409*a_sum + 545140134*b_sum
        nChecked=compare(checked,numerator//denominator,digits)
        print('Nombre de décimales justes: ' + str(checked) + '   ' + str(nChecked-checked)  +  ' décimales en ' + str(dt) + 's, temps total: ' + str(totalTime) + 's')
        checked=nChecked
        start=time()

    denominator = 13591409*a_sum + 545140134*b_sum 
    
    return numerator//denominator,dt,checked,totalTime_cste

def exec_and_save_method (digits):
    '''
    Execute la méthode passée en paramètre et sauvegarde le temps d'execution `time`
    '''
    one = 10**digits
    pi,dt,correct,dt_cste=chudnovsky(one,digits)


    # Création du dossier de sauvegarde
    date=str(round(time()))
    os.mkdir('tmp/'+date+'/')
    DictTime = {'Chudnovsky test 1': dt} 
    np.save('tmp/'+date+'/time_chudnovsky.npy', DictTime)
    DictCorrect = {'Chudnovsky test 1': correct} 
    np.save('tmp/'+date+'/correct_chudnovsky.npy', DictCorrect)
    print('====================================================================')
    print('Chudnovsky a été executé pour ' + str(digits) + ' décimales en ' + str(dt) + 's')
    print('Temps de calcul des constantes: '+ str(dt_cste))
    print('Nombre de décimales justes: ' + str(correct))

exec_and_save_method(10**6)