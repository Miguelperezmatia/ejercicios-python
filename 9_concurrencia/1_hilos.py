import threading
import time 

'''
    Crea un programa capaz de ejecutar de manera asíncrona una función que tardará en finalizar un número concreto de
    segundos parametrizables. También debes poder asignarle un nombre. La función imprime su nombre, cuándo empieza, 
    el tiempo que durará su ejecución y cuando finaliza.

    Utilizando el concepto de asincronía y la función anterior, crea el siguiente programa que ejecuta en este orden:

    - Una función C que dura 3 segundos.
    - Una función B que dura 2 segundos.
    - Una función A que dura 1 segundo.
    - Una función D que dura 1 segundo.
    - Las funciones C, B y A se ejecutan en paralelo, es decir, al mismo tiempo o en su defecto que de la sensación de simultaneidad.
    - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
'''

def saludar(nombre, segundos):

    inicio = time.perf_counter()

    print(f"Iniciando {nombre}")
    print(f"Mi nombre es {nombre} y duraré un total de {segundos} segundos aproximadamente")
    time.sleep(segundos)
    print(f"Finalizando {nombre}")

    final = time.perf_counter()
    tiempo_total = final - inicio

    print(f"La funcion {nombre} ha tardado en ejecutarse un total de {tiempo_total} segundos.")



hilo_uno = threading.Thread(target=saludar, name="C", args=("C", 3))
hilo_dos = threading.Thread(target=saludar, name="B", args=("B", 2))
hilo_tres = threading.Thread(target=saludar, name="A", args=("A", 1))
hilo_cuatro = threading.Thread(target=saludar, name="D", args=("D", 1))

hilo_uno.start()
hilo_dos.start()
hilo_tres.start()

hilo_uno.join()
hilo_dos.join()
hilo_tres.join()

hilo_cuatro.start()
hilo_cuatro.join()





