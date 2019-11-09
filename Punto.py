"""
Nombre: Punto.py
Objetivo: Es la superclase en la jerarquía de herencia.
Autor: Carlos Alejandro Figueroa Bazán
Fecha: 9/11/2019
"""

class Punto(object):
    # Método constructor
    def __init__(self, valorX, valorY):
        # Creamos atributos
        self.x = valorX
        self.y = valorY

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def setX(self, valorX):
        self.x = valorX

    def setY(self, valorY):
        self.y = valorY

    # Método toString()
    def toString(self):
        return ("Las coordenadas del punto son: ", str(self.x), " , ", str(self.y))