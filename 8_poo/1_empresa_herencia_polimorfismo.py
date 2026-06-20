import time

'''
    Implementa la jerarquía de una empresa de desarrollo formada por Empleados que pueden ser Gerentes o Programadores.

    Cada empleado tiene un identificador y un nombre.
    Dependiendo de su labor, tienen propiedades y funciones exclusivas de su,actividad, y almacenan los empleados a su cargo.
'''

#   Clases

class Empleado():
    
    def __init__(self, identificador, nombre):
        self._identificador = identificador
        self._nombre = nombre

    def trabajar(self):
        print("Estoy realizando labores de oficina")

class Programador(Empleado):

    def __init__(self, identificador, nombre, lenguaje, sistema_operativo, tareas):
        super().__init__(identificador, nombre)  
        self.lenguaje_favorito = lenguaje
        self.sistema_operativo = sistema_operativo  
        self.tareas = tareas
        self.lenguajes = [lenguaje]

    def trabajar(self):
        print("Estoy escribiendo código y analizando que todo funciona de forma correcta")

    def escribir_codigo_proyecto(self, proyecto):  
        print(f"Estoy escribiendo código {self.lenguaje_favorito} en el proyecto {proyecto}")

    def completar_tarea(self):
        print("Completando tarea...")
        time.sleep(3)
        self.tareas+=1
        print("Tarea completada con éxito")

    def aprender_lenguaje(self,lenguaje):

        if lenguaje not in self.lenguajes:
            print(f"Estoy aprendiendo el lenguaje {lenguaje}")
            time.sleep(5)
            print("Lenguaje aprendido")
            self.lenguajes.append(lenguaje)
            return 
        
        print(f"El lenguaje {lenguaje} lo tengo dominado")


class Gerente(Empleado):

    def __init__(self, identificador, nombre, departamento, presupuesto):
        super().__init__(identificador, nombre)
        self.departamento = departamento
        self.presupuesto = presupuesto
        self.equipo = []

    def trabajar(self):
        print("Realizando labores de gestión")

    def agregar_empleado(self, empleado):
        print(f"Añadiendo al empleado {empleado._nombre}")
        time.sleep(1)
        self.equipo.append(empleado) 

    def mostrar_equipo(self):
        if not self.equipo:
            print("El equipo está vacío")
            return
        
        for empleado in self.equipo:
            print(f"{empleado._nombre}, {empleado._identificador}")


#   Main

empleado = Empleado(1, "Juan")
programador = Programador(56, "Carlos", "Python", "Linux", 0)
gerente = Gerente(342, "Pepe", "IT", 10000)

#   Polimorfismo

empleado.trabajar()
programador.trabajar()
gerente.trabajar()


#   Funciones específicas

programador.aprender_lenguaje("Java")
print(programador.lenguajes)

gerente.agregar_empleado(empleado)
gerente.agregar_empleado(programador)
gerente.mostrar_equipo()

