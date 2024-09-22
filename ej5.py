# Leer archivo de numeros y mostrar el promedio


def leer_archivo(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    lista = []
    for fila in archivo:
        lista.append(int(fila))
    archivo.close()

    return lista


def obtener_promedio(lista):
    suma = 0
    for numero in lista:
        suma += numero
    promedio = suma / len(lista)
    return promedio


def main():
    nombre_archivo = str(input("Ingrese el nombre del archivo: "))

    lista = leer_archivo(nombre_archivo)
    promedio = obtener_promedio(lista)

    print(f"El promedio de los números es: {promedio}")


if __name__ == "__main__":
    main()
