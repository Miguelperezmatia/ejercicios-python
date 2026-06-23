from multiprocessing import Process
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
    - Las funciones C, B y A se ejecutan en paralelo.
    - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
'''




#   NOTA DE APRENDIZAJE

'''
    Aunque las pausas con time.sleep() simulan operaciones I/O (entrada/salida) que se manejan de forma más eficiente con hilos
    (threading) o asincronía (asyncio), este script utiliza 'multiprocessing' con fines estrictamente didácticos. 
    El objetivo es practicar la sintaxis, la creación y la sincronización (join) de procesos independientes.
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


def main():

    proceso_uno = Process(target=saludar, name="C", args = ("C", 3))
    proceso_dos = Process(target=saludar, name="B", args = ("B", 2))
    proceso_tres = Process(target=saludar, name="A", args = ("A", 1))
    proceso_cuatro = Process(target=saludar, name="D", args = ("D", 1))

    proceso_uno.start()
    proceso_dos.start()
    proceso_tres.start()

    proceso_uno.join()
    proceso_dos.join()
    proceso_tres.join()

    proceso_cuatro.start()
    proceso_cuatro.join()


if __name__ == "__main__":
    main()