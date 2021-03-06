# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 19:49:25 2019

@author: Sanjay-Sir
"""

import pandas as pd
import numpy as np
from sklearn import tree

# [Height, Weight, ShoeSize]
X = [[181,80,44], [177, 70, 43], [160, 60, 38], [154,54,37], 
	 [166,65,40], [190, 90, 47], [175, 64, 39], [177,70,40],
	 [159,60,40], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'female', 'female', 'female', 'male', 'male',
	  'male', 'female', 'male', 'female', 'male']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

prediction = clf.predict([[190, 85, 40]])
print (prediction)