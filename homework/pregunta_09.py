"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    diccionario = dict()
    with open("files/input/data.csv") as archivo:
        lector = csv.reader(archivo, delimiter="\t")
        for row in lector:
            llaves = row[4].split(",")
            print(llaves)
            for par in llaves:
                letra, number = par.split(":")
                print(par)
                number = int(number)
                if letra not in diccionario:
                    diccionario[letra]=0
                diccionario[letra]+=1

    return diccionario