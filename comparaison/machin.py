# Voir http://serge.mehl.free.fr/anx/pi_machin.html

import math
import time
import os

from decimal import Decimal as Dec, getcontext as gc
gc().prec = 100000


def arc_tan_it(x,n):
    '''
    Arctan nème terme
    '''
    numerator = math.pow(-1, n) * math.pow(x, 2 * n + 1)
    denominator = 2 * n + 1
    return Dec(numerator) / Dec(denominator)


def arc_tan(x, iterations):
    '''
    Arctan à l'ordre 'iterations' de 'x'
    '''
    arc_tan_of_x = Dec(0)
    for n in range(0, iterations):
        arc_tan_of_x += arc_tan_it(x,n)
    return arc_tan_of_x


def check (calculated, ref, number,prec):
    test=True 
    i=number
    while test and i<prec:
        if(calculated[i]!=ref[i]):
            test=False
        else:
            i+=1
    return i

def machin_for():
    arc_tan_1_239 = arc_tan(1/239, 3)
    arc_tan_1_5 = arc_tan(1/5, 3)

    filename = os.path.abspath('../y-cruncher/10K/pi-dec-chudnovsky.txt')
    f = open(filename, "r")
    ref = f.read()

    number = 0

    for i in range(3,gc().prec):
        arc_tan_1_239+=arc_tan_it(1/239, i)
        arc_tan_1_5+=arc_tan_it(1/5, i)
        pi = 4 * (4*arc_tan_1_5 - arc_tan_1_239)
        if(i%((gc().prec)//100) == 0):
            print('\n')
            print(str(pi)[:number])
            print(i)
            number = check(str(pi), ref, number,gc().prec)
            print(number)
    print(str(pi)[:number])

machin_for()