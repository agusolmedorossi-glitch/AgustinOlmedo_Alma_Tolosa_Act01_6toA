#Ejercicio 12
import random
class Personaje():
    def __init__(self,nombre):
        self.nombre=nombre
        self.vida=100
        self.inventario=[]

    def mostrar_estado(self):
        print(f"{self.nombre}-Vida:{self.vida}")

    def agregar_objeto(self,objeto):
        self.inventario.append(objeto)
        print("Objeto guardado:",objeto)

    def ver_inventario(self):
        if self.inventario:
            print("Inventario:")
            for i in self.inventario:
                print("--",i)

        else:
            print("Inventario vacio.")

    def usar_objeto(self,objeto):
        if objeto in self.inventario:
            if objeto=="pocion":
                self.vida+=20
                print("Usaste pocion (+20 vida)")
            elif objeto=="espada":
                print("Usaste espada.")
                return 5
            elif objeto=="escudo":
                print("Usaste escudo.")
                return -5
            self.inventario.remove(objeto)

        else:
            print("No tenes ese objeto")
        return 0
    
class Animal:
    def __init__(self,nombre,vida):
        self.nombre=nombre
        self.vida=vida

    def atacar(self,personaje):
        daño=random.randint(5,15)
        personaje.vida-=daño
        print(f"{self.nombre} te ha atacado (-{daño}vida)")

def explorar(personaje):
    evento=random.randint(1,5) #Posibilidad que aparezca un lobo durante la exploración

    if evento==1:
        objeto=random.choice(["pocion","espada","escudo"])
        print("Encontraste:",objeto)
        decision=input("guardar--usar--descartar:")

        if decision=="guardar":
            personaje.agregar_objeto(objeto)

        elif decision=="usar":
            personaje.usar_objeto(objeto)

        else:
            print("Objeto descartado")

    else:
        print("Ha aparecido un lobo")
        animal=Animal("Lobo",40)
        lucha(personaje,animal)

def lucha(personaje,animal):
    while personaje.vida>0 and animal.vida>0: #Mientras que el personaje y el lobo sigan vivos, la batalla no termina

        print("--Lucha--")
        print(f"Tu vida:{personaje.vida}")
        print(f"Vida del animal:{animal.vida}")
        
        print("1. Atacar (Usar tus puños)")
        print("2. Usar objeto")
        print("3. Huir")
        opcion=input("Elija una opción:")
        bonus=0  #El bonus es el efecto extra que tienen los objeto como la espada y el escudo

        if opcion=="1":
            daño=10
            posible_daño_recibido=random.randint(1,5)
            if posible_daño_recibido==1:
                print("Tu ataque ha sido esquivado y el lobo te ha atacado (-30 vida).")
                personaje.vida-=30
            else:
                animal.vida-=daño
                print(f"Has atacado al lobo. Le has quitado {daño} de vida")

        elif opcion=="2":
            personaje.ver_inventario()
            obj=input("Elije lo que usarás:")
            bonus=personaje.usar_objeto(obj)

            if bonus>0: #Mayor que 0 para que la pocion no aplique aquí. Solo escudo y espada
                daño=random.randint(10,15)+bonus #Se le agrega el bonus de la espada o el escudo
                animal.vida-=daño
                print(f"Atacaste con un bonus (-{daño} vida)")

        elif opcion=="3":
            escapar=random.randint(1,10) #En el caso que se elija escapar hay una posibilidad de 1 en 10 que haya un game over al instante, para que el juego no sea tan lineal
            if escapar==1:
                print("El lobo te ha alcanzado. GAME OVER :(")
                personaje.vida-=100
            elif escapar==2: #También se agrega la posibilidad de escapar, pero aún así sufriendo un poco de daño
                print("Has escapado pero el lobo te ha hecho un poco de daño (-15 vida)")
                personaje.vida-=15
                return

            else:
                print("Has escapado")
                return
        else:
            print("Opción invalida.")

        if animal.vida>0:
            daño=random.randint(5,15)+bonus #El daño se elige de manera aleatoria
            if daño<0:
                daño=0 #Para evitar números negativos
            personaje.vida-=daño
            print(f"El animal te ataco -{daño} vida")

    if personaje.vida>0:
        print("Has derrotado al lobo")

    else:
        print("Has perdido. GAME OVER")

def mostrar_menu():
    print("--Aventura--")
    print("1. Explorar")
    print("2. Ver inventario")
    print("3. Ver estado")
    print("4. Salir")


#PROGRAMA PRINCIPAL
jugador=Personaje(input("Ingrese su nombre:"))
opcion=""

while opcion!="4" and jugador.vida> 0:
    mostrar_menu()
    opcion=input("Ingrese una opción:")

    if opcion=="1":
        explorar(jugador)

    elif opcion=="2":
        jugador.ver_inventario()

    elif opcion=="3":
        jugador.mostrar_estado()

    elif opcion=="4":
        print("Fin de la aventura.")

    else:
        print("Opción invalida.")