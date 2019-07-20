# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 11:20:05 2019
@author: Ramon Silva, Adlla Katarine, Daniel Alves
"""

###################################################################
########################## TRATAMENTO #############################
###################################################################

import pandas as pd
# Leitura de arquivo para criação da base_herois de dados
base_herois = pd.read_csv('herois.csv')
base_herois_superpower = pd.read_csv('superpoderes.csv')

# Tratamento de Peso Negativo
base_herois.loc[base_herois.Weight < 0, 'Weight'] = 0
base_herois.loc[base_herois.Weight == 0, 'Weight'] = int(base_herois['Weight'].mean())

# Tratamento de Altura Negativo e substitui pela média
base_herois.loc[base_herois.Height < 0, 'Height'] = 0
base_herois.loc[base_herois.Height == 0, 'Height'] = int(base_herois['Height'].mean())

# Mescla base de dados 
result = base_herois.merge(base_herois_superpower, left_on ='name', right_on='hero_names', how='outer')
# Exclui atributo do nome de herois que estava duplicado
result.drop("hero_names",1,inplace=True)
# result.drop("Alignment",1,inplace=True)

# Apaga os heróis duplicados
result = result.drop(50)
result = result.drop(62)
result = result.drop(69)
result = result.drop(115)
result = result.drop(156)
result = result.drop(259)
result = result.drop(289)
result = result.drop(290)
result = result.drop(481)
result = result.drop(617)
result = result.drop(696)

# base_herois.loc[pd.isnull(base_herois['Weight'])]

# Cria atributo para previsao de dados, excluindo herois sem caracteristicas
previsores = result.iloc[0:734,2:178].values

# Tratando valores 'nan' da base de dados
import numpy as np 
# Cria uma classe SimpleImputer para pre-processamento, 
# representando entrada de dados
from sklearn.impute import SimpleImputer
# imputer recebe a classe que tratar dados nulos, 
# preenchendo com os mais frequentes
imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
# Preenchendo valores vagos com os mais frequentes
# imputer faz as estatiscas sobre o atributo Previsores
imputer = imputer.fit(previsores[:,:]) 
# Atribui as modificação de valores nulos, a mesma variavel
previsores[:,:] = imputer.fit_transform(previsores[:,:])

# Classe para preencher dados vagos
imputer = SimpleImputer(missing_values = '-', strategy='most_frequent')
# imputer faz as estatiscas sobre o atributo Previsores
imputer = imputer.fit(previsores[:,:]) 
# Atribui as modificação de valores nulos, a mesma variavel
previsores[:,:] = imputer.fit_transform(previsores[:,:])

# Transforma Objeto em DATAFRAME para melhor visualização
result = pd.DataFrame(previsores)
guarda = result

# Cria classe para classficação
classe = result.iloc[:,7].values             # 52% Alingment
matriz_accuracy = [0,1,2,3,4]        
for i in range(0,5):
    result = guarda    
    if  (i==1):
        classe = result.iloc[:,10].values    # 76# Cura 
        result = result.drop(columns=10)
    elif(i==2):
        classe = result.iloc[:,17].values    # 76% Voar
        result = result.drop(columns=17)
    elif(i==3):
        classe = result.iloc[:,26].values    # 77% Força
        result = result.drop(columns=26)
    elif(i==4):
        classe = result.iloc[:,46].values
        result = result.drop(columns=46)     # 87% Teleporte
    else:        
        result = result.drop(columns=7)

    # Retorna a modificação
    previsores = result.iloc[:,:].values
###################################################################
########################## PREDITORES #############################
###################################################################
    from sklearn.preprocessing import LabelEncoder
    previsores[:, 0] = LabelEncoder().fit_transform(previsores[:, 0])
    previsores[:, 1] = LabelEncoder().fit_transform(previsores[:, 1])
    previsores[:, 2] = LabelEncoder().fit_transform(previsores[:, 2])
    previsores[:, 3] = LabelEncoder().fit_transform(previsores[:, 3])
    previsores[:, 5] = LabelEncoder().fit_transform(previsores[:, 5])
    previsores[:, 6] = LabelEncoder().fit_transform(previsores[:, 6])
    if(i==0):
        classe = LabelEncoder().fit_transform(classe)
    else:
        previsores[:, 7] = LabelEncoder().fit_transform(previsores[:, 7])
        
    previsores=previsores.astype('int')
    classe=classe.astype('int')
    # Função do pacote sklearn que divide automaticamente dados teste e dados de treinamento
    from sklearn.model_selection import train_test_split
    # Criando variaveis para treinamento e teste, usando o metodo de divisao dos dados
    # Usou-se 25%(test_size = 0.25) como quantidade de atributos para teste e o restante para treinamento
    previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.15, random_state=0)

    # Treinamento a partir de uma Arvore de Decisao, com o criterio de Entropia, unico teste
    from sklearn.tree import DecisionTreeClassifier
    classificador = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
    classificador.fit(previsores_treinamento, classe_treinamento)
    previsoes = classificador.predict(previsores_teste)
    
    from sklearn.metrics import accuracy_score#, confusion_matrix
    # Compara dados de dois atributos retornando o percentual de igualdade deles
    # classe_teste = classe_teste.astype('int')
    matriz_accuracy[i] = accuracy_score(classe_teste, previsoes)
        
    # Cria uma matriz para comparação de dados dos dois atributos
    # matriz = confusion_matrix(classe_teste, previsoes)