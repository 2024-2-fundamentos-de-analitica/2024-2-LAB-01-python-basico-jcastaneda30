"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    diccionario = dict()
    with open("files/input/data.csv") as archivo:
        lector = csv.reader(archivo, delimiter="\t")
        for row in lector:
            letra = row[0]
            number = int(row[1])
            if letra not in diccionario:
                diccionario[letra]=[number,number]
            else:
                diccionario[letra][0] = max(diccionario[letra][0], number)
                diccionario[letra][1] = min(diccionario[letra][1], number)

    ans = []
    for key,value in diccionario.items():
        ans.append((key,value[0], value[1]))

    return sorted(ans)

