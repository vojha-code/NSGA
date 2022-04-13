# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 11:42:21 2019

@author: user
"""

class Individual():
    '''
        An individual in NSGA population
    '''
    mSolution = None
    mCost = None
    mRank = None 
    mDominationSet = None
    mDominatedCount = None
    mNormalizedCost = None
    mAssociatedRef = None 
    mDistanceToAssociatedRef = None
    mCrowdingDistance = None
    
    def __init__(self):
        self.mSolution = None
        self.mCost = [] 
        self.mRank = [] 
        self.mDominationSet = [] 
        self.mDominatedCount = [] 
        self.mNormalizedCost = [] 
        self.mAssociatedRef = [] 
        self.mDistanceToAssociatedRef = []   
        self.mCrowdingDistance = None