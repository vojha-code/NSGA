# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 13:31:34 2019

@author: user
"""
#%%
import numpy as np

import scipy.io
popMat = scipy.io.loadmat('pop.mat')

from individual import Individual
from costFunctions import costFunction

# POP = [Individual() for i in range(0, 80)] # Empty population
# for el in popMat:
#     if el == 'pop':
#         print(el)
#         for i in range(len(popMat[el])):
#             POP[i].mSolution = popMat['pop'][i][0][0][0].tolist()
#             POP[i].mCost = popMat['pop'][i][0][1].flatten().tolist()
        

def Dominates(p,q, OPTIMIZATION = 'MIN'):  
    a = np.asarray(p.mCost)
    b = np.asarray(q.mCost)
    #print(a)
    #print(b)
    if(OPTIMIZATION.upper() == 'MIN' or 'MIN' in OPTIMIZATION.upper()):
         return np.all(a<=b) and np.any(a<b)
    else:
         return np.all(a>=b) and np.any(a>b)
    
        #default return
    return np.all(a<=b) and np.any(a<b)
#%%    

def nonDominatedSorting(POP, OPTIMIZATION = 'MIN'):
    '''
        Compute fast non dominated sorting: 
            Deb K, Pratap A, Agarwal S, et al. 
            A fast and elitist multiobjective genetic algorithm: NSGA-II. 
            IEEE transactions on Evolutionary Computation, 2002, 6(2): 182-197.
        args:
            param:    p_pop             population
            param:    OPTIMIZATION      takes 'MIN' or MAX
        return:  nondominated sorted sets - font 0 to ...
    '''    
    #%%
    nPop = len(POP) 
    for i in range(nPop):   
        POP[i].mDominationSet = []
        POP[i].mDominatedCount = 0
        
    Front = [[]]

    # for each p in POP
    for i in range(nPop):   
        for j in range(i+1, nPop):# for each q in POP 
            p = POP[i]
            q = POP[j]
        
            if Dominates(p, q, OPTIMIZATION):
                #print(i,'p dominates q',i,j)
                p.mDominationSet.append(j)  # Add q to the set of solution dominated by p
                q.mDominatedCount = q.mDominatedCount + 1
                
            if Dominates(q, p, OPTIMIZATION):
                #print(i,'q dominates p',i,j)
                q.mDominationSet.append(i)  # Add p to the set of solution dominated by q
                p.mDominatedCount = p.mDominatedCount + 1                    
                
            POP[i] = p
            POP[j] = q
        #END of j        
        # check if p belongs to first front
        if POP[i].mDominatedCount == 0:
            Front[0].extend([i]) # add all i that is not dominated to font 1
            POP[i].mRank = 0
    #END i

    k = 0 # initilize Front counter
    # while font is not NULL
    while True:
        Q=[]
        for i in Front[k]:
            #print(i)
            p = POP[i]
            for j in p.mDominationSet:
                #print(j)
                q = POP[j]
                q.mDominatedCount = q.mDominatedCount - 1
                if q.mDominatedCount == 0:
                    Q.extend([j])
                    q.mRank = k+1
                #end if
                POP[j] = q
            #end for j
        #end for i
        if Q == []:
            break;
        
        k = k+1
        Front.append(Q)
        
    #del front[len(front)-1]
#%%
    return POP, Front    

        
    