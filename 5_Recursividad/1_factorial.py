'''
    Utiliza el concepto de recursividad para:
        Calcular el factorial de un número concreto (la función recibe ese número).
'''

def calcular_factorial(numero):
    
    if numero == 1 or numero == 0:
        return 1

    return numero * calcular_factorial(numero-1)
