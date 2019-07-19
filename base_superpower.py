# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 00:01:09 2019

@author: Ramon Silva
"""

import pandas as pd
# Leitura de arquivo para criação da base_herois de dados
base_superpower = pd.read_csv('superpoderes.csv')

previsores = base_superpower.iloc[:,1:169].values
classe = base_superpower.iloc[:,0:3].values

from sklearn.preprocessing import LabelEncoder
labelencoder_classe = LabelEncoder()
classe = labelencoder_classe.fit_transform(classe[:,0])
































'''
# Função do pacote sklearn que divide automaticamente dados teste e dados de treinamento
from sklearn.model_selection import train_test_split
# Criando variaveis para treinamento e teste, usando o metodo de divisao dos dados
# Usou-se 25%(test_size = 0.25) como quantidade de atributos para teste e o restante para treinamento
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.15, random_state=0)




import numpy as np
from sklearn.multioutput import MultiOutputClassifier
from sklearn.tree import DecisionTreeClassifier

previsores_treinamento = np.array(previsores_treinamento)
classe_treinamento = np.array(classe_treinamento)

classificador = DecisionTreeClassifier(criterion = 'entropy', 
                                       random_state = 0,
                                       max_depth = 40,
                                       min_samples_leaf = 10,
                                       max_features = 30)

multiOutputs = MultiOutputClassifier(classificador,n_jobs=-1)

previsoes = multiOutputs.fit(previsores_treinamento, classe_treinamento)

from sklearn.metrics import confusion_matrix, accuracy_score
precisao = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)

print(classificador.feature_importances_)

'''