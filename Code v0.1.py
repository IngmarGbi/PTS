# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 13:48:53 2019

@author: henri.marteville
"""

import math

class individu(object):
    def _init_(self):
        self.trajet = []
        self.cout = None
    
    

class generation(object):
    
    id = 0
    
    def _init_(self):
        self.identifiant = id
        self.population = []
        self.meilleurCout = None
        generation.id += 1
    
    def calculCout(self):
        coutTotal = 0
        for i in range (0,len(self.population)-2):
            coutTotal += gene.distance(self.population[i+1],self.population[i])
        coutTotal += gene.distance(self.population[len(self.population),self.population[0]]) #Parcours la liste de l'indice 0 à (n-2) et ajoute au cout total la distance entre le point i et i+1
        return coutTotal
            
            
class gene(object):
    
    def _init_(self,x,y):
        self.nom = ""
        self.x = x
        self.y = y
        
    def distance(geneA,geneB):
        xA = geneA.x
        yA = geneA.y
        xB = geneA.x
        yB = geneA.y
        return (math.sqrt((xB - xA)^2 + (yB - yA)^2)) #Formule de la distance entre 2 points
    

    

    
        
        
    
        
        
    

        
        