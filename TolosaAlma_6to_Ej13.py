#Ejercicio 13
import random

class Jugador:
    def __init__(self, nombre):
        self.nombre=nombre
        self.puntaje=0

    def lanzar_dados(self):
        dado=random.randint(1,6)
        self.puntaje+=dado
        print(f"{self.nombre} saco: {dado}")
    
    def mostrar_puntaje(self):
        print(f"{self.nombre} tiene:{self.puntaje}")

#PROGRAMA PRINCIPAL
jugador=Jugador(input("Ingrese su nombre:"))
jugador1=Jugador("Jugador 1")
jugador2=Jugador("Jugador 2")

rondas=5
ronda_actual=1

while ronda_actual<=rondas:
    print(f"--Ronda:{ronda_actual}---")
    input("Presione ENTER para lanzar el dado")

    jugador.lanzar_dados()
    jugador1.lanzar_dados()
    jugador2.lanzar_dados()
    print("--Puntajes--")
    jugador.mostrar_puntaje()
    jugador1.mostrar_puntaje()
    jugador2.mostrar_puntaje()

    ronda_actual+=1

print("--Resultado final--")
jugador.mostrar_puntaje()
jugador1.mostrar_puntaje()
jugador2.mostrar_puntaje()

if jugador.puntaje>jugador1.puntaje and jugador.puntaje>jugador2.puntaje:
    print("Ganaste")
elif jugador1.puntaje>jugador2.puntaje:
    print("Jugador 1 ha ganado. Game over")
else:
    print("Ha ganado el jugador 2. Game over")