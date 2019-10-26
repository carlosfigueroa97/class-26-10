"""
Nombre: SoluciónEjercicio.py
Objetivo: Resolver ejercicio 1
Autor: Carlos Alejandro Figueroa Bazán
Fecha: 26 de Octubre de 2019
"""

def main():
    sueldo = int(input('Ingrese el sueldo de un trabajador: '))
    if(sueldo < 1000):
        aumento = sueldo * .15
        sueldo = sueldo + aumento
    else:
        aumento = sueldo * .12
        sueldo = sueldo + aumento
    print(f'El sueldo del trabajador es: {sueldo}')
          
if __name__ == "__main__":
    main()