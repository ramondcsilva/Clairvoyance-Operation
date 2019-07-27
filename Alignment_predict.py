"""
Created on Thu Jul  4 11:20:05 2019
@author: Ramon Silva, Adlla Katarine, Daniel Alves
"""

########################## TRATAMENTO #############################
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
imputer = SimpleImputer(missing_values = '-', strategy='constant', fill_value='bad')
# imputer faz as estatiscas sobre o atributo Previsores
imputer = imputer.fit(previsores[:,7].reshape(1,-1)) 
# Atribui as modificação de valores nulos, a mesma variavel
previsores[:,7] = imputer.fit_transform(previsores[:,7].reshape(1,-1))

imputer = SimpleImputer(missing_values = 'neutral', strategy='constant', fill_value='bad')
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
classe = result.iloc[:,7].values        # 52% Alingment features = 20, depth = 21 66%
result = result.drop(columns=7)

# Retorna a modificação
previsores = result.iloc[:,:].values
    
########################## PREDITORES #############################
from sklearn.preprocessing import LabelEncoder
previsores[:, 0] = LabelEncoder().fit_transform(previsores[:, 0])
previsores[:, 1] = LabelEncoder().fit_transform(previsores[:, 1])
previsores[:, 2] = LabelEncoder().fit_transform(previsores[:, 2])
previsores[:, 3] = LabelEncoder().fit_transform(previsores[:, 3])
previsores[:, 5] = LabelEncoder().fit_transform(previsores[:, 5])
previsores[:, 6] = LabelEncoder().fit_transform(previsores[:, 6])
previsores[:, 7] = LabelEncoder().fit_transform(previsores[:, 7])

previsores = previsores.astype('int')

classe = LabelEncoder().fit_transform(classe)

# Função do pacote sklearn que divide automaticamente dados teste e dados de treinamento
from sklearn.model_selection import train_test_split
# Criando variaveis para treinamento e teste, usando o metodo de divisao dos dados
# Usou-se 25%(test_size = 0.25) como quantidade de atributos para teste e o restante para treinamento
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.33, random_state=0)
'''
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Atribui o escalonamento ao atributo previsores
previsores_treinamento = scaler.fit_transform(previsores_treinamento)
previsores_teste = scaler.fit_transform(previsores_teste)
'''
# Treinamento a partir de uma Arvore de Decisao, com o criterio de Entropia, unico teste  
# Hiperparamenters para achar a melhores paramentros para a arvore
paramenter = {"max_depth": [3,10],
              "min_samples_leaf": [1,5],
              'criterion': ('gini','entropy')}  

# Encontrando a melhor configuração para a arvores 
from sklearn.tree import DecisionTreeClassifier
tree = DecisionTreeClassifier()

from sklearn.model_selection import GridSearchCV #RandomizedSearchCV
classificador = GridSearchCV(tree,paramenter, cv=3)

classificador.fit(previsores_treinamento, 
                  classe_treinamento)

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
                           cv=5)

scores_cv['test_precision_macro']

from sklearn.metrics import accuracy_score, confusion_matrix
# Compara dados de dois atributos retornando o percentual de igualdade deles
accuracy = accuracy_score(classe_teste, previsoes) 
# Cria uma matriz para comparação de dados dos dois atributos
matriz = confusion_matrix(classe_teste, previsoes)

from sklearn import metrics
import matplotlib.pyplot as plt
preds = classificador.predict_proba(previsores_teste)[::,1]
cls_teste = pd.DataFrame(classe_teste).astype('float')
fpr, tpr,_ = metrics.roc_curve(cls_teste, preds)
auc = metrics.roc_auc_score(cls_teste, preds)
plt.plot(fpr,tpr,label="Alignment, auc="+str(auc))
plt.legend(loc=4)
plt.show()