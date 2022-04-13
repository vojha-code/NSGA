# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:48:27 2019

@author: user
"""
import numpy as np
from misc import sort_by_values
import math


#POP =  mPopulation
#Front = mF

#Function to calculate crowding distance
def crowdingDistance(POP, Front):
    '''
        Recieves a population and its a set of nondominated solutions (form front 0 to ...)
        args:
            param:    P              population
            param:    front = I     front  (index of individuals in P) a nondominated sorted front
        
        return: distance
    '''
    #P = population
    nFrontlen = len(Front) # l = |I| , i.e., inds_in_this_font
    nObj = len(POP[0].mCost)
    for i in range(nFrontlen):
        # retrive costs 
        costs = [POP[ind].mCost for ind in Front[i]]        
        
        iFrontLen = len(Front[i])
        distance = [[0 for i in range(nObj)] for i in range(iFrontLen)] # for each i, set I[i]distance = 0
        
        for j in range(nObj):
            #fetch values of the objetcive functions
            values = [cost[j] for cost in costs]
            #sort for values of the objecive m
            s_cost = np.sort(values)
            s_ind = np.argsort(values).tolist()
            
            distance[s_ind[0]][j] = np.Inf
            for k in range(1,iFrontLen-1):
                dist = np.abs(s_cost[k+1] - s_cost[k-1]) / np.abs(s_cost[0] - s_cost[iFrontLen-1])
                
                distance[s_ind[k]][j] = dist
            # end 
            distance[s_ind[iFrontLen-1]][j] = np.Inf
        #end
        for k in range(iFrontLen):
            ind = Front[i][k]
            #print(ind, np.sum(distance[m]))
            POP[ind].mCrowdingDistance = np.sum(distance[k])
            
    return POP


