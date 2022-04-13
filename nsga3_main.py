# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 09:21:50 2019

@author: V Ojha
"""

# General GA imports

#Imports from NSGA-III functions

from costFunctions import costFunction
from geneticOperators import crossover, mutation
from individual import Individual


from misc import *

from nsga3.params import Params
from nsga3.generateReferencePoints import generateReferencePoints
from nsga3.sortAndSelectPopulation import sortAndSelectPopulation


# Python standard libraries
import copy
import numpy as np
import random
import matplotlib.pyplot as plt
#%% Problem setting
mVar = 50
mMin = -1
mMax = 1

# optimization type minimization and maximization
mOptimization = 'MIN'#  mParams.n_optimization 
mProblem =  'test' # 'kursawe' # 'test' # 'kursawe' # 'test'


# NSGA    Parameter setting
mDivision = 10# mParams.n_division #  number of division/sprade of the points between 0 and 1 for an objective function 
mMaxIt = 50# mParams.n_max_itrations # Maximum Number of Iterations
mPop = 80# mParams.n_max_population # Population Size

pCrossover = 0.5 #  mParams.n_prob_crossover # Crossover Percentage
mCrossover = 2*round(pCrossover*mPop/2) # Number of Parnets (Offsprings)
pMutation = 0.5 # 1.0 - pCrossover # Mutation Percentage
mMutation = round(pMutation*mPop) # Number of Mutants


nMu = 0.02 # Mutation Rate
nSigma = 0.1*(mMax - mMin) # Mutation Step Size

mBestIndividual = Individual()

gPerformanceRecord = []
#%% Initilization
            
# Creating initial populations
mPopulation = [Individual() for i in range(0, mPop)] # Empty population

#%% Generating population fron a unifiorm distribution
for pop in mPopulation:
    n_sol = [np.random.uniform(-1, 1) for i in range(mVar)]
    pop.mSolution = n_sol
    pop.mCost = costFunction(n_sol, mProblem)

#%%
# Generating initial refernce points systmaticaly
mObj = len(mPopulation[0].mCost)
mZr = generateReferencePoints(mObj, mDivision) #  tested OK      
# collecting and initilizing reference points values 
cParams = Params(mPop, mZr, mZr.shape[1], [], [], [])

#%% 1c. Sortining of the population according to their approximation error/ classifcation error
#mPopulation = [mPopulation[i] for i in sort_by_values([i for i in range(0,len(mPopulation))], [pop.mCost[0] for pop  in mPopulation])]
   
#setBest(mPopulation[0]) 
#gPerformanceRecord.append(costFunction(mBestIndividual.mSolution))

mPopulation, mF, cParams = sortAndSelectPopulation(mPopulation, cParams, mOptimization)

#%% Loop through genetic process
fig = plt.figure()

y1 = [mPopulation[i].mCost[0] for i in range(mPop) if i in mF[0]]
y2 = [mPopulation[i].mCost[1] for i in range(mPop) if i in mF[0]]
plt.scatter(y1,y2, marker='+')
#plt.xlim(0, 1)
#plt.ylim(0, 1)
plt.xlabel('Objective 1')
plt.ylabel('Objective 2')
plt.show()

for itr in range(mMaxIt):
    print('iteration', itr)
    #STEP 2: Generating offsprings ---------------------------------------------------------------------
    # 2a. copy population in to itrPopulation
    itrPopulation = mPopulation # current population
    # CROSSOVER
    countCorssover, countMutation = 0, 0            
    while(countCorssover < mCrossover/2):
        countCorssover = countCorssover + 1
        # DO Crossover
        p1_idx = random.randint(0, mPop-1)
        p2_idx = random.randint(0, mPop-1)
        
        p1 = copy.deepcopy(mPopulation[p1_idx]) 
        p2 = copy.deepcopy(mPopulation[p2_idx]) 
        
        c1, c2 = crossover(p1.mSolution, p2.mSolution)
        
        ind1 = Individual()
        ind1.mSolution = c1
        ind1.mCost = costFunction(c1, mProblem)
        itrPopulation.append(ind1)
        
        ind2 = Individual()
        ind2.mSolution = c2
        ind2.mCost = costFunction(c2, mProblem)               
        itrPopulation.append(ind2)
        
    # MUTATION OPEARATION
    while(countMutation < mMutation):
        countMutation = countMutation + 1
        # DO mutation
        p_idx = random.randint(0, mPop-1)
        p = copy.deepcopy(mPopulation[p_idx]) 
        
        c = mutation(p.mSolution, nMu, nSigma)
        
        ind = Individual()
        ind.mSolution = c
        ind.mCost = costFunction(c, mProblem)
        itrPopulation.append(ind)
        

                    
    mPopulation = []
    #Generating offsprings END---------------------------------------------------------------------
    # SAVE - all populaion and for post processing
    mPopulation, mF, cParams = sortAndSelectPopulation(itrPopulation, cParams, mOptimization)
    
    #for pop in mPopulation:
    #    print(pop.mRank+1)    
    #for f in nFront:
    #    print(np.add(f,1))
        
    # Iteration Information
    print(mF)
    y1 = [mPopulation[i].mCost[0] for i in range(mPop) if i in mF[0]]
    y2 = [mPopulation[i].mCost[1] for i in range(mPop) if i in mF[0]]
    plt.scatter(y1,y2, marker='o')
    #plt.xlim(0, 1)
    #plt.ylim(0, 1)
    #plt.show()
    
    
print(mF)
y1 = [mPopulation[i].mCost[0] for i in range(mPop) if i in mF[0]]
y2 = [mPopulation[i].mCost[1] for i in range(mPop) if i in mF[0]]
plt.scatter(y1,y2, marker='*')
#plt.xlim(0, 1)
#plt.ylim(0, 1)
plt.xlabel('Objective 1')
plt.ylabel('Objective 2')
plt.show()
#%%     
def setBest(pIndividual, itr = 0):
    '''
        Compare the current individial tree with the best Tree found so far
        arges:
            param:  pIndividual  an individual tree
    '''
    printBest = False
    if mBestIndividual.mSolution  == None:
        mBestIndividual.mSolution = pIndividual.mSolution
        mBestIndividual.mCost = pIndividual.mCost
        printBest = True
    
    if mBestIndividual.mCost[0] > pIndividual.mCost[0]:
        mBestIndividual.mSolution = pIndividual.mSolution
        mBestIndividual.mCost = pIndividual.mCost
        printBest = True
    
    
    if printBest:
        print('GP Itr', itr, 'best sol [',  round(mBestIndividual.mCost[0], 5), round(mBestIndividual.mCost[1], 5), '] this is new best')
    
    return printBest

#%%## Test Population
# import scipy.io
# popMat = scipy.io.loadmat('pop.mat')
# for el in popMat:
#     if el == 'pop':
#         print(el)
#         for i in range(len(popMat[el])):
#             mPopulation[i].mSolution = popMat['pop'][i][0][0][0].tolist()
#             mPopulation[i].mCost = popMat['pop'][i][0][1].flatten().tolist()



# cech_idx = 1
# mPopulation[cech_idx].mSolution
# mPopulation[cech_idx].mCost
# costFunction(mPopulation[cech_idx].mSolution)

# ## Test Generation Population
# popMat = scipy.io.loadmat('popG.mat')
# for el in popMat:
#     if el == 'pop':
#         print(el)
#         for i in range(len(popMat[el])):
#             if popMat['pop'][i][0][2].tolist() == []:
#                 ind = Individual()
#                 ind.mSolution = popMat['pop'][i][0][0][0].tolist()
#                 ind.mCost = popMat['pop'][i][0][1].flatten().tolist()
#                 itrPopulation.append(ind)
        
            