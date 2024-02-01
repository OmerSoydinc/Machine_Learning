# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 16:53:38 2024

@author: omers
"""

#kütüphaneler
# verileri düzgün bir şekilde tutabilmek için
import pandas as pd 
# büyük sayılar ve hesaplamalar              
import numpy as np   
# çizim için kullanılmaktadır.            
import matplotlib.pyplot as plt  

# kod bölümü 

 #veri yükleme
veriler = pd.read_csv('veriler.csv')

print(veriler)
 #veri ön işleme

boy= veriler[['boy']]

print(boy)


boy_kilo = veriler[['boy','kilo']]
print(boy_kilo)