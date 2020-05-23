""""
 new backend for encryption app
"""
from __future__ import division
from __future__ import print_function

import math 
import numpy as np
import random
import sympy
from functools import reduce

from random import randint
from numpy import poly1d
from numpy.polynomial.polynomial import Polynomial as poly




import random
import functools
from numpy.polynomial.polynomial import Polynomial as poly



PRIME = 257
_PRIME = 257

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
        return make_random_shares(self.secret,self.z_a1_coef,self.min_share,self.total_share)
#         coef = []
#         for i in range(self.min_share - 2):
#             coef.append(randint(1,PRIME))

#         coef.append(self.z_a1_coef)
#         coef.append(self.secret)

#         #equation 
#         equation = poly1d(coef)

        


#         return [ ( i , equation(i)%PRIME ) for i in range(1,self.total_share+1) ]


class elshache_re:
    
    

    def shareReconstruction(self,x_coef,y_coef,min_share):
        if(len(x_coef)!=len(y_coef) or len(x_coef) < min_share or len(y_coef) < min_share):
            raise Exception("Please recheck you input file. X and Y coef does'nt match.")

#         summation = 0

#         for i in range(len(x_coef)):
#             l = 1
#             for m in range(min_share):
#                 if(m!=i):
#                     l*= (poly([-1*x_coef[m],1])/(x_coef[i]-x_coef[m]))
#             summation += y_coef[i]*l

#         return summation.coef[0]%PRIME
        return recover_secret(x_coef,y_coef)

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



"""
added solid code for a0 
"""



# 12th Mersenne Prime
# (for this application we want a known prime number as close as
# possible to our security level; e.g.  desired security level of 128
# bits -- too large and all the ciphertext is large; too small and
# security is compromised)
#_PRIME = 257
# 13th Mersenne Prime is 2**521 - 1

_RINT = functools.partial(random.SystemRandom().randint, 0)

def _eval_at(poly, x, prime):
    """Evaluates polynomial (coefficient tuple) at x, used to generate a
    shamir pool in make_random_shares below.
    """
    accum = 0
    for coeff in reversed(poly):
        accum *= x
        accum += coeff
        accum %= prime
    return accum

def make_random_shares(secret_key,z_a1_coef,minimum, shares, prime=_PRIME):
    """
    Generates a random shamir pool, returns the secret and the share
    points.
    """
    if minimum > shares:
        raise ValueError("Pool secret would be irrecoverable.")
        
    #qikoo edit- added our secret here     
    poly = []
    
    poly.append(secret_key)
    poly.append(z_a1_coef)
    for i in range(minimum-2):
         poly.append(_RINT(prime - 1))
    #poly = coef_list.reverse()
    #poly.append(secret_key)
    #print(type(poly))
    
    points = [(i, _eval_at(poly, i, prime))
              for i in range(1, shares + 1)]
    return points

def _extended_gcd(a, b):
    """
    Division in integers modulus p means finding the inverse of the
    denominator modulo p and then multiplying the numerator by this
    inverse (Note: inverse of A is B such that A*B % p == 1) this can
    be computed via extended Euclidean algorithm
    http://en.wikipedia.org/wiki/Modular_multiplicative_inverse#Computation
    """
    x = 0
    last_x = 1
    y = 1
    last_y = 0
    while b != 0:
        quot = a // b
        a, b = b, a % b
        x, last_x = last_x - quot * x, x
        y, last_y = last_y - quot * y, y
    return last_x, last_y

def _divmod(num, den, p):
    """Compute num / den modulo prime p

    To explain what this means, the return value will be such that
    the following is true: den * _divmod(num, den, p) % p == num
    """
    inv, _ = _extended_gcd(den, p)
    return num * inv

def _lagrange_interpolate(x, x_s, y_s, p):
    """
    Find the y-value for the given x, given n (x, y) points;
    k points will define a polynomial of up to kth order.
    """
    k = len(x_s)
    assert k == len(set(x_s)), "points must be distinct"
    def PI(vals):  # upper-case PI -- product of inputs
        accum = 1
        for v in vals:
            accum *= v
        return accum
    nums = []  # avoid inexact division
    dens = []
    for i in range(k):
        others = list(x_s)
        cur = others.pop(i)
        #qikoo edit added numpy polynomial undo ho gya
        nums.append(PI(x - o for o in others))
#         print(nums)
        dens.append(PI(cur - o for o in others))
    den = PI(dens)
    num = sum([_divmod(nums[i] * den * y_s[i] % p, dens[i], p)
               for i in range(k)])
    result =(_divmod(num, den, p) + p) % p
#     with open("filesa.txt","+a") as f:
#         f.write("{}".format(result))
    return result


def recover_secret(x_s,y_s, prime=_PRIME):
    """
    Recover the secret from share points
    (x, y points on the polynomial).
    """
    #if len(shares) < 2:
    #    raise ValueError("need at least two shares")
    #x_s, y_s = zip(*shares)
#     print(type(x_s))
#     return print(x_s)
    return _lagrange_interpolate(0, x_s, y_s, prime)