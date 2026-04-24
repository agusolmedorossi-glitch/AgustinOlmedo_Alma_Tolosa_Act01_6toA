""""
import random
class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre 
        self.salud = 100
        self.golpe_critico = 1
    def mostrar(self):
        print(f"{self.nombre}: {self.salud} HP")
    def atacar(self, enemigo):
        daño = random.randint(10, 25)
        enemigo.salud -= daño
        print(f"{self.nombre} ataco causando {daño} de daño.")
    def curarse(self):
        curacion = random.randint(10, 20)
        self.salud += curacion
        if self.salud > 100:
            self.salud = 100
        print(f"{self.nombre} se curo {curacion} de vida.")
    def ataque_critico(self, enemigo):
        if self.golpe_critico == 1:
            self.golpe_critico = 0
            daño_critico = 50
            enemigo.salud -= daño_critico
            print(f"{self.nombre} causo {daño_critico} de daño.")
        else:
            print("estas cansado y pierdes el turno.")

class Enemigo(Personaje):
    def turno_automatico(self, jugador):
        decision = random.choice(["A", "S"])
        if decision == "A":
            daño = random.randint(5, 15)
            jugador.salud -= daño
            print(f"el enemigo ataco causando {daño} de daño.")
        else:
            self.curarse()
class Juego:
    def __init__(self):
        nombre_p = input("ingrese el nombre del aventurero: ")
        self.jugador = Personaje(nombre_p)
        self.rival = Enemigo("chatgpt.exe")
    def accion(self):
        print(f"{self.jugador.nombre} vs {self.rival.nombre}")
        while self.jugador.salud > 0 and self.rival.salud > 0:
            self.jugador.mostrar()
            self.rival.mostrar()
            print("A: Atacar  S: Curar  R: Crítico")
            opcion = input(": ").capitalize()
            if opcion == "A":
                self.jugador.atacar(self.rival)
            elif opcion == "S":
                self.jugador.curarse()
            elif opcion == "R":
                self.jugador.ataque_critico(self.rival)
            else:
                print("te quedaste paralizado y perdiste el turno.")
            if self.rival.salud <= 0:
                print(f"felicidades {self.jugador.nombre} ganaste")
                break
            print("turno del rival")
            self.rival.turno_automatico(self.jugador)
            if self.jugador.salud <= 0:
                print("NO TE MUERAAAAS")
                break
juego = Juego()
juego.accion()
""""
""""
import random
class personaje:
    def __init__(self, nombre):
        self.nombre_p = nombre
        self.monedas = 0
class Cofre: 
    def __init__(self):
        self.estado = "cerrado" 
        self.cantidad = random.randint(5, 25)
    def abrir(self):
        if self.estado == "abierto":
            print("El cofre ya está abierto.")
            return
        if random.randint(0, 1) == 1:
            self.estado = "abierto"
            print("¡Lograste abrir el papuacofre!")
        else:
            print("No lograste abrirlo... está bien duro.")
class Juego:
    def __init__(self):
        nombree = input("Ingrese el nombre del aventurero: ")
        self.prota = personaje(nombree)
    def exploracion(self):
        while True:
            print(Encuentras un cofre en la oscuridad")
            cofre_actual = Cofre()
            while True:
                print(f"Monedas actuales: {self.prota.monedas}")
                print("1_ Intentar abrir el cofre")
                print("2_ Tomar las monedas")
                print("3_ Seguir explorando (buscar otro cofre)")
                print("4_ ESCAPAR DE FORMA EPICA")
                accion = int(input("¿Qué harás?: "))
                if accion == 1:
                    cofre_actual.abrir()
                elif accion == 2:
                    if cofre_actual.estado == "abierto":
                        if cofre_actual.cantidad > 0:
                            print(f"¡Recogiste {cofre_actual.cantidad} monedas!")
                            self.prota.monedas += cofre_actual.cantidad
                            cofre_actual.cantidad = 0 
                        else:
                            print("El cofre ya está vacío.")
                    else:
                        print("¡El cofre está cerrado! Necesitas abrirlo primero.")
            
                elif accion == 3:
                    print("Buscas otro cofresuqui más adelante...")
                    break 
                elif accion == 4:
                    print("¡SALES DE FORMA EPICA CON EXPLOSIONES DE FONDO!")
                    print(f"{self.prota.nombre_p} sale con {self.prota.monedas} monedas.")
                    return
                else:
                    print("Opción no encontrada.")
juego = Juego()
juego.exploracion()
""""
""""
import random
class Auto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.distancia = 0
        self.nitro = 1
    def mostrar(self):
        print(f"corredor: {self.nombre} a recorrido: {self.distancia} metros")
    def acelerar(self):
        avance = random.randint(3, 7)
        self.distancia += avance
        print(f"{self.nombre} saco {avance} metros")

    def usar_nitro(self):
        if self.nitro == 1:
            self.nitro = 0
            avance_extra = random.randint(10, 15)
            self.distancia += avance_extra
            print(f"{self.nombre} usaste el nitro y sacaste {avance_extra} metros de distancia")
        else:
            print("te quedaste sin nitro pierdes un turno")

    def frenar(self):
        print(f"{self.nombre} decidiste ir lento para asegurar el motor")
class Rival(Auto):
    def turno_automatico(self):
        decision = random.randint(1, 10)
        if decision > 8 and self.nitro == 1:
            self.usar_nitro()
        else:
            self.acelerar()
class Carrera:
    def __init__(self):
        print("bienvenido a la copa piston")
        nombre_p = input("ingresa el nombre de tu piloto: ")
        self.jugador = Auto(nombre_p)
        self.rival = Rival("corredor malo")
        self.meta = 50
    def iniciar(self):
        print(f"comienza la carrera: {self.jugador.nombre} vs {self.rival.nombre}")
        while self.jugador.distancia < self.meta and self.rival.distancia < self.meta:
            self.jugador.mostrar()
            self.rival.mostrar()
            print("A: Acelerar  N: Nitro  F: Frenar")
            opcion = input(": ").capitalize()
            if opcion == "A":
                self.jugador.acelerar()
            elif opcion == "N":
                self.jugador.usar_nitro()
            elif opcion == "F":
                self.jugador.frenar()
            else:
                print("te equivocas de marcha y pierdes un turno")
            if self.jugador.distancia >= self.meta:
                print(f"felicidades {self.jugador.nombre} ganaste, esstoy orgulloso de vos voy a llorar de la emocion amigo...")
                break
            print("turno del enemigo malvado malvadote")
            self.rival.turno_automatico()
            if self.rival.distancia >= self.meta:
                print(f"el rival {self.rival.nombre} gano la carrera...")
                break
carrera=Carrera()
carrera.iniciar()
""""
""""
import random
class Hechicero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.energia = 30
        self.poder_especial = 1
    def mostrar(self):
        print(f"{self.nombre}: {self.vida} HP | {self.energia} MP")
    def atacar(self, objetivo):
        if self.energia >= 10:
            daño = random.randint(15, 25)
            objetivo.vida -= daño
            self.energia -= 10
            print(f"{self.nombre} lanza un hechizo y quita {daño} de vida")
        else:
            print(f"{self.nombre} no tiene suficiente energia")
    def descansar(self):
        recuperacion = random.randint(15, 25)
        self.energia += recuperacion
        print(f"{self.nombre} descansa y recupera {recuperacion} de energia")
    def bola_fuego(self, objetivo):
        if self.poder_especial == 1:
            self.poder_especial = 0
            danio_fuego = 45
            objetivo.vida -= danio_fuego
            print(f"{self.nombre} lanza una BOLA DE FUEGO y quita {danio_fuego} de vida")
        else:
            print("ya no te queda magia para la bola de fuego")
class Rival(Hechicero):
    def turno_automatico(self, jugador):
        if self.energia >= 10:
            decision = random.choice(["A","D","D","D","D"]) 
            if decision == "A":
                self.atacar(jugador)
            else:
                self.descansar()
        else:
            self.descansar()
class Combate:
    def __init__(self):
        nombre_h = input("ingresa el nombre de tu hechicero: ")
        self.jugador = Hechicero(nombre_h)
        self.rival = Rival("mago malito malote")
    def iniciar(self):
        print(f"comienza el duelo: {self.jugador.nombre} vs {self.rival.nombre}")
        while self.jugador.vida > 0 and self.rival.vida > 0:
            self.jugador.mostrar()
            self.rival.mostrar()
            print("A: Hechizo  D: Descansar  F: Bola de Fuego")
            opcion = input(": ").capitalize()

            if opcion == "A":
                self.jugador.atacar(self.rival)
            elif opcion == "D":
                self.jugador.descansar()
            elif opcion == "F":
                self.jugador.bola_fuego(self.rival)
            else:
                print("te trabaste con las palabras del hechizo y perdiste el turno")
            if self.rival.vida <= 0:
                print("victoria has ganado el duelo")
                break
            print("turno del malote")
            self.rival.turno_automatico(self.jugador)
            if self.jugador.vida <= 0:
                print("has caido en combate...")
                break
combate=Combate()
combate.iniciar()
""""
""""
import random
class Aventurero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = []
    def mostrar_mochila(self):
        if len(self.inventario) > 0:
            print(f"mochila de : {self.nombre} tiene : {self.inventario} ")
        else:
            print(f"tu mochila esta vacia")
    def guardar(self, objeto):
        self.inventario.append(objeto)
        print(f"has guardado {objeto} en la mochila")
    def usar(self, objeto):
        print(f"has usado {objeto}desaparece de tu vista")
    def descartar(self, objeto):
        print(f"has dejado {objeto} tirado en el camino")
class Mundo:
    def __init__(self):
        self.objetos_posibles = ["espada", "pocion", "escudo", "mapa", "antorcha", "moneda"]
    def generar_encuentro(self):
        return random.choice(self.objetos_posibles)
class Partida:
    def __init__(self):
        nombre_a = input("ingresa el nombre del aventurero: ")
        self.jugador = Aventurero(nombre_a)
        self.escenario = Mundo()
        self.jugando = True
    def jugar(self):
        print(f"comienza la aventura de {self.jugador.nombre}")
        while self.jugando:
            objeto = self.escenario.generar_encuentro()
            print(f"vas caminando y encuentras: {objeto}")
            print("G: Guardar  U: Usar  D: Descartar  I: Inventario  S: Salir")
            opcion = input(": ").capitalize()
            if opcion == "G":
                self.jugador.guardar(objeto)
            elif opcion == "U":
                self.jugador.usar(objeto)
            elif opcion == "D":
                self.jugador.descartar(objeto)
            elif opcion == "I":
                self.jugador.mostrar_mochila()
            elif opcion == "S":
                print("decidiste volver a casa")
                self.jugando = False
            else:
                print("te quedaste mirando el objeto sin saber que hacer")
partida=Partida()
partida.jugar()
""""
""""
import random
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje = 0
    def mostrar(self):
        print(f"{self.nombre}: {self.puntaje} puntos acumulados")
    def lanzar_dado(self):
        valor = random.randint(1, 1000)
        self.puntaje += valor
        print(f"{self.nombre} lanzo el dado y saco un {valor}")
class Rival(Jugador):
    def turno_automatico(self):
        self.lanzar_dado()
class Torneo:
    def __init__(self):
        nombre_u = input("ingresa tu nombre de jugador: ")
        self.usuario = Jugador(nombre_u)
        self.rivales = [Rival("hombre malo 1"), Rival("hombre muy malo 1")]
        self.rondas_totales = 3
    def iniciar(self):
        print("hola, te van a ganar bro ")
        ronda_actual = 1
        while ronda_actual <= self.rondas_totales:
            print(f"ronda {ronda_actual} de {self.rondas_totales}")
            print("L: Lanzar dado  S: Salir")
            opcion = input(": ").capitalize()
            if opcion == "L":
                self.usuario.lanzar_dado()
                print("turno de los rivales...")
                for r in self.rivales:
                    r.turno_automatico()
                print("posiciones actuales:")
                self.usuario.mostrar()
                for r in self.rivales:
                    r.mostrar()
                ronda_actual += 1
            elif opcion == "S":
                print("escapaste del torneo mas importante de tu vida.....")
                return
            else:
                print("te distrajiste pierdes el turno por distraido")
                ronda_actual += 1
        self.anunciar_ganador()
    def anunciar_ganador(self):
        print("resultado del torneo multiversal")
        puntos_usuario = self.usuario.puntaje
        if puntos_usuario > self.rivales[0].puntaje and puntos_usuario > self.rivales[1].puntaje:
            print(f"felicidades {self.usuario.nombre} eres el campeon")
        else:
            print("perdiste.")
torneo=Torneo()
torneo.iniciar()
""""
""""
import random
class Torre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.resistencia = 100
        self.escudo_activo = 0
    def mostrar(self):
        estado = "ACTIVO" if self.escudo_activo == 1 else "DESACTIVADO"
        print(f" {self.nombre}: {self.resistencia} HP | Escudo: {estado}")
    def recibir_danio(self, cantidad):
        if self.escudo_activo == 1:
            cantidad = cantidad // 2
            self.escudo_activo = 0
            print("el escudo absorbio parte del impacto")
        self.resistencia -= cantidad
        print(f"{self.nombre} recibio {cantidad} de daño")
    def reparar(self):
        curacion = random.randint(15, 25)
        self.resistencia += curacion
        print(f"obreros trabajando... {self.nombre} recupero {curacion} puntos.")
    def activar_escudo(self):
        self.escudo_activo = 1
        print(f"{self.nombre} ha levantado una barrera magica.")
class Horda:
    def generar_ataque(self):
        return random.randint(15, 30)
class Juego_defensa:
    def __init__(self):
        nombre_t = input("ingresa el nombre de tu torre: ")
        self.torre = Torre(nombre_t)
        self.enemigos = Horda()
        self.viva = True
    def iniciar(self):
        print(f"comienza la defensa de {self.torre.nombre}")
        while self.viva:
            self.torre.mostrar()
            print("A: Esperar ataque  R: Reparar  E: Escudo")
            opcion = input(": ").capitalize()
            if opcion == "R":
                self.torre.reparar()
            elif opcion == "E":
                self.torre.activar_escudo()
            elif opcion == "A":
                print("te preparas para el impacto.")
            else:
                print("el panico te paralizo y no hiciste nada.")
            print("--- los enemigos atacan! ---")
            danio = self.enemigos.generar_ataque()
            self.torre.recibir_danio(danio)
            if self.torre.resistencia <= 0:
                print(f"la torre {self.torre.nombre} se ha derrumbado.")
                print("GAME OVER")
                self.viva = False
partida=Juego_defensa()
partida.iniciar()
""""