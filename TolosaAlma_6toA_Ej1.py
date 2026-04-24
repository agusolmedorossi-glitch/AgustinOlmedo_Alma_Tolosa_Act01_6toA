#Ejercicio 1

class Alumno:
    def __init__(self):
        self.nombre=input("Ingrese nombre:")
        self.nota=int(input("Ingrese nota:"))
        
    def aprobar(self):
        if self.nota>=7:
            print("El alumno:",self.nombre,"Ha aprobado.")
        else:
            print("El alumno:",self.nombre,"No ha aprobado.")

alumno1=Alumno()
alumno1.aprobar()