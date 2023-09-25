import pandas as pd

def aplicar_filtro(df, columna=None, condicion=None):
   
    if columna is not None and condicion is not None:
        return df[df[columna].apply(condicion)]
    elif condicion is not None:
        return df[condicion(df)]
    else:
        raise ValueError("Proporcione al menos una condición de filtro.")