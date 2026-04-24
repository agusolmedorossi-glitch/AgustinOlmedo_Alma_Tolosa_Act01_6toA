#Ejercicio 14

import random

class Torre:
    def __init__(self):
        self.vida=100
        self.defensa=5
        self.recursos=20

    def mostrar_estado(self):
        print(f"Vida: {self.vida}- Defensa: {self.defensa}- Recursos: {self.recursos}")

    def reparar(self):
        if self.recursos>=10:
            self.vida+=15
            self.recursos-=10
            print("La torre se ha reparado (+15 vida)")
        
        else:
            print("No hay suficientes recursos")

    def mejorar_defensa(self):
        if self.recursos>=15:
            self.defensa+=3
            self.recursos-=15
            print("Mejoraste la defensa de la torre (+3)")
        else:
            print("No hay suficientes recursos")

    def atacar_enemigo(self):
        daño=random.randint(10,20)
        print(f"Atacaste al enemigo (-{daño} vida)")
        return daño
    
    def recibir_daño(self,daño):
        daño_real=daño-self.defensa
        if daño_real<0:
            daño=0
        self.vida-=daño_real
        print(f"La torre recibio {daño_real} de daño")

class Enemigo:
    def __init__(self):
        self.vida=random.randint(20,40)

    def atacar(self,torre):
        daño=random.randint(5,15)

        if random.randint(1,4)==1:
            daño*=2
            print("Daño multiplicado.")
        torre.recibir_daño(daño)

    def recibir_daño(self,daño):
        self.vida-=daño

#PROGRAMA PRINCIPAL
torre=Torre()
ronda=1
rondas_totales=5
while torre.vida>0 and ronda<=rondas_totales:
    print(f"---Ronda: {ronda}---")
    enemigo=Enemigo()

    while enemigo.vida>0 and torre.vida>0:
        print("1. Atacar")
        print("2. Reparar torre")
        print("3. Mejorar defensa")

        opcion=input("Elija una opción:")
        if opcion=="1":
            daño=torre.atacar_enemigo()
            enemigo.recibir_daño(daño)

        elif opcion=="2":
            torre.reparar()

        else:
            print("Opción inválida.")
    
        if enemigo.vida>0:
            enemigo.atacar(torre)

    if torre.vida>0:
        print("Ganaste")
        torre.recursos+=10
        print("Ganaste recursos (+10)")
    torre.mostrar_estado()
    ronda+=1
print("La torre ha caído. Game over")
