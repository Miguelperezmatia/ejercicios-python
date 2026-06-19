import io
'''
    Desarrolla un programa de gestión de ventas que almacena sus datos en un archivo .txt.

        - Cada producto se guarda en una línea del archivo de la siguiente manera: [nombre_producto], [cantidad_vendida], [precio].

        - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar, actualizar, eliminar productos y salir.

        - También debe poseer opciones para calcular la venta total y por producto.

        - La opción salir borra el .txt.
'''

def menu():
    print("""
          GESTIÓN DE VENTAS
          =================

          OPCIÓN    ACCIÓN

            1       AÑADIR
            2       CONSULTAR
            3       ACTUALIZAR
            4       ELIMINAR
            5       SALIR
        """)
    
def elegir_accion(archivo):
        
        operacion = input("Elige una opción: ")

        if operacion == "1":
            anadir(archivo)

        elif operacion == "2":
            consultar(archivo)
        
        elif operacion == "3":
            actualizar(archivo)
        
        elif operacion == "4":
            eliminar(archivo)
        
        elif operacion == "5":
            salir(archivo)

        else:
            print("Elige una opción válida")

        return operacion

def anadir(archivo):
    nombre_producto = input("Escribe el nombre del producto: ")
    cantidad = input("Escribe la cantidad vendida: ")
    precio = input("Escribe precio de una unidad: ")
    archivo.write(f"[{nombre_producto}], [{cantidad}], [{precio}]\n")

    print("Añadido correctamente")





def consultar():
    pass

def actualizar():
    pass

def eliminar():
    pass

def salir():
    pass



ventas = io.open("ventas.txt", "w")
while True:
    menu()
    op = elegir_accion(ventas)
    if op == "5":
        break

ventas.close()

    

