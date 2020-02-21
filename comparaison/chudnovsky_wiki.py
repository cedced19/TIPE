#Voir https://en.wikipedia.org/wiki/Chudnovsky_algorithm
# https://www.craig-wood.com/nick/articles/pi-chudnovsky/


import time
import os
from decimal import Decimal as Dec, getcontext as gc


def compare (calculated, prec):
    filename = os.path.abspath('../y-cruncher/10K/pi-dec-chudnovsky.txt')
    f = open(filename, "r")
    ref = f.read()
    test=True 
    i=0
    while test and i<prec:
        if(calculated[i]!=ref[i]):
            test=False
        else:
            i+=1
    return i


def PI(maxK: int = 70, prec: int = 1008, disp: int = 1007):  # Parameter defaults chosen to gain 1000+ digits within a few seconds
    gc().prec = prec
    K, M, L, X, S = 6, 1, 13591409, 1, 13591409
    start = time.time()
    for k in range(1, maxK + 1):
        M = (K**3 - 16*K) * M // k**3 
        L += 545140134
        X *= -262537412640768000
        S += Dec(M * L) / X
        K += 12
    pi = 426880 * Dec(10005).sqrt() / S
    pi = Dec(str(pi)[:disp])  # Drop few digits of precision for accuracy
    number=compare(str(pi),disp)
    end = time.time()
    elapsed = end - start
    print("PI(maxK={} iterations, gc().prec={}, disp={} digits) =\n{}\n\ntime: {}\n\nnumber: {}".format(maxK, prec, disp, pi, elapsed, number))
    return pi


Pi = PI(317, 4501, 4500)

#For greater precision and more digits (takes a few extra seconds) - Try
#Pi = PI(317, 4501, 4500)
#Pi = PI(353, 5022, 5020)