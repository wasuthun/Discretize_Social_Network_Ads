#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 18:42:24 2019
discretize by EstimatedSalary
@author: johnpaul
"""

import numpy as np
import pandas as pd

dataset = pd.read_csv('/Users/johnpaul/Downloads/Social_Network_Ads.csv')

print(dataset)
X = np.ravel(dataset.iloc[:, 3].values)
def discretize(data, bins):
    split = np.array_split(np.sort(data), bins)
    cutoffs = [x[-1] for x in split]
    cutoffs = cutoffs[:-1]
    discrete = np.digitize(data, cutoffs, right=True)
    return discrete, cutoffs

discrete_data, cutoff = discretize(X, 3)

print(X)
print(discrete_data)
print(cutoff)
