from Producto import Producto 

menu = """Bienvenido a la tienda de tecnologia.
1 - Insertar producto
2 - Ver todos
3 - Actualizar
4 - Eliminar
5 - Salir
"""

eleccion = None
while eleccion !=  5:
    print(menu)
    eleccion = int(input("Elija una opcion: "))
    if eleccion == 1:
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio del producto: "))
        cantidad = int(input("Cantidad del producto: "))
        producto = Producto(nombre, precio, cantidad)
        id = insertar(producto) 
        print("El id del producto insertado es: ", id)


    elif eleccion == 2:
        print("Obteniendo productos... ")
        for producto in obtener(): 
            print("===========================")
            print("Id: ", producto["_id"])
            print("Nombre: ", producto["nombre"])
            print("Precio: ", producto["precio"])
            print("Cantidad: ", producto["cantidad"])

    elif eleccion == 3:
        print("Actualizar")
        id = input("Escribe el id: ")
        nombre = input("Escriba el id: ")
        nombre = input("Nuevo nombre del producto: ")
        precio = float(input("Nueva cantidad del producto: "))
        producto = Producto(nombre, precio, cantidad)
        productos_actualizados = actualizar(id, producto) 
        print("Numero de productos actualizados: ",  productos_actualizados)

    elif eleccion == 4:
        print("Eliminar")
        id = input("Escriba el id: ")
        productos_eliminados = eliminar(id) 
        print("Numero de productos eliminados: ", productos_eliminados)
        