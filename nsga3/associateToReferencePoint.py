# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 16:20:16 2019

@author: V Ojha
"""

import numpy as np


#pPopulation=  nPopulation
def associateToReferencePoint(pPopulation, pParams):
    '''
        Method for the associating solution to the refernce points
    '''
    
    Zr =  pParams.Zr
    nZr = pParams.nZr
    rho = np.zeros(nZr)
    
    dist = np.zeros((len(pPopulation), nZr))
    
    for i in range(len(pPopulation)):
        for j in range(nZr):
            #print(Zr[0,j])
            #Compute reference line w
            w = np.asanyarray(np.divide(Zr[:,j], np.linalg.norm(Zr[:,j])))
            z = np.asmatrix(pPopulation[i].mNormalizedCost)
            # compute distance between an individual and the reference point
            dist[i,j] = np.linalg.norm(np.subtract(np.transpose(z), np.dot(np.dot(w,z),w)))
        
        dmin = np.min(dist[i,:])
        dminIndex = np.argmin(dist[i,:])
        
        # assign refernce 
        pPopulation[i].mAssociatedRef = dminIndex
        pPopulation[i].mDistanceToAssociatedRef = dmin
        # conting number of reference point assosiation
        rho[dminIndex] = rho[dminIndex] + 1    
    
        
        
    return pPopulation, dist, rho



