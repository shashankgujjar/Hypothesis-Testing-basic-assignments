# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:52:25 2020

@author: user
"""

import pandas as pd
import scipy 
from scipy import stats
import statsmodels.api as sm

#from plotly.tools import FigureFactory as FF

############2 sample T Test(Marketing Strategy) ##################

LabTat = pd.read_csv("E:\Data\Assignments\i made\hypothesis testing\LabTAT.csv")
LabTat
LabTat.columns

##########Normality Test ############

print(stats.shapiro(LabTat.Lab1))    #Shapiro Test

print(stats.shapiro(LabTat.Lab2)) 

print(stats.shapiro(LabTat.Lab3)) 

print(stats.shapiro(LabTat.Lab4)) 

help(stats.shapiro)

#################### Variance Test #############
scipy.stats.levene(LabTat.Lab1, LabTat.Lab2, LabTat.Lab3, LabTat.Lab4)


#################### One Way ANOVA Test #############

from statsmodels.formula.api import ols 
mod=ols('Lab1~Lab2+Lab3+Lab4',data= LabTat).fit() 
table=sm.stats.anova_lm(mod,type=2) 
print(table) 






