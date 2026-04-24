#Ejercicio 9
import random

class Explorador():
    def __init__(self):
        self.jugador = input("Ingrese su nombre: ")
        self.vida = 100
        self.monedas = 0
        self.gemas = 0

    def recolectar(self, monedas, gemas):
        self.monedas += monedas
        self.gemas += gemas
        print("Recolectaste:", monedas, "monedas y", gemas, "gemas")

    def daño_recibido(self, daño):
        self.vida -= daño
        print("Recibiste", daño, "de daño")

    def estado_jugador(self):
        print("Jugador:", self.jugador)
        print("Vida:", self.vida)
        print("Monedas:", self.monedas)
        print("Gemas:", self.gemas)



class Cofre():
    def __init__(self):
        self.abierto = False
        #Cant. random de objetos que puede haber en un cofre
        self.recursos = {
            "monedas": random.randint(5, 20),
            "gemas": random.randint(0, 5)
        }

    def abrir(self, jugador):
        if self.abierto:
            print("El cofre ya está abierto")
            return

        self.abierto = True
        print("El cofre se ha abierto")

        if random.randint(1, 10) <= 3: # Posible trampa o recompensa
            daño = random.randint(5, 15)
            print("Una serpiente te atacó")
            jugador.daño_recibido(daño)
        else:
            print("Encontraste un tesoro")
            monedas = self.recursos["monedas"]
            gemas = self.recursos["gemas"]
            jugador.recolectar(monedas, gemas)

    def mostrar_estado(self):
        if not self.abierto:
            print("El cofre está cerrado")
        else:
            print("El cofre ya fue abierto.")


# PROGRAMA PRINCIPAL
jugador = Explorador()

cofre = Cofre()

opcion = ""

while opcion != "3" and jugador.vida > 0:
    print("\n--- MENÚ ---")
    print("1. Abrir cofre")
    print("2. Ver estado")
    print("3. Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        cofre.abrir(jugador)

    elif opcion == "2":
        jugador.estado_jugador()

    elif opcion == "3":
        print("Fin del juego")

    else:
        print("Opción inválida")


if jugador.vida <= 0:
    print("El jugador ha muerto. Game over")