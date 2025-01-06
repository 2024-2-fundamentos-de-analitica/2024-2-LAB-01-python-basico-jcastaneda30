"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    diccionario = dict()
    with open("files/input/data.csv") as cssv:
        readerr = csv.reader(cssv, delimiter="\t")
        for row in readerr:
            letra = row[0]
            number = int(row[1])
            if letra not in diccionario:
                diccionario[letra]=0
            diccionario[letra]+=number
    
    return sorted(diccionario.items())
