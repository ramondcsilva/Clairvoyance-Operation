# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 00:01:09 2019

@author: Ramon Silva
"""

import pandas as pd
import pandas as dd
from scipy.spatial import distance

# Leitura de arquivo para criação da base_herois de dados
base_superpower = pd.read_csv('superpoderes.csv')

previsores = base_superpower.iloc[:,1:169].values
previsores = base_superpower.iloc[:,0:169].values


##################################################################
########################## DISTÂNCIA #############################
##################################################################


colunas = [
    'names',
    'distance'
]

base_distancias = dd.DataFrame(columns=colunas, index=range(667))

#usuário faz a escolha do heroi (por indice)
heroi = int(input('heroi escolhido: '))


#é feito um for para calcular a distancia entre todos os super herois e seus super-poderes
#escolhido pelo usuário     
for i in range(0, 667):
         base_distancias.loc[i,"distance"] = distance.hamming([previsores[heroi,:]],[previsores[i,:]])
#Ordena o array em ordem crescente
base_distancias = base_distancias.sort_values(by=['distance'], axis = 0, kind= 'mergesort')


#distance.hamming([previsores[4,[0,1,2, 10, 22, 35, 45, 57, 89, 99, 100, 121, 130]]],[previsores[7,[0,1,2, 10, 22, 35, 45, 57, 89, 99, 100, 121, 130]]])

#FUNCIONA
distance.hamming([previsores[5,1:3]],[previsores[6,1:3]]) #ok 0
distance.jaccard([previsores[5,1:3]],[previsores[6,1:3]]) #ok 0
distance.kulsinski([previsores[5,1:3]],[previsores[6,1:3]]) #ok 1
distance.rogerstanimoto([previsores[5,1:3]],[previsores[6,1:3]]) #ok 0
distance.russellrao([previsores[5,1:3]],[previsores[6,1:3]]) #ok 1
distance.sokalmichener([previsores[5,1:3]],[previsores[6,1:3]]) #ok 0

#NÃO FUNCIONA
distance.dice([previsores[5,0:2]],[previsores[6,0:2]])
distance.chebyshev([previsores[5,0:2]],[previsores[6,0:2]])
distance.sokalsneath([previsores[5,0:2]],[previsores[6,0:2]])
distance.yule([previsores[5,0:2]],[previsores[6,0:2]])