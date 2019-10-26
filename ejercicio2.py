"""
Nombre: SoluciónEjercicio.py
Objetivo: Resolver ejercicio 2
Autor: Carlos Alejandro Figueroa Bazán
Fecha: 26 de Octubre de 2019
"""

def main():
    categoria = int(input('Ingrese la categoria: '))
    sueldo = int(input('Ingrese el sueldo del trabajador'))
    if(categoria == 1):
        aumento = sueldo * .15
        sueldo = sueldo + aumento
    elif(categoria == 2):
        aumento = sueldo * .10
        sueldo = sueldo + aumento
    elif(categoria == 3):
        aumento = sueldo * .8
        sueldo = sueldo + aumento
    elif(categoria == 4):
        aumento = sueldo * .7
        sueldo = sueldo + aumento
    else:
        print('No existe esa categoria...')
    print(f'El sueldo es: {sueldo}')
    
if __name__ == "__main__":
    main()