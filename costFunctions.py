# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 12:00:05 2022

@author: user
"""
import math
import numpy as np

def costFunction(x, problem = 'test'):
    
    if problem == 'test':
        return test(x)
    if problem == 'kursawe':
        return kursawe(x)
    if problem == 'sch':
        return kursawe(x)
    
    # is not problem defined reurn none
    return None
#%%
#x = [0.5,0.2,0.33,0.1]
def test(x):
    n = len(x)
    y = np.subtract(x,np.divide(1, math.sqrt(n)))
    z =  -np.sum(np.power(y,2))
    f1 = 1 - math.exp(z)
    #print(z1)
    
    y = np.add(x,np.divide(1, math.sqrt(n)))
    z =  -np.sum(np.power(y,2))
    f2 = 1 - math.exp(z)
    
    return [f1, f2]
    

def kursawe(x):
    s = 0
    for i in range(len(x)-1):
        s += -10*math.exp(-0.2*math.sqrt(x[i]**2 + x[i+1]**2))
    f1 = s

    s = 0
    for i in range(len(x)):
        s += abs(x[i])**0.8 + 5*math.sin(x[i]**3)
    f2 = s
    
    return [f1, f2]

def sch(x):
    return [x**2, (x-2)**2]