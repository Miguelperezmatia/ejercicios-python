import io
import os

'''
    Desarrolla un programa de gestión de ventas que almacena sus datos en un archivo .txt.

        - Cada producto se guarda en una línea del archivo de la siguiente manera: [nombre_producto], [cantidad_vendida], [precio].

        - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar, actualizar, eliminar productos y salir.

        - También debe poseer opciones para calcular la venta total y por producto.

        - La opción salir elimina el .txt.
'''

class Excepcion_personalizada(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


def menu():

    print("""
          GESTIÓN DE VENTAS
          =================

          OPCIÓN    ACCIÓN

            1       AÑADIR
            2       CONSULTAR
            3       ACTUALIZAR
            4       ELIMINAR
            5       MOSTRAR VENTA POR PRODUCTO
            6       MOSTRAR VENTA TOTAL
            7       SALIR
        """)
    
def elegir_accion():
        
        operacion = input("Elige una opción: ")

        if operacion == "1":
            anadir()

        elif operacion == "2":
            consultar()
        
        elif operacion == "3":
            actualizar()
        
        elif operacion == "4":
            eliminar()

        elif operacion == "5":
            mostrar_venta_producto()

        elif operacion == "6":
            mostrar_venta_total()
        
        elif operacion == "7":
            salir()

        else:
            print("Elige una opción válida")

        return operacion

def anadir():

    archivo_escritura = io.open("ventas.txt", "a")

    try:
        nombre_producto = input("Escribe el nombre del producto: ").upper()
        cantidad = int(input("Escribe la cantidad vendida: "))
        precio = float(input("Escribe el precio de una unidad: "))
        archivo_escritura.write(f"[{nombre_producto}], [{cantidad}], [{precio}]\n")
        archivo_escritura.close()
        print("Añadido correctamente")

    except ValueError as e:
        print(f"Error. {type(e).__name__}")
        print("Introduce valores correctos")


def consultar():

    try:
        archivo_lectura = io.open("ventas.txt", "r")
        texto = archivo_lectura.read()

        if not texto:
            print("El archivo ventas está vacío")
            print("No hay ningún dato que mostrar")
            return
        
        archivo_lectura.close()
        print(texto)

    except FileNotFoundError as e:
        print(f"Error: {type(e).__name__}")
        print("Antes de consultar el archivo de ventas debes crearlo")


def actualizar():

    producto = input("Introduce el producto que desea actualizar").upper()

    try:
        archivo_lectura = io.open("ventas.txt", "r")
        lista = archivo_lectura.readlines()
        archivo_escritura = io.open("ventas.txt","w")


        for i in lista:
            if producto not in i:
                archivo_escritura.write(i)
            else: 
                opcion = input("Introduce un 1 para cambiar la cantidad y un 2 para modificar el precio: ")
                if opcion == "1":
                    nueva_cantidad = int(input("Introduce la nueva cantidad: "))
                    elementos = i.split(", ")
                    elementos[1] = f"[{nueva_cantidad}]"
                    nueva_linea = f"{elementos[0]}, {elementos[1]}, {elementos[2]}"
                    archivo_escritura.write(nueva_linea)
                    print("Nueva cantidad modificada con éxito")
                elif opcion == "2":
                    nuevo_precio = float(input("Introduce el nuevo precio: "))
                    elementos = i.split(", ")
                    elementos[2] = f"[{nuevo_precio}]"
                    nueva_linea = f"{elementos[0]}, {elementos[1]}, {elementos[2]}\n"
                    archivo_escritura.write(nueva_linea)
                    print("Nuevo precio modificado con éxito")
                else:
                    raise Excepcion_personalizada ("Error. Debes introducir un 1 o un 2")
                
        archivo_lectura.close()
        archivo_escritura.close()

    except FileNotFoundError as e:
        print(f"Error: {type(e).__name__}")
        print("Antes de consultar el archivo de ventas debes crearlo")

    except ValueError as e:
        print(f"Error. {type(e).__name__}")
        print("Introduce valores correctos")

    except Excepcion_personalizada as e:
        print(f"Error. {type(e).__name__}")
        print(e)
    

def eliminar():

    producto = input("Introduce el producto que desea eliminar").upper()
    es_borrado = False

    try:
        archivo_lectura = io.open("ventas.txt", "r")
        lista = archivo_lectura.readlines()

        archivo_escritura = io.open("ventas.txt", "w")

        for i in lista:
            if producto in i:
                es_borrado = True

        for i in lista:
            if producto not in i:
                archivo_escritura.write(i)

        if es_borrado:
            print("Se ha borrado el producto")
        else:
            print("No se ha encontrado el producto")

        archivo_lectura.close()
        archivo_escritura.close()
                
    except FileNotFoundError as e:
        print(f"Error: {type(e).__name__}")
        print("Antes de consultar el archivo de ventas debes crearlo")
 

def salir():
    try:
        os.remove("ventas.txt")
        print("Archivo de ventas borrado con éxito")

    except FileNotFoundError as e:
        print(f"Error: {type(e).__name__}")
        print("Antes de eliminar el archivo de ventas debes crearlo")

def mostrar_venta_producto():

    producto = input("Introduce el producto: ").upper()

    try:
        archivo_lectura = io.open("ventas.txt", "r")
        lista = archivo_lectura.readlines()

        venta_producto = 0

        for i in lista:
            if producto in i:
                elementos = i.split(", ")
                cantidad = int(elementos[1].replace("[","").replace("]",""))
                precio = float(elementos[2].replace("[","").replace("]",""))
                venta_producto += cantidad * precio
                print(f"La venta total del producto {producto} ha sido de {venta_producto} euros")
                archivo_lectura.close()
                return
        
        archivo_lectura.close()
        print(f"No se ha encontrado el producto {producto}")

    except FileNotFoundError as e:
        print(f"Error: {type(e).__name__}")
        print("No existe el archivo de ventas")
    
def mostrar_venta_total():
    try:
        archivo_lectura = io.open("ventas.txt", "r")
        lista = archivo_lectura.readlines()

        venta_total = 0

        for i in lista:
            elementos = i.split(", ")
            cantidad = int(elementos[1].replace("[","").replace("]",""))
            precio = float(elementos[2].replace("[","").replace("]",""))
            venta_total+=cantidad*precio

        archivo_lectura.close()
        print(f"La venta total es de {venta_total} euros")
        
    except FileNotFoundError as e:
        print(f"Error: {type(e).__name__}")
        print("No existe el archivo de ventas")


while True:
    menu()
    op = elegir_accion()
    if op == "7":
        break