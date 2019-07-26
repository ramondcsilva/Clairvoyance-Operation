# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 00:01:09 2019
@author: Ramon Silva, Adlla Katarine, Daniel Alves
"""

import pandas as pd
import pandas as dd
from scipy.spatial import distance
import numpy as np 

class SuperPower:
    
    def __init__(self):
        # Leitura de arquivo para criação da base_herois de dados
        self.base_superpower = pd.read_csv('superpoderes.csv')
        self.previsores = self.base_superpower.iloc[:,1:169].values
        self.nomes = self.base_superpower.iloc[:,0].values
    
    def criarListas(self):
        self.names = self.base_superpower["hero_names"] #Lista com o nome de todos os heróis
        #Lista com todas as distâncias que podem ser escolhidas pelo usuário
        self.distancia_type = ["Distância de Hamming", "Distância de Jaccard", "Distância de Kulsinski", 
                          "Distância de Rogerstanimoto", "Distância de Russellrao", "Distância de Sokalmichener"]
        self.superpower = self.base_superpower.columns[1:] #Lista de todos os super-poderes
    
    def retornarNames(self):
        return self.names
    
    def retornarDistancias(self):
        return self.distancia_type
    
    def retornarSuperPower(self):
        return self.superpower
    
    #TEMPORARIO - VER
    def escolherSuperPower(self, escolha_n):
        escolha_sp = [] #Lista com os indices dos super-poderes escolhidos
        ss = [] #Lista com o nome dos super-poderes escolhidos
        for i in range(0,escolha_n):
            print(f"Escolha {(i+1)}: ")
            escolha_sp.append(int(input()))
            ss.append(self.superpower[escolha_sp[i]])
    
    def criarBaseDadosPoderes(self):
        #É criado uma base de dados com todos os super-poderes(escolhidos pelo usuário) dos heróis
        self.base_distancias = dd.DataFrame(columns=self.ss, index=range(667))
        #Informações sobre os super-poderes é passado para a "base_distancias"
        for i in range(0,len(self.ss)):
            self.base_distancias.iloc[:,i] = self.base_superpower.loc[:, str(self.superpower[self.escolha_sp[i]])]
        self.base_distancias = self.base_distancias.iloc[:,:].values

    def escolherHeroi(self, heroi):
        # Encontra indice do Heroi pesquisado
        self.heroi, = np.where(self.nomes == self.heroi)
    
    def escolherDistancia(self, escolha_distancia):
        self.escolha_distancia = escolha_distancia
    
    def calcularDistancia(self):
        if(self.escolha_distancia == 0):
            ################### DISTÂNCIA DE HAMMING #############################
            for i in range(0, 667):
                if(i != self.heroi):
                    self.valor_distancias[i,1] = distance.hamming([self.base_distancias[self.heroi,:]],[self.base_distancias[i,:]])
                    self.valor_distancias[i,0] = i
                
        elif(self.escolha_distancia == 1):
            ################### DISTÂNCIA DE JACCARD #############################
            for i in range(0, 667):
                if(i != self.heroi):
                    self.valor_distancias[i,1] = distance.jaccard([self.base_distancias[self.heroi,:]],[self.base_distancias[i,:]])
                    self.valor_distancias[i,0] = i
        elif(self.escolha_distancia == 2):
            ################### DISTÂNCIA DE ROGERSTANIMOTO #############################
            for i in range(0, 667):
                if(i != self.heroi):
                    self.valor_distancias[i,1] = distance.rogerstanimoto([self.base_distancias[self.heroi,:]],[self.base_distancias[i,:]])
                    self.valor_distancias[i,0] = i
                    
        elif(self.escolha_distancia == 3):
            ################### DISTÂNCIA DE KULSINSKI #############################
            for i in range(0, 667):
                if(i != self.heroi):
                    self.valor_distancias[i,1] = distance.kulsinski([self.base_distancias[self.heroi,:]],[self.base_distancias[i,:]])
                    self.valor_distancias[i,0] = i
                    
        elif(self.escolha_distancia == 4):
            ################### DISTÂNCIA DE RUSSELLRAO #############################
            for i in range(0, 667):
                if(i != self.heroi):
                    self.valor_distancias[i,1] = distance.russellrao([self.base_distancias[self.heroi,:]],[self.base_distancias[i,:]])
                    self.valor_distancias[i,0] = i
                     
        else:
            ################### DISTÂNCIA DE SOKALMICHENER #############################
            for i in range(0, 667):
                if(i != self.heroi):
                    self.valor_distancias[i,1] = distance.sokalmichener([self.base_distancias[self.heroi,:]],[self.base_distancias[i,:]])
                    self.valor_distancias[i,0] = i
                    
        #Ordena o array em ordem crescente
        self.valor_distancias = pd.DataFrame(self.valor_distancias).sort_values(by=1)
        
    
    def rankingHerois(self):
        # Guarda os 10 herois com menores distancias
        result = self.valor_distancias.iloc[1:11,0:2]
        for i in range(0,10):
            numero = self.valor_distancias.iloc[i+1,0].astype('int')
            result.iloc[i,0] = self.base_superpower.iloc[numero,0] 