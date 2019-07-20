# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 00:01:09 2019

@author: Ramon Silva
"""

import pandas as pd
from scipy.spatial import distance
import numpy as np 

# Leitura de arquivo para criação da base_herois de dados
base_superpower = pd.read_csv('superpoderes.csv')

previsores = base_superpower.iloc[:,1:169].values
previsores = base_superpower.iloc[:,0:169].values

##################################################################
########################## DISTÂNCIA #############################
##################################################################

#FUNCIONA
distance.hamming([previsores[5,0:2]],[previsores[6,0:2]]) #ok
distance.jaccard([previsores[5,0:2]],[previsores[6,0:2]]) #ok
distance.kulsinski([previsores[5,0:2]],[previsores[6,0:2]]) #ok
distance.rogerstanimoto([previsores[5,0:2]],[previsores[6,0:2]]) #ok
distance.russellrao([previsores[5,0:2]],[previsores[6,0:2]]) #ok
distance.sokalmichener([previsores[5,0:2]],[previsores[6,0:2]]) #ok

heroi = input('heroi escolhido: ')

poderes = [3, 4, 5, 7]

valor_distancias = np.zeros((667,168), dtype=np.float64)

for i in range(0, 667):
    
    for y in range(0, poderes.index):
        valor_distancias[i,y] = distance.hamming([previsores[i,poderes[y]]],[previsores[i,poderes[y]]])


for y in range(0, poderes.index):
    print(valor_distancias([[0],[y]]))



#NÃO FUNCIONA
distance.dice([previsores[5,0:2]],[previsores[6,0:2]])
distance.chebyshev([previsores[5,0:2]],[previsores[6,0:2]])
distance.sokalsneath([previsores[5,0:2]],[previsores[6,0:2]])
distance.yule([previsores[5,0:2]],[previsores[6,0:2]])