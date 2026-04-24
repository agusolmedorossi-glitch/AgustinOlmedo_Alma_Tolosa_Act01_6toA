#Ejercicio 11
import random

class Hechicero:
    def __init__(self, nombre):
        self.nombre= nombre
        self.vida=100
        self.energia=100
        self.estado="Normal"
        self.enfriamiento=0
        self.pocion_energia=5

    def aplicar_estado(self):
        if self.estado=="quemado":
            self.vida-=5
            print(f"{self.nombre} se esta quemando (-5 vida)")

    def puede_actuar(self):
        if self.estado=="paralizado":
            if random.randint(1,2)==1:
                print(f"{self.nombre} esta electrocutado y su saltea su turno.")
                return False
        return True
    
    def ataque_basico(self,enemigo):
        daño=10
        evento=random.randint(1,5)

        if evento==1:
            print("El hechicero esquivo el ataque.")

        elif evento==2:
            daño=20
            print("Golpe crítico.")

        enemigo.vida-=daño
        print(f"{self.nombre} hizo un ataque básico (-10 vida)")
        estado=random.randint(1,4)
        if estado==1:
            enemigo.estado="quemado"
            print("El enemigo se esta quemando")

        elif estado==2:
            enemigo.estado="paralizado"
            print("El enemigo quedo electrocutado.")

    def hechizo_fuerte(self,enemigo):
        if self.enfriamiento>0:
            print("Espere para utilizar nuevamente")
            return

        if self.energia<15:
            print("No hay energía suficiente")
            return
            
        self.energia-=15
        self.enfriamiento=3

        daño=25
        evento=random.randint(1,5)

        if evento==1:
            print("El hechizo fallo")
            return
        elif evento==2:
            daño=40
            print("Hechizo potenciado.")
        elif evento==3:
            print("El daño se invirtió")
            self.vida-=daño
            return
            
        enemigo.vida-=daño
        print(f"{self.nombre} lanzo un hechizo fuerte (-25 vida)")

    def curarse(self):
        if self.energia>=10:
            self.vida+=15
            self.energia-=10
            print(f"{self.nombre} se curó (+15 vida)")

        else:
            print("No tienes energía")

    def recargar_energia(self):
        if self.pocion_energia>0:
            self.energia+=10
            print(f"{self.nombre} recargo energía (+10 energía)")
            self.pocion_energia-=1
        else:
            print("No tienes pociones para recargar energía")

    def bajar_enfriamiento(self):
        if self.enfriamiento>0:
            self.enfriamiento-=1

    def mostrar_estado(self):
        print(f"{self.nombre}-Vida:{self.vida}-Energía:{self.energia}-Estado:{self.estado}-Enfriamiento:{self.enfriamiento}")

#PROGRAMA PRINCIPAL
jugador=Hechicero("Tu hechicero")
enemigo=Hechicero("Hechicero enemigo")
ronda=0
while jugador.vida>0 and enemigo.vida>0:
    ronda+=1
    jugador.aplicar_estado()
    enemigo.aplicar_estado()
    jugador.bajar_enfriamiento()
    enemigo.bajar_enfriamiento()

    if jugador.puede_actuar():
        print("La lucha ha comenzado. Elige tu movimiento")
        print("1. Ataque básico.")
        print("2. Hechizo fuerte")
        print("3. Curarse")
        print("4. Recargar energía")

        opcion=input("Eliga una opcion:")

        if opcion=="1":
            jugador.ataque_basico(enemigo)

        elif opcion=="2":
            jugador.hechizo_fuerte(enemigo)

        elif opcion=="3":
            jugador.curarse()

        elif opcion=="4":
            jugador.recargar_energia()

        else:
            print("Opción invalida")
    if enemigo.vida<=0:
        break

    if enemigo.puede_actuar():
        accion=random.randint(1,4)
        if accion==1:
            enemigo.ataque_basico(jugador)
        elif accion==2:
            enemigo.hechizo_fuerte(jugador)
        elif accion==3:
            enemigo.curarse()
        else:
            enemigo.recargar_energia()

    print("Ronda número:",ronda)
    print("---Estado jugadores--")
    jugador.mostrar_estado()
    enemigo.mostrar_estado()

if jugador.vida>0:
    print("Haz ganado")

else:
    print("GAME OVER")