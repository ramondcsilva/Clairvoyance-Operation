# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 00:01:09 2019

@author: Ramon Silva
"""

import pandas as pd
from scipy.spatial import distance

# Leitura de arquivo para criação da base_herois de dados
base_superpower = pd.read_csv('superpoderes.csv')

previsores = base_superpower.iloc[:,1:169].values

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

#NÃO FUNCIONA
distance.dice([previsores[5,0:2]],[previsores[6,0:2]])
distance.chebyshev([previsores[5,0:2]],[previsores[6,0:2]])
distance.sokalsneath([previsores[5,0:2]],[previsores[6,0:2]])
distance.yule([previsores[5,0:2]],[previsores[6,0:2]])