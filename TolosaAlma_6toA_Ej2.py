#Ejercicio 2

class Persona:
    def __init__(self):
        self.nombre=input("Ingrese un nombre:")
        self.edad=int(input("Ingrese la edad:"))
        
    def mayor_edad(self):
        if self.edad>=18:
            print("La persona",self.nombre,"es mayor de edad.")
            
        else:
            print("La persona",self.nombre,"no es mayor de edad.")
            
persona1=Persona()
persona1.mayor_edad()
