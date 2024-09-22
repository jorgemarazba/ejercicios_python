def escribirLista(Lista, nombreArchivo):
    archivo = open(nombreArchivo, 'w')
    
    
    for fila in Lista:
        for columna in fila:
            if isinstance(columna, str):
                archivo.write(columna)
            else:
                archivo.write(str(columna))
            archivo.write("\t")
            
        archivo.write("\n")
    archivo.close()