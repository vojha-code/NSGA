# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 14:21:12 2019

@author: user
"""

import numpy as np
import random

from nsga3.normalizePopulation import normalizePopulation    
from nsga3.associateToReferencePoint import associateToReferencePoint
from nonDominatedSorting import nonDominatedSorting



# pPopulation = mPopulation
# pPopulation = itrPopulation
# pParams = cParams

def sortAndSelectPopulation(pPopulation, pParams, pOptimization = 'MIN'):
    '''
        Population sorting and selection method calls
    '''
    nPopulation, nParams = normalizePopulation(pPopulation, pParams)
    
    nPopulation, nFront = nonDominatedSorting(nPopulation, pOptimization)
    
    # ###Test Pop rank and Fronts
    # for pop in nPopulation:
    #     print(pop.mRank+1)    
    # for f in nFront:
    #     print(np.add(f,1))
    
    if len(nPopulation) == nParams.nPop:
        return nPopulation, nFront, nParams
    
    
    nPopulation, dist, rho = associateToReferencePoint(nPopulation, nParams)
    
    ##Test
    # for pop in nPopulation:
    #     print(pop.mAssociatedRef+1) 
    # for pop in nPopulation:
    #     print(pop.mDistanceToAssociatedRef) 
    
    newPopulation = []
    for i in range(len(nFront)):
        if len(newPopulation) + len(nFront[i]) > nParams.nPop:
            nLastFront = nFront[i]
            break
        #Extent newpopulation by adding all population in Front i
        newPopulation.extend([nPopulation[popIndex] for popIndex in nFront[i]])
        

    # Adding individuals from last front to the population
    while True:
        
        rhoMinIndex =  np.argmin(rho)
        associtedFromLastFront = []
        for popIndex in nLastFront:
            if nPopulation[popIndex].mAssociatedRef == rhoMinIndex:
                associtedFromLastFront.append(popIndex)

            
        if not associtedFromLastFront:
            rho[rhoMinIndex] = np.Inf
            continue
        
        if rho[rhoMinIndex] == 0:
            distToRhoMinIndexList = [dist[inexInLastFront][rhoMinIndex] for inexInLastFront in associtedFromLastFront]
            newMemberIndex =  np.argmin(distToRhoMinIndexList)
        else:
            newMemberIndex = random.randint(0,len(associtedFromLastFront)-1)
            
        memberToAdd = associtedFromLastFront[newMemberIndex]
        
        if memberToAdd in nLastFront:
            nLastFront.remove(memberToAdd)
        
        newPopulation.append(nPopulation[memberToAdd])
        
        rho[rhoMinIndex] = rho[rhoMinIndex] + 1
        
        if len(newPopulation) >= nParams.nPop:
            break
    # End while
    
       
    newPopulation, newFront = nonDominatedSorting(newPopulation, pOptimization)
    
    return newPopulation, newFront, nParams
    


