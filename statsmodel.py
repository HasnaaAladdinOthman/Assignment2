# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 17:56:01 2018

@author: Hasnaa
"""

import statsmodels.api as sm
from sklearn import datasets ## imports datasets from scikit-learn
import pandas as pd
#data2 = datasets.load_boston() ## loads Boston dataset from datasets library 
df = pd.read_csv('train.csv', index_col=0)
df.head()
lm = sm.OLS.from_formula('medv ~ lstat', df)
result = lm.fit()
print (result.summary())