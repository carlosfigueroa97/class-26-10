"""
Nombre: SoluciónEjercicio.py
Objetivo: Resolver ejercicio 4
Autor: Carlos Alejandro Figueroa Bazán
Fecha: 02 de Noviembre de 2019
"""
calificaciones = []

def insertarCalificaciones(n):
    for i in range(n):
       calificacion = float(input(f'Ingrese la calificación {i}: '))
       calificaciones.append(calificacion)

def promedioGeneral(n):
    sum = 0
    for i in calificaciones:
        sum += i
    promedio = sum / n
    print(f'El promedio general es: {promedio}')

def alumnosAprobadosReprobados(n):
    aprobados = 0
    for i in calificaciones:
        if(i >= 70):
            aprobados += 1
    reprobados = n - aprobados
    porcentajeA = (aprobados / n) * 100
    porcentajeB = (reprobados / n) * 100
    print(f'El numero de alumnos aprobados es: {aprobados}')
    print(f'El numero de alumnos reprobados es: {reprobados}')
    print(f'El porcentaje de alumnos aprobados es: {porcentajeA}')
    print(f'El porcentaje de alumnos aprobados es: {porcentajeB}')

def main():
    n = int(input('Ingrese el numero de calificaciones que desea capturar: '))
    insertarCalificaciones(n)
    promedioGeneral(n)
    alumnosAprobadosReprobados(n)

if __name__ == "__main__":
    main()