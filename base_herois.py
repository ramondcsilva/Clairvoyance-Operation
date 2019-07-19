# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 11:20:05 2019
@author: Ramon Silva
"""
# Biblioteca para calculo de distancia dos atributos com valores booleanos
# import scipy as spi

import pandas as pd
# Leitura de arquivo para criação da base_herois de dados
base_herois = pd.read_csv('herois.csv')
base_herois_superpower = pd.read_csv('superpoderes.csv')

# Mescla base de dados  
result = base_herois.merge(base_herois_superpower, left_on='name', right_on='hero_names', how='outer')

# Tratamento de Peso Negativo
base_herois.loc[base_herois.Weight < 0, 'Weight'] = 0
base_herois.loc[base_herois.Weight == 0, 'Weight'] = int(base_herois['Weight'].mean())

# Tratamento de Altura Negativo e substitui pela média
base_herois.loc[base_herois.Height < 0, 'Height'] = 0
base_herois.loc[base_herois.Height == 0, 'Height'] = int(base_herois['Height'].mean())

base_herois.loc[pd.isnull(base_herois['Weight'])]

# Cria atributo para previsao de dados
previsores = base_herois.iloc[:,1:12].values

# Tratando valores 'nan' da base de dados
import numpy as np 
# Cria uma classe SimpleImputer para pre-processamento, 
# representando entrada de dados
from sklearn.impute import SimpleImputer
# imputer recebe a classe que tratar dados nulos, 
# preenchendo com os mais frequentes
imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
# Preenchendo valores vagos com os mais frequentes
imputer = SimpleImputer(missing_values = '-', strategy='most_frequent')
# imputer faz as estatiscas sobre o atributo Previsores
imputer = imputer.fit(previsores[:,:]) 
# Atribui as modificação de valores nulos, a mesma variavel
previsores[:,:] = imputer.fit_transform(previsores[:,:])

