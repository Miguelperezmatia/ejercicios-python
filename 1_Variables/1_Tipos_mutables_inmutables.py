'''
    Crea dos funciones que reciban dos parámetros cada una, definidos previamente en variables globales. 

    Caso 1 (Tipos Inmutables):  La primera función recibirá dos tipos de datos inmutables (por ejemplo, cadenas de texto).
    Caso 2 (Tipos Mutables):    La segunda función recibirá dos tipos de datos mutables (por ejemplo, listas).

    Ambas funciones deben intercambiar los valores de los parámetros en su interior, retornarlos y asignar este retorno a dos 
    variables nuevas.

    A continuación, el programa debe imprimir el valor de las variables originales y de las nuevas, comprobando que:

    1. Se ha invertido el valor en las variables nuevas.
    2. Se ha **conservado el valor original** en las primeras, demostrando que al realizar una reasignación local 
       (con el símbolo `=`), Python protege el dato original incluso cuando se utilizan tipos mutables.
'''

#   Inmutables

cadena_vieja_uno = "Hola"
cadena_vieja_dos = "Adios"

def intercambio_inmutables(cadena_uno, cadena_dos):
    aux = cadena_uno
    cadena_uno = cadena_dos
    cadena_dos = aux

    return cadena_uno, cadena_dos

cadena_nueva_uno, cadena_nueva_dos = intercambio_inmutables(cadena_vieja_uno, cadena_vieja_dos)

print(f"La primera cadena nueva es {cadena_nueva_uno} y la primera cadena antigua es {cadena_vieja_uno}")
print(f"La segunda cadena nueva es {cadena_nueva_dos} y la segunda cadena antigua es {cadena_vieja_dos}\n")


#   Mutables

lista_vieja_uno = [30, True, "Hola"]
lista_vieja_dos = [False, 66, "Adios"]

def intercambio_mutables(lista_uno, lista_dos):
    aux = lista_uno
    lista_uno = lista_dos
    lista_dos = aux

    return lista_uno, lista_dos

lista_nueva_uno, lista_nueva_dos = intercambio_mutables(lista_vieja_uno, lista_vieja_dos)

print(f"La primera lista nueva es {lista_nueva_uno} y la primera lista antigua es {lista_vieja_uno}")
print(f"La segunda lista nueva es {lista_nueva_dos} y la segunda lista antigua es {lista_vieja_dos}")



