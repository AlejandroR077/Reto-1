import pandas as pd

def fill_nan(df, method='fixed', value=None, limit=None):
    if method == 'fixed':
        if value is None:
            raise ValueError("Debes proporcionar un valor para 'value' cuando method='fixed'.") #Rellena con un valor fijo
        filled_df = df.fillna(value=value, limit=limit)
    elif method == 'mean': 
        filled_df = df.fillna(df.mean(), limit=limit)   #Rellena con la media
    elif method == 'bfill':
        filled_df = df.fillna(method='bfill', limit=limit) # Rellenando los NaN con el valor de adelante proyectando el valor hacia atrás hasta una posición)
    elif method == 'ffill':
        filled_df = df.fillna(method='ffill', limit=limit) # Rellenando los NaN con el valor de atrás (proyectando el valor hacia delante hasta una posición)
    else:
        raise ValueError("Método de limpieza no valido")

    return filled_df