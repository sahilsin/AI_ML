import matplotlib.pyplot as plt
import numpy as np
import math as mt

#changing value of n i.e the number of coin tossed as for simulation nothing else can be varied
for n in range(3,1000):
    P_E=0
    P_F=0
    P_G=0
    P_EF=0
    P_EG=0
    P_GF=0
    EF=0
    EG=0
    GF=0
    i=n

    P_E=((mt.factorial(n)/(mt.factorial(n-i)*mt.factorial(i))))*pow(0.5,i)+((mt.factorial(n)/(mt.factorial(n-0)*mt.factorial(0))))*pow(0.5,i)

    P_F=((mt.factorial(n)/(mt.factorial(n-(i-1))*mt.factorial(i-1))))*pow(0.5,i)+((mt.factorial(n)/(mt.factorial(n-i)*mt.factorial(i))))*pow(0.5,i)

    P_G=1-((mt.factorial(n)/(mt.factorial(n-i)*mt.factorial(i))))*pow(0.5,i)

    P_EF=((mt.factorial(n)/(mt.factorial(n-i)*mt.factorial(i))))*pow(0.5,i)

    P_EG=((mt.factorial(n)/(mt.factorial(n-0)*mt.factorial(0))))*pow(0.5,i)

    P_GF=((mt.factorial(n)/(mt.factorial(n-(i-1))*mt.factorial(i-1))))*pow(0.5,i)

    if (P_G < 0): P_G = 0

    EF=P_E*P_F
    EG=P_E*P_G
    GF=P_G*P_F



    print("P(E)=",P_E)
    print("P(F)=",P_F)
    print("P(G)=",P_G)
    print("P(EF)=",P_EF)
    print("P(EG)=",P_EG)
    print("P(GF)=",P_GF)

    if(EF==P_EF):
        print("P(E) and P(F) are independent")

    if(EG==P_EG):
         print("P(E) and P(G) are independent")

    if(GF==P_GF):
        print("P(G) and P(F) are independent")


