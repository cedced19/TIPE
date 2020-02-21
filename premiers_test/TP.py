

def pgcd (a, b):
    if (a < b):
        (a,b)=(b,a)
    q=a//b
    r=a%b
    while (r != 0):
        a=b
        b=r
        q=a//b
        r=a%b
    return b

def quotien (p, q):
    d=pgcd(p,q)
    p=p//d
    q=q//d
    if (q<0):
        p*=-1
        q*=-1
    return (p, q)

def plus (p, q):
    (x1, x2)=p
    (y1, y2)=q
    return quotien(x1*y2+x2*y1, x2*y2)

def fois (p, q):
    (x1, x2)=p
    (y1, y2)=q
    return quotien(x1*y1, x2*y2)


def dvp (p, q, n):
    r=p%q
    L=str(r)
    for i in range(n):
        L += str((r*10)//q)
        r=(r*10)%q
    return L



#https://en.wikipedia.org/wiki/Chudnovsky_algorithm
