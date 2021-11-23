from math import *
from decimal import Decimal
# Black Scholes
def bscholes(S,X,r,T,i):

    d_1 = (log10(S/X)+(r+(pow(i,2))/2)*T)/(i*sqrt(T))
    d_2 = (log10(S/X)+(r-(pow(i,2))/2)*T)/(i*sqrt(T))
    BS = S*d_1-X*exp(-r*T)*d_2

    print('$' + str(round(BS,2)))

bscholes(38.72,42,0.02,31,0.031)