'''

El Museo del Prado de Madrid te ha pedido un programa sencillo para automatizar el cobro en taquilla. 
El programa debe calcular el precio final de la entrada basándose en la edad del visitante y si posee el Carné Joven de la Comunidad de Madrid.

Especificaciones técnicas:

Precio Base: Define una variable llamada PRECIO_GENERAL con un valor de 15 (euros).
Entrada de datos: El programa debe pedir por consola:
La edad del usuario (número entero).
Si tiene Carné Joven (el usuario responderá "si" o "no").

Lógica de Descuentos:
Menores de 18 años: La entrada es gratuita (0€).
Mayores de 65 años (incluido): Tienen un 50% de descuento sobre el precio general.
Usuarios con Carné Joven: Si no cumplen ninguna de las anteriores pero tienen el carné, se les aplica
un descuento fijo de 5€ (pagarían 10€).
Resto de casos: Pagan el precio general.

Formato de salida:
El programa debe imprimir un mensaje final indicando el precio que debe pagar el cliente.
'''

PRECIO_GENERAL = 15
edad = int(input("Escribe tu edad: "))
tener_carne_joven = input("Escribe si tienes o no carné joven (si / no): ")
descuento = 0
precio_total = 0


if edad < 18:
        precio_total = 0
elif edad >= 65:
        descuento = 0.50 * PRECIO_GENERAL
        precio_total = PRECIO_GENERAL - descuento
elif tener_carne_joven=="si":
        descuento=5
        precio_total=PRECIO_GENERAL-descuento
else:
        precio_total=PRECIO_GENERAL

print(f"En total debes pagar {precio_total} euros.")
