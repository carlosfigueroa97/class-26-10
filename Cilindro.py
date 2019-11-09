"""
Nombre: Cilindro.py
Objetivo: Es la subclase de circunferencia.
Autor: Carlos Alejandro Figueroa Bazán
Fecha: 9/11/2019
"""

from Circunferencia import Circunferencia
from Punto import Punto

class Cilindro(Circunferencia):
    def __init__(self, valorX, valorY, vradio, valtura):
        self.altura = valtura
        Circunferencia.__init__(self, valorX, valorY, vradio)
        Punto.__init__(self, valorX, valorY)

    def getAltura(self):
        return self.altura

    def setAltura(self, valtura):
        self.altura = valtura

    def toString(self):
        return "La altura es: " , str(self.altura)