# Se requiere escribir un archivo txt con 10 veces el saludo "Hola Mundo"

archivo = open("saludo.txt", "w")
for i in range(10):
    archivo.write("Hola Mundo\n")
archivo.close()

