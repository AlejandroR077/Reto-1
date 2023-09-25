from Modulos.Conexion import conexion

print("Ingrese desde donde quiere importar su dataset")
n = int(input("(1) Local, (2) Url, (3) Socrata \n"))

if n == 1:
    ubicacion = "local"
    ruta = input("Ingrese la ruta \n")
    token = ""
    print(conexion(ubicacion, ruta, token))
    

elif n == 2:
    ubicacion = "url"
    ruta = input("Ingrese la url \n")
    token = ""
    print(conexion(ubicacion, ruta, token))

elif n == 3: 
    ubicacion = "socrata"
    ruta = input("Ingrese la url \n")
    token = input("Ingrese el token \n")
    print(conexion(ubicacion, ruta, token))

else:
    print("Dato fuera del rango, pruebe: (1) Local, (2) Url, (3) Socrata ")




