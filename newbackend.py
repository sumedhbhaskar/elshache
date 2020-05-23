""""
 new backend for encryption app
"""

import math 
import numpy as np
import random
import sympy
from functools import reduce

from random import randint
from numpy import poly1d
from numpy.polynomial.polynomial import Polynomial as poly



PRIME = 257

class elshache:
    
    
    
    
    @staticmethod
    def findInverse(r,finitefieldprime):
        for i in range(finitefieldprime):
            if(math.fmod(r*i,finitefieldprime)==1):
                return i

    def __init__(self,s,n,t):
        self.secret  = s
        self.total_share = n
        self.min_share = t
        self.randomNumber = random.randint(1,PRIME)
        self.randomNumberInverse = elshache.findInverse(self.randomNumber,PRIME)
        self.z_a1_coef = self.randomNumber*self.secret%PRIME

        self.sntrbz = [self.secret,self.total_share,self.min_share,self.randomNumber,self.randomNumberInverse,self.z_a1_coef]

    def shareConstruction(self):

        coef = []
        for i in range(self.min_share - 2):
            coef.append(randint(1,PRIME))

        coef.append(self.z_a1_coef)
        coef.append(self.secret)

        #equation 
        equation = poly1d(coef)

        return [ ( i , equation(i)%PRIME ) for i in range(1,self.total_share+1) ]


class elshache_re:
    
    

    def shareReconstruction(self,x_coef,y_coef,min_share):
        if(len(x_coef)!=len(y_coef) or len(x_coef) < min_share or len(y_coef) < min_share):
            raise Exception("Please recheck you input file. X and Y coef does'nt match.")

        summation = 0

        for i in range(len(x_coef)):
            l = 1
            for m in range(min_share):
                if(m!=i):
                    l*= (poly([-1*x_coef[m],1])/(x_coef[i]-x_coef[m]))
            summation += y_coef[i]*l

        return summation.coef[0]%PRIME

    def shareReconstruction_a1(self,x_coef,y_coef,min_share,randomNumberInverse):
        
        if(len(x_coef)!=len(y_coef) or len(x_coef) < min_share or len(y_coef) < min_share):
            raise Exception("Please recheck you input file. X and Y coef does'nt match.")
        
        summation = 0
        
        for i in range(len(x_coef)):
            l = 1
            for m in range(min_share):
                if(m!=i):
                    l*= (poly([-1*x_coef[m],1])/(x_coef[i]-x_coef[m]))
            summation += y_coef[i]*l

        return (summation.coef[1]*randomNumberInverse)%PRIME



"""""""