
#Ejercicio 8

class Personaje():
    def __init__(self, vida, ataque):
        self.nombre_jugador=input("Ingrese el nombre de su personaje:")
        self.vida=100
        self.ataque=20

    def atacar(self,otro):
        print(f"{self.nombre_jugador} ataca a {otro.nombre}")
        otro.vida-=self.ataque

    def vivo(self):
        return self.vida>0

    def mostrar_estado(self):
        print(f"{self.nombre_jugador} tiene {self.vida} de vida")
        
#PROGRAMA PRINCIPAL
jugador=Personaje()
enemigo=Personaje()

while jugador.vivo and enemigo.vivo():
    accion=input("Ingrese accion (1 para atacar):")

    if accion=="1":
        jugador.atacar(enemigo)

    else:
        print("Vuelva a ingresar.")

    jugador.mostrar_estado()
    enemigo.mostrar_estado()

    if not enemigo.vivo():
        print("Ganaste. MUY BIENNN")
    else:
        enemigo.atacar(jugador)
    jugador.mostrar_estado()
    enemigo.mostrar_estado()

    if not jugador.vivo():
        print("GAME OVER :(")
