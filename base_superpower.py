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
# visualizar = pd.DataFrame(nomes)

##################################################################
################### EXEMPLO DE BUSCA #############################
##################################################################

#Listas criados para facilitar o checkbox na interface gráfica
names = base_superpower["hero_names"] #Lista com o nome de todos os heróis

#Lista com todas as distâncias que podem ser escolhidas pelo usuário
distancia_type = ["Distância de Hamming", "Distância de Jaccard", "Distância de Kulsinski", 
                  "Distância de Rogerstanimoto", "Distância de Russellrao", "Distância de Sokalmichener"]

superpower = base_superpower.columns[1:] #Lista de todos os super-poderes

escolha_n = int(input('Escolha a quantidade de superpower que deseja calcular:')) 
escolha_sp = [] #Lista com os indices dos super-poderes escolhidos
ss = [] #Lista com o nome dos super-poderes escolhidos
for i in range(0,escolha_n):
    print(f"Escolha {(i+1)}: ")
    escolha_sp.append(int(input()))
    ss.append(superpower[escolha_sp[i]])
    
#É criado uma base de dados com todos os super-poderes(escolhidos pelo usuário) dos heróis
base_distancias = pd.DataFrame(columns=ss, index=range(667))

#Informações sobre os super-poderes é passado para a "base_distancias"
for i in range(0,len(ss)):
    base_distancias.iloc[:,i] = base_superpower.loc[:, str(superpower[escolha_sp[i]])]
    
base_distancias = base_distancias.iloc[:,:].values

#usuário faz a escolha do heroi (por indice)
heroi = str(input('Heroi escolhido: '))

# Encontra indice do Heroi pesquisado
heroi, = np.where(nomes == heroi)
print(heroi)
# nomes.Index

#um array é instanciado para guardar todos os valores de distancia calculados
valor_distancias = np.zeros((667,2), dtype=np.double)

for i in range(0,len(distancia_type)):
    print(f"{i} - {distancia_type[i]}")
escolha_distancia = input()
#é feito um for para calcular a distancia entre todos os super herois e seus super-poderes
#escolhido pelo usuário 
if(escolha_distancia == 0):
    ################### DISTÂNCIA DE HAMMING #############################
    for i in range(0, 667):
        if(i != heroi):
            valor_distancias[i,1] = distance.hamming([base_distancias[heroi,:]],[base_distancias[i,:]])
            valor_distancias[i,0] = i
        
elif(escolha_distancia == 1):
    ################### DISTÂNCIA DE JACCARD #############################
    for i in range(0, 667):
        if(i != heroi):
            valor_distancias[i,1] = distance.jaccard([base_distancias[heroi,:]],[base_distancias[i,:]])
            valor_distancias[i,0] = i

elif(escolha_distancia == 2):
    ################### DISTÂNCIA DE ROGERSTANIMOTO #############################
    for i in range(0, 667):
        if(i != heroi):
            valor_distancias[i,1] = distance.rogerstanimoto([base_distancias[heroi,:]],[base_distancias[i,:]])
            valor_distancias[i,0] = i
            
elif(escolha_distancia == 3):
    ################### DISTÂNCIA DE KULSINSKI #############################
    for i in range(0, 667):
        if(i != heroi):
            valor_distancias[i,1] = distance.kulsinski([base_distancias[heroi,:]],[base_distancias[i,:]])
            valor_distancias[i,0] = i
            
elif(escolha_distancia == 4):
    ################### DISTÂNCIA DE RUSSELLRAO #############################
    for i in range(0, 667):
        if(i != heroi):
            valor_distancias[i,1] = distance.russellrao([base_distancias[heroi,:]],[base_distancias[i,:]])
            valor_distancias[i,0] = i
'''             
else:
    ################### DISTÂNCIA DE SOKALMICHENER #############################
    for i in range(0, 667):
        if(i != heroi):
            valor_distancias[i,1] = distance.sokalmichener([base_distancias[heroi,:]],[base_distancias[i,:]])
            valor_distancias[i,0] = i
'''             
print(escolha_distancia)
#Ordena o array em ordem crescente
valor_distancias = pd.DataFrame(valor_distancias).sort_values(by=1)         

# Guarda os 10 herois com menores distancias
result = valor_distancias.iloc[1:11,0:2]
for i in range(0,10):
    numero = valor_distancias.iloc[i+1,0].astype('int')
    result.iloc[i,0] = base_superpower.iloc[numero,0] 