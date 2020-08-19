# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 12:45:09 2020

@author: user
"""

import pandas as pd 
import numpy as np 

COF = pd.read_csv("E:\Data\Assignments\i made\hypothesis testing\Costomer+OrderForm.csv") 



################Chi-Square Test ################

import scipy 
from scipy import stats 

count = pd.crosstab([COF.Phillippines,COF.Indonesia],[COF.Malta,COF.India]) 
count 


Chisquares_results = scipy.stats.chi2_contingency(count) 
Chisquares_results
