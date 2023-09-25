import pandas as pd 
from sodapy import Socrata

def conexion(ubicacion, ruta, token):  

    if ubicacion == 'local':          
        try:
            dataframe = pd.read_csv(ruta) 
            return dataframe              
        except FileNotFoundError:      
            print("El archivo CSV no se encontró, validar la ruta.")
            return None
        except Exception:
            print(f"Error al importar el dataset", str(ruta))
            return None

    elif ubicacion == 'url':              
        try:
            dataframe = pd.read_csv(ruta) 
            return dataframe              
        except FileNotFoundError:      
            print("El archivo no se encontro en la url dada, validar.")
            return None
        except Exception:
            print("Error al importar el dataset")
            return None

    elif ubicacion == 'socrata': 
        try:
            cliente = Socrata(ruta, None)
            resultado = cliente.get(token, limit=1000)   
            dataframe = pd.DataFrame.from_records(resultado)
            return dataframe
        except requests.exceptions.RequestException as e:
            print("Error al conectar con el cliente de Socrata")
            return None
        except Exception as e:
            print("Error al importar el dataset desde Socrata")
            return None
   
    else:
        print("La ubicacion no es valida. Utilice 'local', 'url' o 'socrata'.")
        return None



#conexion("socrata","www.datos.gov.co", "ji8i-4anb")
#conexion("local","/work/phone_data.csv","")
#conexion("url","https://raw.githubusercontent.com/Opensourcefordatascience/Data-sets/master/automotive_data.csv", "")
