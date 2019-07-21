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
nomes = base_superpower.iloc[:,0].values
# previsores = base_superpower.iloc[:,0:169].values
# visualizar = pd.DataFrame(nomes)
##################################################################
########################## DISTÂNCIA #############################
##################################################################
'''
#FUNCIONA
distance.hamming([previsores[5,0:2]],[previsores[6,0:2]]) #ok
distance.jaccard([previsores[5,0:2]],[previsores[6,0:2]]) #ok
distance.kulsinski([previsores[5,0:2]],[previsores[6,0:2]]) #ok
distance.rogerstanimoto([previsores[5,0:2]],[previsores[6,0:2]]) #ok
distance.russellrao([previsores[5,0:2]],[previsores[6,0:2]]) #ok
distance.sokalmichener([previsores[5,0:2]],[previsores[6,0:2]]) #ok
'''

##################################################################
################### EXEMPLO DE BUSCA #############################
##################################################################

#distance.hamming([previsores[4,[0,1,2, 10, 22, 35, 45, 57, 89, 99, 100, 121, 130]]],[previsores[7,[0,1,2, 10, 22, 35, 45, 57, 89, 99, 100, 121, 130]]])
    
#usuário faz a escolha do heroi (por indice)
heroi = str(input('heroi escolhido: '))

# Encontra indice do Heroi pesquisado
heroi, = np.where(nomes == heroi)
print(heroi)
# nomes.Index
#um array é instanciado para guardar todos os valores de distancia calculados
valor_distancias = np.zeros((667,2), dtype=np.double)

#é feito um for para calcular a distancia entre todos os super herois e seus super-poderes
#escolhido pelo usuário
for i in range(0, 667):
        #valor_distancias[i,0] = distance.hamming([previsores[4,[0,1,2, 10, 22, 35, 45, 57, 89, 99, 100,
         #               121, 130]]],[previsores[i,[0,1,2, 10, 22, 35, 45, 57, 89, 99, 100, 121, 130]]])
     valor_distancias[i,1] = distance.hamming([previsores[heroi,:]],[previsores[i,:]])
     valor_distancias[i,0] = i
#help(valor_distancias.sort) 
#Ordena o array em ordem crescente
valor_distancias = pd.DataFrame(valor_distancias).sort_values(by=1)         
# valor_distancias[:,1].sort(axis=0)
# Guarda os 10 herois com menores distancias
result = valor_distancias.iloc[1:11,0:2]
# result = result.iloc[1:11,0:2]
        
'''
#NÃO FUNCIONA
distance.dice([previsores[5,0:2]],[previsores[6,0:2]])
distance.chebyshev([previsores[5,0:2]],[previsores[6,0:2]])
distance.sokalsneath([previsores[5,0:2]],[previsores[6,0:2]])
distance.yule([previsores[5,0:2]],[previsores[6,0:2]])
'''