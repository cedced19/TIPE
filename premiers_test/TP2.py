
# https://giordano.github.io/blog/2017-11-21-hexadecimal-pi/
# https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula#BBP_digit-extraction_algorithm_for_%CF%80

import numpy as np 

eps = np.finfo(float).eps

def powermod(a, b, n):
    return a**b%n

def S(n, j):
    # Somme de gauche
    s = 0.0
    denom = j
    for k in range(0,n+1):
        s      = s + powermod(16, n - k, denom) / denom
        denom += 8

    # Somme de droite
    num = 1 / 16
    frac = num / denom
    while (frac > eps):
        s     += frac
        num   /= 16
        denom += 8
        frac = num / denom
    return s

def pi_digit(n):
    return hex(int(16 * ((4*S(n, 1) - 2*S(n, 4) - S(n, 5) - S(n, 6))% 1.0)))[2:]


def allpi(n):
    number = "0x3."
    for i in range(0,(n*16)+1):
        number+= pi_digit(i)
    return(number)


print(allpi(30))
