# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 11:20:05 2019
@author: Ramon Silva, Adlla Katarine, Daniel Alves
"""

###################################################################
########################## TRATAMENTO #############################
###################################################################

import pandas as pd
import numpy as np 

#import scikitplot as skplt
#import matplotlib.pyplot as plt
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

#Personagens com nomes iguais(não necessariamente duplicados) tiveram seus nomes alterados
result.loc[23, 'name'] = "Angel II"
result.loc[48, 'name'] = "Atlas II"
result.loc[97, 'name'] = "Black Canary II"
result.loc[623, 'name'] = "Spider-Man II"
result.loc[624, 'name'] = "Spider-Man III"
result.loc[674, 'name'] = "Toxin II"

# base_herois.loc[pd.isnull(base_herois['Weight'])]

# Cria atributo para previsao de dados, excluindo herois sem caracteristicas
previsores = result.iloc[0:734,2:178].values

# Tratando valores 'nan' da base de dados 
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
imputer = SimpleImputer(missing_values = '-', strategy='constant', fill_value='neutral')
# imputer faz as estatiscas sobre o atributo Previsores
imputer = imputer.fit(previsores[:,7].reshape(1,-1)) 
# Atribui as modificação de valores nulos, a mesma variavel
previsores[:,7] = imputer.fit_transform(previsores[:,7].reshape(1,-1))

imputer = SimpleImputer(missing_values='-', strategy='most_frequent')
# imputer faz as estatiscas sobre o atributo Previsores
imputer = imputer.fit(previsores[:,:]) 
# Atribui as modificação de valores nulos, a mesma variavel
previsores[:,:] = imputer.fit_transform(previsores[:,:])


# Transforma Objeto em DATAFRAME para melhor visualização
result = pd.DataFrame(previsores)
guarda = result

# Cria classe para classficação
classe = result.iloc[:,7].values             # 52% Alingment features = 20, depth = 21 66%

# accuracy_ndepth = result.iloc[0:168,0]
# accuracy_nfeatures = result.iloc[0:168,0]
accuracy = [0,1,2,3,4]  
for i in range(0,5):
    result = guarda  
    if  (i==1):
        classe = result.iloc[:,10].values    # 76% Cura features = 70, depth = 5 %97 - Ocorre 100% de accuracy quando +100 features
        result = result.drop(columns=10)
    elif(i==2):
        classe = result.iloc[:,17].values    # 76% Voar features = 20, depth = 21 % - Ocorre 100% de accuracy quando +90 features - Default 100%
        result = result.drop(columns=17)
    elif(i==3):
        classe = result.iloc[:,26].values    # 77% Força features = 20, depth = 21 %
        result = result.drop(columns=26)
    elif(i==4):
        classe = result.iloc[:,46].values
        result = result.drop(columns=46)     # 87% Teleporte features = 15, depth = 9 94%
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
    
    previsores = previsores.astype('int')
    classe = classe.astype('int')
    
    # Função do pacote sklearn que divide automaticamente dados teste e dados de treinamento
    from sklearn.model_selection import train_test_split
    # Criando variaveis para treinamento e teste, usando o metodo de divisao dos dados
    # Usou-se 25%(test_size = 0.25) como quantidade de atributos para teste e o restante para treinamento
    previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.33, random_state=0)

    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    # Atribui o escalonamento ao atributo previsores
    previsores_treinamento = scaler.fit_transform(previsores_treinamento)
    previsores_teste = scaler.fit_transform(previsores_teste)
    
#for i in range(0,168):
    # Treinamento a partir de uma Arvore de Decisao, com o criterio de Entropia, unico teste  
    # Hiperparamenters para achar a melhores paramentros para a arvore
    from scipy.stats import randint
    paramenter = {"max_depth": randint(3,10),
                  "min_samples_leaf": randint(1,5),
                  "max_features": randint(5,15),
                  "criterion": ["gini","entropy"]}  
    
    from sklearn.tree import DecisionTreeClassifier
    tree = DecisionTreeClassifier()
    
    from sklearn.model_selection import RandomizedSearchCV
    classificador = RandomizedSearchCV(tree,paramenter, cv=5)
    
    classificador.fit(previsores_treinamento, classe_treinamento)
    
    print("Tuned: {}".format(classificador.best_params_))
    print("Best score is {}".format(classificador.best_score_))
    
    previsoes = classificador.predict(previsores_teste)

    # Usando o Cross_validate para avaliar o classificador
    from sklearn.model_selection import cross_validate
    scoring = ['precision_macro', 'recall_macro']
    scores_cv = cross_validate(classificador, 
                            previsores, 
                            classe,
                            scoring=scoring, 
                            cv=10)
    scores_cv['test_precision_macro']

    from sklearn.metrics import accuracy_score, confusion_matrix
    # Compara dados de dois atributos retornando o percentual de igualdade deles
    # classe_teste = classe_teste.astype('int')
    # accuracy_nfeatures[i] = accuracy_score(classe_teste, previsoes)
    # accuracy_ndepth[i] = accuracy_score(classe_teste, previsoes)
    accuracy[i] = accuracy_score(classe_teste, previsoes) 
    # Cria uma matriz para comparação de dados dos dois atributos
    matriz = confusion_matrix(classe_teste, previsoes)