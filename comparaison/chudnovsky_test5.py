import math
import gmpy2
from gmpy2 import mpz
from time import time, sleep
import threading


# Gestion des threads
numThread=0
threadId=0
dictThread={}

def pi_chudnovsky_bs(digits):
    cste = 640320**3 // 24
    def bs(a, b):
        if b - a == 1:
            if a == 0:
                Pab = Qab = mpz(1)
            else:
                Pab = mpz((6*a-5)*(2*a-1)*(6*a-1))
                Qab = mpz(a**3*cste)
            Tab = Pab * (13591409 + 545140134*a) 
            if a & True:
                Tab = -Tab
        else:
            m = (a + b) // 2
            global numThread
            if (numThread <= 30):
                numThread+=2
                global threadId
                
                threadId+=1
                firstThread=str(threadId)
                def calc1(a,m):
                    Pam, Qam, Tam = bs(a, m)
                    global dictThread
                    dictThread[firstThread]=(Pam, Qam, Tam)
                p1 = threading.Thread(target=calc1, args=(a, m,))
                p1.start()


                threadId+=1
                secondThread=str(threadId)
                def calc2(m,b): 
                    Pmb, Qmb, Tmb = bs(m,b)
                    global dictThread 
                    dictThread[secondThread]=(Pmb, Qmb, Tmb)
                p2 = threading.Thread(target=calc2, args=(m, b,))
                p2.start()



                p1.join()
                p2.join()
                Pam, Qam, Tam = dictThread[firstThread]
                Pmb, Qmb, Tmb = dictThread[secondThread]
                numThread-=2
                del dictThread[firstThread]
                del dictThread[secondThread]
            else:
                Pam, Qam, Tam = bs(a, m)
                Pmb, Qmb, Tmb = bs(m, b)

            Pab = Pam * Pmb
            Qab = Qam * Qmb
            Tab = Qmb * Tam + Pam * Tmb
        return Pab, Qab, Tab

    DIGITS_PER_TERM = math.log10(cste/6/2/6)
    N = int(digits/DIGITS_PER_TERM + 1)

    P, Q, T = bs(0, N)
    one_squared = mpz(10)**(2*digits)
    sqrtC = gmpy2.isqrt(10005*one_squared)
    return (Q*426880*sqrtC) // T

check_digits = {
        100 : 70679,
       1000 :  1989,
      10000 : 75678,
     100000 : 24646,
    1000000 : 58151,
   10000000 : 55897,
}
import os


if __name__ == "__main__":
    digits = 100
    pi = pi_chudnovsky_bs(digits)
    #print(pi)
    #raise SystemExit
    for log10_digits in range(1,9):
        digits = 10**log10_digits
        start =time()
        pi = pi_chudnovsky_bs(digits)
        print("chudnovsky_gmpy_mpz_bs: digits",digits,"time",time()-start)
        if digits in check_digits:
            last_five_digits = pi % 100000
            if check_digits[digits] == last_five_digits:
                print("Last 5 digits %05d OK" % last_five_digits)
            else:
                print("Last 5 digits %05d wrong should be %05d" % (last_five_digits, check_digits[digits]))






# threading.active_count() --> beaucoup trop long
# https://medium.com/contentsquare-engineering-blog/multithreading-vs-multiprocessing-in-python-ece023ad55a
