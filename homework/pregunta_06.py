"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

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
                    diccionario[letra]=[number,number]
                else:
                    diccionario[letra][0] = min(diccionario[letra][0], number)
                    diccionario[letra][1] = max(diccionario[letra][1], number)

    ans = []
    for key,value in diccionario.items():
        ans.append((key,value[0], value[1]))
    print(sorted(ans))
    return sorted(ans)

