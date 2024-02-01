# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 17:27:54 2024

@author: omers
"""

'''
eksik verileri (sayısal veriler)
verinin bulunduğu kolonun ortalaması alınarak 
eksik verilerin doldurulması işlemi
'''



#kütüphaneler
import pandas as pd 
import numpy as np   
import matplotlib.pyplot as plt  



veriler = pd.read_csv('eksikveriler.csv')

print(veriler)

# eksik veriler

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values = np.nan, strategy='mean')

yas = veriler.iloc[:,1:4].values
print(yas)

imputer = imputer.fit(yas[:,1:4])
yas[:,1:4] = imputer.transform(yas[:,1:4])
print(yas)

