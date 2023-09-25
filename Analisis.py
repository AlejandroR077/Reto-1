import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def analizar_nan(df):
    # Identificar la cantidad de valores NaN por columna
    nan_columnas = df.isna().sum()
    print("Cantidad de valores NaN por columna:")
    print(nan_columnas)

    # Identificar la cantidad de valores NaN por fila
    nan_filas = df.isna().sum(axis=1)
    print("Cantidad de valores NaN por fila:")
    print(nan_filas)

    # Calcular la cantidad total de valores NaN en el DataFrame
    total_nan = df.isna().sum().sum()
    print("Cantidad total de valores NaN:", total_nan)

    # Crear un mapa de calor de valores NaN
    sns.heatmap(df.isnull(), cbar=False)
    plt.show()

def analizar_valor(df, valor):
    
    # Identificar la cantidad de valores iguales a valor por columna
    valores_columnas = (df == valor).sum()
    print(f"Cantidad de valores igual a '{valor}' por columna:")
    print(valores_columnas)

    # Identificar la cantidad de valores iguales a valor por fila
    valores_filas = (df == valor).sum(axis=1)
    print(f"Cantidad de valores igual a '{valor}' por fila:")
    print(valores_filas)

    # Calcular la cantidad total de valores iguales a valor en el DataFrame
    total_valores = (df == valor).sum().sum()
    print(f"Cantidad total de valores igual a '{valor}': {total_valores}")

    # Crear un mapa de calor de valores iguales a valor
    sns.heatmap(df == valor, cbar=False)
    plt.show()

