# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 00:01:09 2019
@author: Ramon Silva, Adlla Katarine, Daniel Alves
"""

import pandas as pd
import pandas as dd
from sklearn.metrics.cluster import adjusted_rand_score, adjusted_mutual_info_score, completeness_score
from scipy.spatial import distance
import numpy as np 

class SuperPower:
    
    def __init__(self):
        '''
        Leitura de arquivo para criação da base_superpower de dados, 
        '''
        self.base_superpower = pd.read_csv('superpoderes.csv')
    
    def criarListas(self):
        '''
        São criadas 3 listas, cada uma contendo o nome dos herois, distancias disponiveis e super-poderes.
        '''
        self.names = self.base_superpower["hero_names"] #Lista com o nome de todos os heróis
        #Lista com todas as distâncias que podem ser escolhidas pelo usuário
        self.distancia_type = ["Distância de Jaccard", "Distância de Russellrao", "Distância de Hamming",
                               "Distância de ROGERSTANIMOTO", "Distância de KULSINSKI"]
        self.superpower = self.base_superpower.columns[1:] #Lista de todos os super-poderes
        
    def retornarNames(self):
        '''
        Retorna uma lista com o nome de todos os herois.
        '''
        return self.names
    
    def retornarDistancias(self):
        '''
        Retorna uma lista com o nome das distâncias disponiveis.
        '''
        return self.distancia_type
    
    def retornarSuperPower(self):
        '''
        Retorna uma lista com o nome de todos os super-poderes.
        '''
        return self.superpower
    
    def escolherSuperPower(self, lista):
        '''
        Uma lista com indice dos super-poderes escolhidos é passada por parametro e depois criado outra
        lista com o nome de cada um desses super-poderes.
        '''
        self.indices_sPoderesEscolhidos = lista #Lista com os indices dos super-poderes escolhidos
        self.listaSPoderes = [] #Lista com o nome dos super-poderes escolhidos
        for i in range(0, len(self.indices_sPoderesEscolhidos)):
            self.listaSPoderes.append(self.superpower[self.indices_sPoderesEscolhidos[i]])
    
    def criarBaseDadosPoderes(self):
        '''
        É criado uma base de dados com todos os super-poderes(escolhidos pelo usuário) dos heróis
        e informações sobre os super-poderes é passado para a "baseSPoderes_Escolhidos"
        '''
        self.baseSPoderes_Escolhidos = dd.DataFrame(columns = self.listaSPoderes, index = range(667))
        
        for i in range(0, len(self.listaSPoderes)):
            self.baseSPoderes_Escolhidos.iloc[:,i] = self.base_superpower.loc[:, str(self.superpower[self.indices_sPoderesEscolhidos[i]])]
        self.baseSPoderes_Escolhidos = self.baseSPoderes_Escolhidos.iloc[:,:].values

    def escolherHeroi(self, heroiAux):
        '''
        Recebe o heroi escolhido por indice.
        '''
        print(heroiAux)
        self.heroi, = np.where(self.names == heroiAux)
        print(self.heroi)
        
    def escolherDistancia(self, escolha_distancia):
        '''
        Recebe a distancia escolhida por indice.
        '''
        self.escolha_distancia = escolha_distancia
    
    def criarArrayDistancia(self):
        '''
        Um array é instanciado para guardar todos os valores de distancia calculados.
        '''
        self.valor_distancias = np.zeros((667,2), dtype=np.double)
    
    def distanciaJaccard(self):
        '''
        Calcula a distancia de Jaccard.
        '''
        for i in range(0, 667):
            if(i != self.heroi):
                self.valor_distancias[i,1] = distance.jaccard([self.baseSPoderes_Escolhidos[self.heroi,:]],[self.baseSPoderes_Escolhidos[i,:]])
                self.valor_distancias[i,0] = i
    
    def distanciaRussellRao(self):
        '''
        Calcula a distancia de RussealRao.
        '''
        for i in range(0, 667):
            if(i != self.heroi):
                self.valor_distancias[i,1] = distance.russellrao([self.baseSPoderes_Escolhidos[self.heroi,:]],[self.baseSPoderes_Escolhidos[i,:]])
                self.valor_distancias[i,0] = i
    
    
    def distanciaHamming(self):
        '''
        Calcula a distancia de Hamming.
        '''
        for i in range(0, 667):
                if(i != self.heroi):
                    self.valor_distancias[i,1] = distance.hamming([self.baseSPoderes_Escolhidos[self.heroi,:]],[self.baseSPoderes_Escolhidos[i,:]])
                    self.valor_distancias[i,0] = i
    
    def distanciaROGER(self):
        '''
        Calcula a distancia de ROGERSTANIMOTO.
        '''
        for i in range(0, 667):
                if(i != self.heroi):
                    self.valor_distancias[i,1] = distance.rogerstanimoto([self.baseSPoderes_Escolhidos[self.heroi,:]],[self.baseSPoderes_Escolhidos[i,:]])
                    self.valor_distancias[i,0] = i

    def distanciaKulsin(self):
        '''
        Calcula a distancia de KULSINSKI.
        '''
        for i in range(0, 667):
                if(i != self.heroi):
                    self.valor_distancias[i,1] = distance.kulsinski([self.baseSPoderes_Escolhidos[self.heroi,:]],[self.baseSPoderes_Escolhidos[i,:]])
                    self.valor_distancias[i,0] = i

    def ordenarDistancias(self):
        '''
        Ordena o array das distancias em ordem crescente.
        '''
        self.valor_distancias = pd.DataFrame(self.valor_distancias).sort_values(by=1)
    
    def calcularDistancia(self):
        '''
        Usa um if para descobrir qual o método de distância escolhido e por fim chama o método de ordenação.
        '''
        self.criarArrayDistancia()
        
        if(self.escolha_distancia == 0):
            ################### DISTÂNCIA DE JACCARD #############################
            self.distanciaJaccard()
            
        elif(self.escolha_distancia == 1):
            ################### DISTÂNCIA DE RUSSELLRAO #############################
            self.distanciaRussellRao()
            
        elif(self.escolha_distancia == 2):
            ################### DISTÂNCIA DE HAMMING #############################
            self.distanciaHamming()
            
        elif(self.escolha_distancia == 3):
            ################### DISTÂNCIA DE ROGERSTANIMOTO #############################
            self.distanciaROGER()
        
        else:
            ################### DISTÂNCIA DE KULSINSKI #############################
            self.distanciaKulsin()
                    
        self.ordenarDistancias()
        
    
    def rankingHerois(self):
        '''
        É feito o ranking com os personagens mais similares com os 10 heróis com menores distancias.
        '''
        ranking = self.valor_distancias.iloc[1:11,0:2]
        for i in range(0,10):
            numero = self.valor_distancias.iloc[i+1,0].astype('int')
            ranking.iloc[i,0] = self.base_superpower.iloc[numero,0]
        return ranking.values.tolist()