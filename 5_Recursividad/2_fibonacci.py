'''
    Utiliza el concepto de recursividad para:
        Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci (la función recibe la posición).
'''

def calcular_valor(posicion):
    if posicion==0:
        return 0
    
    if posicion==1:
        return 1
    
    return calcular_valor(posicion-1) + calcular_valor(posicion-2)

print(calcular_valor(5))