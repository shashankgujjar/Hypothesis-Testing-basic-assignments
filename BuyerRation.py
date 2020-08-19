# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:20:38 2020

@author: user
"""

import calendar as c
c.isleap(2020)


import time as t
t.sleep(0)


import pandas as pd 
import numpy as np 
from scipy import stats 


Buyerdata= pd.read_csv("E:\Data\Assignments\i made\hypothesis testing\BuyerRatio.csv")

male=[50,142,131,70] 
female=[435,1523,1356,750] 

buyr=np.array([male,female]) 
buyr

################Chi-Square Test ################

chi2_stat,p_val,dof,ex=stats.chi2_contingency(buyr) 
print(chi2_stat) 	
print(p_val) 
print(dof) 
print(ex) 
