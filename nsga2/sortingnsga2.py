# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:08:18 2022

@author: user
"""
import numpy as np
import math
def sortList(aList, order='ascending'):
    '''
        Sorting each individuals by their 
        Acending order sorting (lowesr value first) and gradualy increasing
        reutrns a sorted list and sorted index
    '''
    temp = [val for val in aList]
    sorted_list = []
    sorted_index = []
    if order == 'ascending':
        while(len(sorted_list)!=len(temp)):
            index = temp.index(min(temp))
            value = temp[index]
            if value in aList:
                sorted_list.append(value)
                sorted_index.append(index)
            temp[index] = math.inf # Initilize min to infinit to avoid computing it
    else:
        while(len(sorted_list)!=len(temp)):
            index = temp.index(max(temp))
            value = temp[index]
            if value in aList:
                sorted_list.append(value)
                sorted_index.append(index)
            temp[index] = -math.inf # Initilize min to negative infinit to avoid computing it
        
    return sorted_list, sorted_index
#%%
#POP = mPopulation
#Front = mF

def sortingNSGA2(POP):
    # perfrom the sorting
    crowding_dist = []
    for pop in POP:
        crowding_dist.append(pop.mCrowdingDistance)
    #sort in decending order
    _, s_cd_ind = sortList(crowding_dist, 'decending')
    
    cPOP = []
    rank = []
    for i in range(len(POP)):
        cPOP.append(POP[s_cd_ind[i]])
        rank.append(cPOP[i].mRank)

    # sort in addending order
    _, s_rank_ind = sortList(rank)    
    rPOP = []
    rank = []
    for i in range(len(POP)):
        rPOP.append(cPOP[s_rank_ind[i]])
        rank.append(rPOP[i].mRank)
        
    maxRank = np.max(rank)
    newFront = []
    if maxRank == 0:
        newFront.append([index for index in range(len(rank)) if rank[index] == 0])
    else:
        for i in range(maxRank):
            newFront.append([index for index in range(len(rank)) if rank[index] == i])
    
    return rPOP, newFront

