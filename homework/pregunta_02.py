"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    diccionario = dict()
    with open("files/input/data.csv") as cssv:
        readerr = csv.reader(cssv, delimiter="\t")
        for row in readerr:
            letra = row[0]
            if letra not in diccionario:
                diccionario[letra]=0
            diccionario[letra]+=1
    
    return sorted(diccionario.items())

