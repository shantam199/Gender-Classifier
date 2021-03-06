# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 19:46:31 2019

@author: Sanjay-Sir
"""

import pandas as pd
import numpy as np
from sklearn.svm import SVC

# [Height, Weight, ShoeSize]
X = [[181,80,44], [177, 70, 43], [160, 60, 38], [154,54,37], 
	 [166,65,40], [190, 90, 47], [175, 64, 39], [177,70,40],
	 [159,60,40], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'female', 'female', 'female', 'male', 'male',
	  'female', 'female', 'male', 'female', 'male']

clf = SVC()
clf = clf.fit(X,Y)

prediction = clf.predict([[175, 65, 37]])

print (prediction)