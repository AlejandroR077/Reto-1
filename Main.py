from Modulos.Analisis import analizar_nan, analizar_valor
from Modulos.Conexion import conexion
from Modulos.Datos import generar_mapa_de_calor_correlacion
from Modulos.Datos import generar_diagrama_de_cajas
from Modulos.Datos import generar_histogramas
from Modulos.Datos import generar_distancia_a_media_para_todas
#from Modulos.Daotos import generar_graficos_de_barras_de_promedio_por_columna
from Modulos.Filtrado import filtrar
from Modulos.Limpieza import fill_nan


print("Ingrese desde donde quiere importar su dataset")
n = int(input("(1) Local, (2) Url, (3) Socrata \n"))

if n == 1:
    ubicacion = "local"
    ruta = input("Ingrese la ruta \n")
    token = ""
    df = conexion(ubicacion, ruta, token)
    print(conexion(ubicacion, ruta, token))
    

elif n == 2:
    ubicacion = "url"
    ruta = input("Ingrese la url \n")
    token = ""
    df = conexion(ubicacion, ruta, token)
    print(conexion(ubicacion, ruta, token))

elif n == 3: 
    ubicacion = "socrata"
    ruta = input("Ingrese la url \n")
    token = input("Ingrese el token \n")
    df = conexion(ubicacion, ruta, token)
    print(conexion(ubicacion, ruta, token))

else:
    print("Dato fuera del rango, pruebe: (1) Local, (2) Url, (3) Socrata ")

print("Ingrese el tipo de opcion de analisis para el dataframe")
n1 = int(input("(1) NaN, (2) Algun valor  \n"))

if n1 == 1:
    print(analizar_nan(df))
elif n1 == 2:
    valor = input("Ingrese el valor al dato a analizar \n")
    print(analizar_valor(df, valor))
else:
    print("Opcion fuera del rango, pruebe: (1) NaN, (2) Algun valor ")

print("Desea limpiar el dataframe?")

op = int(input("(1) Si, (2) No  \n"))

if op == 1:

    print("Como desea reemplazar los datos NaN: ")
    op1 = int(input("(1) Rellenar valor fijo, (2) Proyectar el valor hacia atras, (3) Proyectar el valor hacia delante \n"))
    if op1 == 1:
        val = input("reemplazar NaN por el valor de: \n")
        df = fill_nan(df, method='fixed', value=val)
        print(df)
    elif op1 == 2:
        lim = int(input("Ingrese el valor hasta el cual se va a proyectar para reemplazar el NaN \n"))
        df = fill_nan(df, method='bfill', limit=lim)
        print(df)
    elif op1 == 3:
        lim = int(input("Ingrese el valor hasta el cual se va a proyectar para reemplazar el NaN \n"))
        df = fill_nan(df, method='ffill', limit=lim)
        print(df)
    else:
        print("Opcion fuera del rango, pruebe: (1) Rellenar valor fijo, (2) Proyectar el valor hacia atras, (3) Proyectar el valor hacia delante")

print("Desea ver un analisis mas profundo de los datos?")

op2 = int(input("(1) Si, (2) No  \n"))

if op2 == 1:
    print(generar_diagrama_de_cajas(df))
    print(generar_histogramas(df))
    print(generar_mapa_de_calor_correlacion(df))
    print(generar_distancia_a_media_para_todas(df))
    #print(generar_graficos_de_barras_de_promedio_por_columna(df))

print(df)
print("Desea aplicar algun filtro?")
op4 = int(input("(1) Si, (2) No \n"))

if op4 == 1:
    columna = input("Ingrese la columna: \n")
    operador = input("Ingrese el tipo de filtrado \n Mayor que (>), Menor que (<), Igual a (==), Valor entre (:) \n")
    valor = float(input("Ingrese el valor \n"))

    df = filtrar(df, columna, operador, valor)
    print(df)
 

 ##               C:\\Users\\Diego_PC\\Desktop\\Reto\\dfnan.csv