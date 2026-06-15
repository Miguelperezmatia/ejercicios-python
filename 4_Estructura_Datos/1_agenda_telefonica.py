'''
    Crea una agenda de contactos por terminal.

    Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
    Cada contacto debe tener un nombre y un número de teléfono.

    El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación los datos necesarios
    para llevarla a cabo.

    El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos 

    También se debe proponer una operación de finalización del programa.
'''

agenda = {"Nacho":635893572, "Miguel":644400759}

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
        operacion = int(input("Introuce la operación que quieres realizar (del 1 al 5): "))
        if operacion >= 1 and operacion <= 5:
            return operacion
        else:
            print("Operación incorrecta")
            print("Inténtalo de nuevo\n")


def busqueda(agenda):
    contacto = input("Introduce el contacto a buscar: \n")
    if contacto in agenda:
        print(f"El contacto {contacto} tiene el número de teléfono {agenda[contacto]}")
    else:
        print(f"El contacto {contacto} no existe")

def eliminacion(agenda):
    contacto = input("Introduce el contacto a eliminar: \n")
    if contacto in agenda:
        del agenda[contacto]
        print(f"Contacto {contacto} eliminado correctamente")
    else:
        print(f"El contacto {contacto} no existe")
    print(agenda)



def realizar_accion(operacion):
    if operacion == 1:
        busqueda(agenda)
    elif operacion == 2:
        insercion()
    elif operacion == 3:
        actualizacion()
    elif operacion == 4:
        eliminacion(agenda)
    else:
        salir()

menu()
operacion = introducir_operacion()
realizar_accion(operacion)