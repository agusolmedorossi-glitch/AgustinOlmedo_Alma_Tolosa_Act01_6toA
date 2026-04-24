#Ejercicio 10:
import random
class Auto():
    def __init__(self, nombre):
        self.nombre= nombre
        self.posicion=0
    
    def avanzar(self,metros):
        fallo= random.randint(1,5)
        if fallo == 1:
            print(f"{self.nombre} tuvo un desperfecto y no pudo avanzar.")
        else:
            self.posicion+=metros
            print(f"{self.nombre} avanzó {metros} posiciones")

    def perder_posiciones(self,metros):
        self.posicion-=metros

    def mostrar_posicion(self):
        print(f"{self.nombre} se encuentra en la posición:{self.posicion}")

#PROGRAMA PRINCIPAL
meta=100
vueltas=0
jugador=Auto("Tu auto")

auto1=Auto("Auto 1.")
auto2=Auto("Auto 2.")

while jugador.posicion < meta and auto1.posicion < meta and auto2.posicion < meta:
    curva=random.randint(1,3)

    if curva==1:
        print("Se acerca una curva.")
        print("1. Bajar velocidad")
        print("2. Subir velocidad (Riesgo de choque)")

        opcion=input("Elija una opción:")

        if opcion=="1":
            jugador.avanzar(2)

        elif opcion=="2":
            choque= random.randint(1,3)

            if choque==1:
                print("Chocaste.Has perdido posiciones")
                perdida_posicion=random.randint(5,15)
                jugador.perder_posiciones(perdida_posicion)
                print(f"Retrocediste {perdida_posicion} posiciones")

            else:
                jugador.avanzar(20)

        else:
            print("Opcion no valida")

    else:
        print("1. Acelerar poco (5)")
        print("2. Acelerar mucho (10)")

        opcion= input("Elija una opcion:")

        if opcion=="1":
            jugador.avanzar(5)

        elif opcion=="2":
            falla_motor=random.randint(1,3)
            if falla_motor==1:
                print("El motor ha fallado. Has perdido posiciones")
                perdida_posicion=random.randint(5,15)
                jugador.perder_posiciones(perdida_posicion)
                print(f"Retrocediste {perdida_posicion} posiciones")
            
            else:
                jugador.avanzar(10)
    vueltas+=1
    auto1.avanzar(random.randint(2,20))
    auto2.avanzar(random.randint(2,20))
    print(f"Vuelta número:{vueltas}")
    jugador.mostrar_posicion()
    auto1.mostrar_posicion()
    auto2.mostrar_posicion()
print("RESULTADO DE LA CARRERA")

if jugador.posicion>=meta:
    print("Ganaste la carrera")
elif auto1.posicion>=meta:
    print("El auto 1 ha ganado la carrera. GAME OVER")

else:
    print("El auto 2 ha ganado la carrera. GAME OVER")