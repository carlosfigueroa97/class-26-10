"""
Nombre: Circunferencia.py
Objetivo: Es la subclase de punto.
Autor: Carlos Alejandro Figueroa Bazán
Fecha: 9/11/2019
"""

from Punto import Punto

class Circunferencia(Punto):
    # Método constructor
    def __init__(self, valorX, valorY, vradio):
        # Actualizar el atributo
        self.radio = vradio
        # Actualizar los atributos de Punto
        Punto.__init__(self, valorX, valorY)

    def getRadio(self):
        return self.radio

    def setRadio(self, vradio):
        self.radio = vradio

    # Método toString
    def toString(self):
        return "El valor del radio es: ", str(self.radio)