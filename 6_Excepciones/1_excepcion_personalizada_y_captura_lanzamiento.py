'''
    Crea una función que sea capaz de procesar parámetros, pero que también pueda lanzar 3 tipos diferentes de excepciones 
    (una de ellas tiene que corresponderse con un tipo de excepción creada por nosotros de manera personalizada, y debe ser
    lanzada de manera manual) en caso de error.

    - Captura todas las excepciones desde el lugar donde llamas a la función.
    - Imprime el tipo de error.
    - Imprime si no se ha producido ningún error.
    - Imprime que la ejecución ha finalizado.
'''

#   Creación de la excepción personalizada

class Numero_negativo_exception(Exception):

    def __init__(self, mensaje):
        super().__init__(mensaje)

    

#   Función

def dividir():

    numero_uno = int(input("Escribe el primer número entero: "))
    if numero_uno < 0:
        raise Numero_negativo_exception("El primer número debe ser positivo")
    
    numero_dos = int(input("Escribe el segundo número entero: "))
    if numero_dos < 0:
        raise Numero_negativo_exception("El segundo número debe ser positivo")
    
    return numero_uno // numero_dos



#   Main

try:
    resultado = dividir()
    print(f"El resultado de la división entera es {resultado}")
    print("No se ha producido ningún error")

except ArithmeticError as e:
    print(f"Tipo de error: {type(e).__name__}")
    print("No se puede dividir por 0")

except ValueError as e:
    print(f"Tipo de error: {type(e).__name__}")
    print("Introduce un número entero")

except Numero_negativo_exception as e:
    print(f"Tipo de error: {type(e).__name__}")
    print(f"{e}")

finally:
    print("Ejecución de la función dividir finalizada")

