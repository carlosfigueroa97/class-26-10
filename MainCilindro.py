"""
Nombre: MainCilindro.py
Objetivo: INstanciar a clase cilindro.
Autor: tomado de
Fecha: 9/11/2019
"""

from tkinter import *
from Cilindro import Cilindro

def main():
    w = Tk()
    w.title("Objetos tipo Cilindro")

    lblX = Label(w, text="Coordenada en X: ")
    lblX.grid(column=5, row=5)
    lblY = Label(w, text="Coordenada en Y: ")
    lblY.grid(column=5, row=8)
    cil = Cilindro(10,10, 12.13, 25.11)

    w.mainloop()


if __name__ == "__main__":
    main()