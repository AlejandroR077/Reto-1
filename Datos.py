import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def datos(df):

    sns.heatmap(df.sub(df.mean()).abs(), cmap='coolwarm', annot=True)
    plt.title("Mapa de calor de distancia de valores a la media por columna")
    plt.show()

    # Diagramas de cajas y bigotes por columna
    sns.boxplot(data=df, orient='vertical', palette='Set2')
    plt.title("Diagramas de cajas y bigotes por columna")
    plt.show()

    # Cuartiles por columna
    cuartiles = df.describe(percentiles=[0.25, 0.5, 0.75])
    print("Cuartiles por columna:")
    print(cuartiles)