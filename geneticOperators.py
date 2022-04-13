# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 14:53:46 2022

@author: user
"""
import numpy as np
import math
import random 

def crossover(p1, p2):
    
    alpha = np.random.rand(len(p1))

    c1 = np.multiply(alpha,p1) + np.multiply(np.subtract(1,alpha),p2)
    c2 = np.multiply(alpha,p2) + np.multiply(np.subtract(1,alpha),p1)

    return c1.tolist(), c2.tolist()


def mutation(p, mu, sigma):
    
    nVar = len(p)
    
    nMu = math.ceil(mu*nVar)

    mPts = random.sample([i for i in range(len(p))],nMu)
    
    c = [(p[i] + sigma * np.random.randn()) if i in mPts else p[i] for i in range(len(p)) ]
    
    return c
