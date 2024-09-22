# Realice un programa en Python que permita crear un archivo con líneas que el usuario escriba y
# termine cuando en una línea nueva el usuario escriba “fin_archivo”

archivo = open("saludo.txt", "w")
print("------ Bienvenido al programa de creación de archivos ------\n")
print("Escribe líneas que se guardarán en el archivo saludo.txt")
print("Escribe 'fin_archivo' para terminar")
while True:
    texto = input("Escribe una línea: ")
    if texto == "fin_archivo":
        break
    archivo.write(texto + "\n")
archivo.close()
print("Archivo creado con éxito")

