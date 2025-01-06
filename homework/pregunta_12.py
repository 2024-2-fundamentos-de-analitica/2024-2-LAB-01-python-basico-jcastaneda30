"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    diccionario = {}

    with open("files/input/data.csv") as archivo:
        lector = csv.reader(archivo, delimiter='\t')

        for fila in lector:
            letra = fila[0]

            f = fila[4].split(",")

            numbers = [int(x.split(':')[1]) for x in f]
            
            if letra not in diccionario:
                diccionario[letra] = 0
            
            suma = sum(numbers)
            diccionario[letra] += suma
        
    return diccionario