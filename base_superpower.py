# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 00:01:09 2019

@author: Ramon Silva
"""

import pandas as pd
# Leitura de arquivo para criação da base_herois de dados
base_superpower = pd.read_csv('superpoderes.csv')

previsores = base_superpower.iloc[:,1:169].values

##################################################################
########################## DISTÂNCIA #############################
##################################################################

# CÁLCULO DA DISTÂNCIA DE HAMMING
from scipy.spatial import distance
distance.hamming([previsores[0,:]],[previsores[1,:]])
distance.hamming([previsores[0,0:2]],[previsores[96,0:2]])
distance.hamming([previsores[5,0:2]],[previsores[6,0:2]])

distance.jaccard([previsores[5,0:2]],[previsores[6,0:2]])