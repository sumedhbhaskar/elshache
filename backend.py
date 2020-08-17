""""
 new backend for encryption app
"""
from __future__ import division
from __future__ import print_function

import math 
import random
import sympy

import functools
from functools import reduce
from random import randint

from numpy import poly1d as Poly
import numpy as np





PRIME = 257
_PRIME = 257




_RINT = functools.partial(random.SystemRandom().randint, 0)

def _eval_at(poly, x, prime):
    """

    evaluate polynomial at x
    
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
            
    poly = []
    
    poly.append(secret_key)
    poly.append(z_a1_coef)
    for i in range(minimum-2):
         poly.append(_RINT(prime - 1))
    
    
    points = [(i, _eval_at(poly, i, prime))
              for i in range(1, shares + 1)]
    return points

def _extended_gcd(a, b):
   
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
    
    inv, _ = _extended_gcd(den, p)
    return num * inv

def _lagrange_interpolate(x, x_s, y_s, p):
    """
    Find the y-value for the given x, given n (x, y) points;
    k points will define a polynomial of up to kth order.
    """
    k = len(x_s)
    assert k == len(set(x_s)), "points must be distinct"
    def PI(vals):  
        accum = 1
        for v in vals:
            accum *= v
        return accum
    nums = []  
    dens = []
    for i in range(k):
        others = list(x_s)
        cur = others.pop(i)
        nums.append(PI(x - o for o in others))
        dens.append(PI(cur - o for o in others))
    den = PI(dens)
    num = sum([_divmod(nums[i] * den * y_s[i] % p, dens[i], p)
               for i in range(k)])
    result =(_divmod(num, den, p) + p) % p

    return result


def recover_secret(x_s,y_s, prime=_PRIME):
    """
    Recover the secret from share points
    (x, y points on the polynomial).
    """
    
    return _lagrange_interpolate(0, x_s, y_s, prime)




class elshache:
    
    @staticmethod
    def findInverse(a,b):
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


    def __init__(self,s,n,t):
        """ 
            values are initialized
        """
        self.secret  = s
        self.total_share = n
        self.min_share = t
        self.randomNumber = random.randint(1,PRIME)
        self.randomNumberInverse,self._ = elshache.findInverse(self.randomNumber,PRIME)
        self.z_a1_coef = self.randomNumber*self.secret%PRIME

        

    def shareConstruction(self):
        return make_random_shares(self.secret,self.z_a1_coef,self.min_share,self.total_share)


class elshache_re:
    
    """
        reconstruction of secrets and creating detection algorithm
    """
    def _extended_gcd(self,a, b):
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

    def _divmod(self,num, den, p):

        inv, _ = _extended_gcd(den, p)
        return num * inv
    
    

    def shareReconstruction(self,x_coef,y_coef,min_share):
        if(len(x_coef)!=len(y_coef) or len(x_coef) < min_share or len(y_coef) < min_share):
            raise Exception("Please recheck you input file. X and Y coef does'nt match.")

        return recover_secret(x_coef,y_coef)

    def shareReconstruction_a1(self,x_coef,y_coef,min_share,randomNumberInverse):
        """
            cheating detection coefficient a1 is extracted here.
        """
        
        if(len(x_coef)!=len(y_coef) or len(x_coef) < min_share or len(y_coef) < min_share):
            raise Exception("Please recheck you input file. X and Y coef doesn't match.")
        
        nums = []
        dems = []
        result_list = []
        result = 0
        
        for i in range(min_share):
            x_list = list(x_coef)
            x_poped = x_list.pop(i)
            
            temp1__ = []
            temp2 = 1            
            
            for j in x_list:
                temp1__.append(j)
                temp2 *= x_poped - j
            temp1_ = Poly(temp1__,True)
            temp1_ = temp1_.c
            temp1 = temp1_[-2]
            
            nums.append(temp1%PRIME)
            a,b=_extended_gcd(temp2,PRIME)
            dems.append(a)
        print(temp1)    
        print(nums)
        print(dems)    
        for i in range(min_share):
            result_list.append(nums[i]*float(dems[i])%PRIME)
        print(result_list)    
        for i in range(min_share):
            result_list[i] = result_list[i]*y_coef[i]%PRIME
        print(result_list)    
        for i in result_list:
            result += i
            
        result = result%PRIME
        print(result)
        return (result*randomNumberInverse)%PRIME
            
        

