# Description: Programa que lee un archivo de texto y muestra su contenido en pantalla
nombre_archivo = str(input("Ingresa el nombre del archivo que deseas leer: "))

archivo = open(nombre_archivo, "r")
for linea in archivo:
    print(linea)
archivo.close()
