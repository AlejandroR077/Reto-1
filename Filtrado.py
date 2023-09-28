import pandas as pd

def filtrar(df, columna, operador, valor):
    if operador == '>':
        return df[df[columna] > valor]
    elif operador == '<':
        return df[df[columna] < valor]
    elif operador == '==':
        return df[df[columna] == valor]
    elif operador == ':':
        valor_min, valor_max = valor
        return df[(df[columna] >= valor_min) & (df[columna] <= valor_max)]
    else:
        raise ValueError("Operador no válido. Utiliza 'mayor_que', 'menor_que', 'igual_a' o 'entre'.")