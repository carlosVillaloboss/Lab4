# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 10:44:22 2024

@author: juanc
"""
from Class_Fecha import Fecha
from Class_Direccion import Direccion


class Usuario:
    def __init__(self, nombre="", id=0):
        
        self.__nombre = nombre
        self.__id = id
        self.__fecha_nacimiento = None
        self.__ciudad_nacimiento = ""
        self.__tel = 0
        self.__email = ""
        self.__dir = None

    # Métodos setter
    def setNombre(self, nombre):
        
        self.__nombre = nombre

    def setId(self, id):
        
        self.__id = id

    def setFecha_nacimiento(self, f):
        
        if isinstance(f, Fecha):
            self.__fecha_nacimiento = f
        else:
            raise ValueError("La fecha de nacimiento debe ser una instancia de la clase Fecha.")

    def setCiudad_nacimiento(self, c):
        
        self.__ciudad_nacimiento = c

    def setTel(self, t):
        
        self.__tel = t

    def setEmail(self, e):
        
        self.__email = e

    def setDir(self, d):
        
        if isinstance(d, Direccion):
            self.__dir = d
        else:
            raise ValueError("La dirección debe ser una instancia de la clase Direccion.")

    # Métodos getter
    def getNombre(self):
        
        return self.__nombre

    def getId(self):
        
        return self.__id

    def getFecha_nacimiento(self):
        
        return self.__fecha_nacimiento

    def getCiudad_nacimiento(self):
        
        return self.__ciudad_nacimiento

    def getTel(self):
        
        return self.__tel

    def getEmail(self):
        
        return self.__email

    def getDir(self):
        
        return self.__dir
    
    # Método toString
    def toString(self):
        
        fecha_nac = str(self.__fecha_nacimiento) if self.__fecha_nacimiento else "No especificada"
        direccion = self.__dir.toString() if self.__dir else "No especificada"
        return (f" {self.__nombre}, {self.__id}, {fecha_nac}, {self.__ciudad_nacimiento}, {self.__tel}, {self.__email}, {direccion}")
