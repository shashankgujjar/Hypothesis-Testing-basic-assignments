# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 12:05:00 2020

@author: user
"""

import pandas as pd
import scipy 
from scipy import stats
import statsmodels.api as sm

cutlet=pd.read_csv("E:\Data\Assignments\i made\hypothesis testing\Cutlets.csv")
cutlet
cutlet.columns


##########Normality Test ############
print(stats.shapiro(cutlet.Unit_A))

print(stats.shapiro(cutlet.Unit_B))

#################### Variance Test #############
scipy.stats.levene(cutlet.Unit_A, cutlet.Unit_B)

######## 2 Sample T test ################
scipy.stats.ttest_ind(cutlet.Unit_A,cutlet.Unit_B)
