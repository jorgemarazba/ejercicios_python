def leer_archivo(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    lista = []
    for fila in archivo:
        columna = fila.split()
        registro = [
            columna[0],
            columna[1],
            columna[2],
            columna[3],
            columna[4],
            columna[5],
        ]

        lista.append(registro)
    archivo.close()

    return lista


def main():
    nombre_archivo = str(input("Ingrese el nombre del archivo: "))
    lista = leer_archivo(nombre_archivo)
    print(lista)


if __name__ == "__main__":
    main()
