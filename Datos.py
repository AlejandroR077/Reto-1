import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Paso 1: Cargar el DataFrame desde el archivo CSV
#df = pd.read_csv("C:\\Users\\Diego_PC\\Desktop\\Reto\\muestra.csv") 

def generar_mapa_de_calor_correlacion(df):
    df_numeric = df.select_dtypes(include=['number'])
    plt.figure(figsize=(10, 6))
    sns.heatmap(df_numeric.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Mapa de Calor de Correlación para Columnas Numéricas')
    plt.show()

# generar_mapa_de_calor_correlacion(df)


def generar_diagrama_de_cajas(df):
    df_numeric = df.select_dtypes(include=['number'])
    for columna in df_numeric.columns:
        plt.figure(figsize=(6, 4))
        sns.boxplot(x=df[columna], orient='vertical', width=0.4)
        plt.title(f'Diagrama de Caja y Bigotes de {columna}')
        plt.show()

# generar_diagrama_de_cajas(df)

def generar_histogramas(df):
    df_numeric = df.select_dtypes(include=['number'])
    for columna in df_numeric.columns:
        plt.figure(figsize=(6, 4))
        sns.histplot(data=df, x=columna, bins=20, kde=True)
        plt.title(f'Histograma de {columna}')
        plt.show()

# generar_histogramas(df)

def generar_distancia_a_media_para_todas(df):
    df_numeric = df.select_dtypes(include=['number'])
    for columna in df_numeric.columns:
        plt.figure(figsize=(6, 4))
        media = df[columna].mean()
        distancia_a_media = df[columna] - media
        sns.histplot(data=distancia_a_media, bins=20, kde=True)
        plt.title(f'Distancia de los Valores a la Media de {columna}')
        plt.xlabel('Distancia a la Media')
        plt.show()

#generar_distancia_a_media_para_todas(df)

"""
def generar_graficos_de_barras_de_promedio_por_columna(df):
    # Paso 1: Seleccionar solo las columnas numéricas
    df_numeric = df.select_dtypes(include=['number'])

    if not df_numeric.empty:
        # Paso 2: Generar un gráfico de barras para cada columna numérica
        for columna in df_numeric.columns:
            plt.figure(figsize=(8, 6))
            promedio = df_numeric[columna].mean()
            plt.bar(columna, promedio, color='skyblue')
            plt.title(f'Promedio de {columna}')
            plt.xlabel(columna)
            plt.ylabel('Promedio')
            plt.xticks(rotation=45)
            plt.show()
    else:
        print('No se encontraron columnas numéricas en el DataFrame.')

generar_graficos_de_barras_de_promedio_por_columna(df)
"""