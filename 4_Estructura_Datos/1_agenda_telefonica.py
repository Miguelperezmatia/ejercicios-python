'''
    Crea una agenda de contactos por terminal.

    Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
    Cada contacto debe tener un nombre y un número de teléfono.

    El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación los datos necesarios
    para llevarla a cabo.

    El programa no puede dejar introducir números de teléfono no numéricos y el numero debe ser de 9 dígitos 

    También se debe proponer una operación de finalización del programa.
'''

agenda = {"Nacho":"635893572", "Miguel":"849305839"}

print(agenda.values())


def menu():
    print("""
            AGENDA DE CONTACTOS 
          ***********************

          OPCIÓN    ACCIÓN
          
            1       BÚSQUEDA
            2       INSERCIÓN
            3       ACTUALIZACIÓN
            4       ELIMINACIÓN
            5       SALIR
          """)


def introducir_operacion():
    while True:
        try:
            operacion = int(input("Introuce la operación que quieres realizar (del 1 al 5): "))
            if operacion >= 1 and operacion <= 5:
                return operacion
            else:
                print("Operación incorrecta")
                print("Inténtalo de nuevo\n")

        except ValueError as e:
            print(f"Error: {type(e).__name__}. Inténtalo de nuevo")

        
       

def busqueda(agenda):
    contacto = input("Introduce el contacto a buscar: \n")
    if contacto in agenda:
        print(f"El contacto {contacto} tiene el número de teléfono {agenda[contacto]}")
    else:
        print(f"El contacto {contacto} no existe")

    print(agenda)

def insercion(agenda):
    contacto =  input("Introduce el contacto a insertar: \n")
    numero = input("Introduce su número de teléfono: \n")

    while True:
        if numero.isdigit() and len(numero) == 9:
            if numero not in agenda.values():
                break
            else:
                print("El número de teléfono introducido ya existe")
                numero = input("Introduce un número de teléfono válido: \n")

        else: 
            print("Introduce un número de teléfono válido")
            numero = input("Inténtalo de nuevo: \n")

    agenda[contacto] = numero
    print(f"Se ha añadido al {contacto} con el numero de telefono {numero} correctamente")
    print(agenda)

def actualizacion(agenda):

    n = input("Introduce un 1 para cambiar el nombre o un 2 para cambiar un número de teléfono: ")

    while True:
        if n == "1":
            actualizar_nombre(agenda)
            break
        elif n == "2":
            actualizar_numero(agenda)
            break
        else:
            print("Debes escribir un 1 o un 2")
            n = input("Introduce un 1 para cambiar el nombre o un 2 para cambiar un número de teléfono: ")

 

def actualizar_nombre(agenda):
    contacto = input("Introduce el contacto a actualizar: \n")
    if contacto in agenda:
        numero = agenda[contacto]
        nuevo_nombre = input("Introduce el nuevo nombre: \n")
        del agenda[contacto]
        agenda[nuevo_nombre] = numero
        print(f"El contacto {contacto} ha sido reenombrado a {nuevo_nombre}")

    else:
        print(f"No existe un contacto llamado {contacto}")

    print(agenda)

def actualizar_numero(agenda):
    numero = input("Introduce el numero a actualizar: ")

    if numero.isdigit():
        if len(numero) == 9:
            if numero in agenda.values():
                numero_nuevo = input("Introduce el numero nuevo: ")
                if validar_numero(numero_nuevo):
                    contacto = encontrar_contacto_asociado(agenda, numero)
                    del agenda[contacto]
                    agenda[contacto] = numero_nuevo

                    print(f"El numero de telefono {numero} del contacto {contacto} ha sido cambiado a {numero_nuevo}")
                else:
                    print("Debes introducir un número de teléfono válido")

        else:
            print("El número de teléfono debe tener una longitud de 9 dígitos")
    else:
        print("Debes introducir un número de teléfono válido")

def validar_numero(numero):
    return numero.isdigit() and len(numero) == 9

def encontrar_contacto_asociado(agenda, numero):

    for c in agenda:
        if agenda[c] == numero:
            return c 


def eliminacion(agenda):
    contacto = input("Introduce el contacto a eliminar: \n")
    if contacto in agenda:
        del agenda[contacto]
        print(f"Contacto {contacto} eliminado correctamente")
    else:
        print(f"El contacto {contacto} no existe")

    print(agenda)

def salir():
    print("Cerrando agenda...")
    exit()


def realizar_accion(operacion):
    if operacion == 1:
        busqueda(agenda)
    elif operacion == 2:
        insercion(agenda)
    elif operacion == 3:
        actualizacion(agenda)
    elif operacion == 4:
        eliminacion(agenda)
    else:
        salir()


#   Main

while True:
    menu()
    operacion = introducir_operacion()
    realizar_accion(operacion)
    if operacion < 1 or operacion > 4:
        break