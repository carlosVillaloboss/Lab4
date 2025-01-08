# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 10:42:29 2024

@author: juanc
"""


class Direccion:
    def __init__(self, calle, nomenclatura, barrio, ciudad, edificio, apto):
        self.__calle = calle
        self.__nomenclatura = nomenclatura
        self.__barrio = barrio
        self.__ciudad = ciudad
        self.__edificio = edificio
        self.__apto = apto

    # Métodos setter
    def setCalle(self, c):
        self.__calle = c

    def setNomenclatura(self, n):
        self.__nomenclatura = n

    def setBarrio(self, b):
        self.__barrio = b

    def setCiudad(self, ci):
        self.__ciudad = ci

    def setEdificio(self, e):
        self.__edificio = e

    def setApto(self, a):
        self.__apto = a

    # Métodos getter
    def getCalle(self):
        return self.__calle

    def getNomenclatura(self):
        return self.__nomenclatura

    def getBarrio(self):
        return self.__barrio

    def getCiudad(self):
        return self.__ciudad

    def getEdificio(self):
        return self.__edificio

    def getApto(self):
        return self.__apto

    # Método toString
    def toString(self):
        return (f"{self.__calle}, {self.__nomenclatura}, {self.__barrio}, {self.__ciudad}, {self.__edificio}, {self.__apto}")
