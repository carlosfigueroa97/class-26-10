"""
Nombre: SoluciónEjercicio.py
Objetivo: Resolver ejercicio 3
Autor: Carlos Alejandro Figueroa Bazán
Fecha: 02 de Noviembre de 2019
"""
sueldos = []

def insertarSueldoTrabajador():
    for i in range(10):
        sueldo = int(input(f'Ingrese el sueldo del trabajador {i}: '))
        sueldos.append(sueldo)

def totalNomina():
    suma = 0
    for i in sueldos:
        suma += i
    return suma

def main():
    insertarSueldoTrabajador()
    suma = totalNomina()
    print(f'El total de la nomina es: {suma}')

if __name__ == "__main__":
    main()