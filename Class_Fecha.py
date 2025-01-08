# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 21:12:38 2024

@author: juanc
"""


class Fecha:
    def __init__(self, dd=1, mm=1, aa=1900):
        self.setDia(dd)
        self.setMes(mm)
        self.setA(aa)
        
    
    def setDia(self, dd):
        
        if 1 <= dd <= 31:
            self.__dia = dd
        else:
            raise ValueError("Día no válido. Debe estar entre 1 y 31.")

    def setMes(self, mm):
        
        if 1 <= mm <= 12:
            self.__mes = mm
        else:
            raise ValueError("Mes no válido. Debe estar entre 1 y 12.")

    def setA(self, aa):
        
        self.__ano = aa

    def getDia(self):
        
        return self.__dia

    def getMes(self):
        
        return self.__mes

    def getA(self):
        
        return self.__ano
    
    def __str__(self):
        
        return f"{self.__dia:02d}, {self.__mes:02d}, {self.__ano}"


        

        

