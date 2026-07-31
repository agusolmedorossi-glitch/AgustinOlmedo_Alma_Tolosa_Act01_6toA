#Controles:                                                                  
#A  D ---- Mover a chicha                  
#E--- Hablar npc                               
#Q---Curarse                   
#Espacio   Z ---Avanzar dialogo, confirmar opción, boleadora   
#flechitas---Mover entre opciones                      
#F5----Guardar partida                                         
#F9 ----Cargar partida                                         
import pygame
import sys
import os
import json
import math

# Sección 1 configuración

ANCHO_PANTALLA= 1280
ALTO_PANTALLA= 720
FPS= 60 

#Suelo
SUELO= 620

#Cámara horizontal
ANCHO_MUNDO= 3840 #1672, problema con que no se muestra a Cruz (Agregar segunda imagen)
MARGEN_CAM_X= ANCHO_PANTALLA // 2

COLOR_LLAVE= (0, 0, 0)   #Chroma Key

#Spritesheets
ANCHO_CUADRO_PERSONAJE = 400
ALTO_CUADRO_PERSONAJE  = 396
ANCHO_CUADRO_CRUZ_ATADO = 400
ALTO_CUADRO_CRUZ_ATADO  = 396
ANCHO_CUADRO_CHICHA_FINAL = 400
ALTO_CUADRO_CHICHA_FINAL  = 393
FRAMES_SPRITESHEET_4 = 4

#Escala a la hora de jugar
ESCALA_GAMEPLAY  = 0.35 #180px

#Escala en las cinematicas
ESCALA_CINEMATICA = 1.0   #144 px

#Tamaño visible personaje en gameplay
ANCHO_VIS_PERSONAJE = int(ANCHO_CUADRO_PERSONAJE * ESCALA_GAMEPLAY)# 180 px
ALTO_VIS_PERSONAJE  = int(ALTO_CUADRO_PERSONAJE  * ESCALA_GAMEPLAY)# 179 px

#Tamaño de las imagenes de plantas en pantalla
ANCHO_VIS_PLANTA = 64
ALTO_VIS_PLANTA  = 64

#Velocidades de movimiento
VELOCIDAD_NORMAL = 4.0
VELOCIDAD_HERIDO = 2.0 

#Estado de salud
SALUD_MAXIMA       = 100
SALUD_INICIAL      = 60
UMBRAL_VIDA_HERIDO = 40    #Debajo del valor: va mas lento
HONOR_MAXIMO       = 100
UMBRAL_HONOR_ALTO  = 60

#Curación por planta
CURACION_POR_PLANTA = 25
ANCHO_CUADRO_CURACION = 500
ALTO_CUADRO_CURACION  = 492
FRAMES_CURACION       = 4
VEL_ANIM_CURACION     = 0.30 ##

#Combate, velocidades por px
VELOCIDAD_BOLEADORA= 9.0
VELOCIDAD_SOLDADO= 1.2
DANIO_BOLEADORA= 1
DISTANCIA_ATAQUE_SOLDADO= 70
DANIO_SOLDADO= 8 
COOLDOWN_LANZAMIENTO= 0.5
SALUD_CRUZ_MAXIMA= 80
SELUD_CRUZ_INICIAL=60
DISTANCIA_SEGUIR=120
VELOCIDAD_CRUZ=3.2
DAÑO_SOLDADO_A_CRUZ=6


#Guardar partida
ARCHIVO_GUARDADO = "partida.json"
TECLA_DIARIO=pygame.K_j

#Seccion 2 rutas

#Pantallas
RUTA_FONDO_MENU= r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Pantallas\fondo_menu.png"
RUTA_PANTALLA_CARGA= r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Pantallas\pantalla_carga.jpeg"
RUTA_SPRITESHEET_MENU=r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Pantallas\spritesheet_menu.png"

#Fondos
RUTA_FONDO_PAMPA= r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Paisajes\pampa.png"
RUTA_FONDO_PAMPA2=r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Paisajes\pampa2.png"
RUTA_FONDO_ATARDECER= r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Paisajes\final_cine.png"

#Chicha: spritesheets
RUTA_CHICHA_NORMAL= r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Npc_Personajes\chicha.png"
RUTA_CHICHA_RENGUEANDO= r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Npc_Personajes\chicha_rengueando.png"
RUTA_CHICHA_COMBATE= r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Npc_Personajes\chicha_ataque.png"
RUTA_CHICHA_SENTADO = r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Npc_Personajes\chicha_cineFinal.png" 
RUTA_CHICHA_CURACION= r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Npc_Personajes\chicha_curacion.png"

#Llancay
RUTA_LLANCAY= r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Npc_Personajes\Llancay.png"

#Cruz spritesheets
RUTA_CRUZ_ATADO= r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Npc_Personajes\cruz_atado.png"
RUTA_CRUZ_LIBRE= r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Npc_Personajes\cruz.png"
RUTA_CRUZ_CINE= r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Npc_Personajes\cruz_atado.png"

#Soldados
RUTA_SOLDADO_AVANCE= r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Npc_Personajes\soldado.png"
RUTA_SOLDADO_CAIDO = r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Npc_Personajes\NPC_caido.png"

#Boleadora
RUTA_BOLEADORA= r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Objetos\boleadora.png"

#Diario
RUTA_FONDO_DIARIO=r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Objetos\DiarioChicha (1).png"
RUTA_ANIM_DIARIO=r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Objetos\anima_diario.png"
ANCHO_CUADRO_ANIM_DIARIO=497.75
ALTO_CUADRO_ANIM_DIARIO=789

#Plantas medicinales
RUTA_MARCELA= r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Objetos\Marcela.png"
RUTA_PAJA_COLORADA= r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Objetos\Paja_Colorada.png"
RUTA_JARILLA = r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Objetos\Jarilla.png"
RUTA_TOLA_SERRANA= r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Objetos\Tola_Serrana.png"

#Música
RUTA_MUSICA_MENU= r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Musica\MUSICA_MENU.ogg"
RUTA_MUSICA_CINEMATICA= r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Musica\Introduccion.ogg"
RUTA_MUSICA_JUEGO= r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Musica\Explorar.ogg"
RUTA_MUSICA_DECISION= r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Musica\Decisión.ogg"
RUTA_MUSICA_FINAL_HONOR_ALTO= r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Musica\MUSICA_FINAL_DEMO.ogg" 
RUTA_MUSICA_FINAL_HONOR_BAJO=r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Musica\MUSICA_FINAL_HONOR_BAJO.ogg"
RUTA_SONIDO_VIENTO= r"" 
RUTA_MUSICA_COMBATE= r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Musica\MUSICA_COMBATE.ogg" 
#Cinemática
RUTA_CINE_PAMPA= r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Paisajes\final_cine.png"

from los_hijos_de_nadieCap2 import *

#Seccion 3 paleta de colores

COLOR_BLANCO        = (255, 255, 255)
COLOR_NEGRO         = (  0,   0,   0)
COLOR_TIERRA        = (101,  67,  33)
COLOR_TIERRA_BORDE  = (160, 110,  60)
COLOR_VERDE_VIDA    = ( 60, 180,  60)
COLOR_ROJO_DANIO     = (200,  40,  40)
COLOR_HONOR_ORO     = (218, 165,  32)
COLOR_CAJA_DLG      = ( 12,   8,   4, 215)
COLOR_OVERLAY_INTRO = (  0,   0,   0, 190)

#Sección 4 utilidades generales, fondos (sacar)

def _quitar_fondo_solido(superficie: pygame.Surface) -> pygame.Surface:
    superficie = superficie.convert_alpha()
    superficie.set_colorkey(COLOR_LLAVE)
    return superficie


def cargar_imagen(ruta: str, escala: tuple = None) -> pygame.Surface:

    if not ruta or not os.path.exists(ruta):
        if ruta:
            print(f"[Asset no encontrado] {ruta}")
        ancho, alto = escala if escala else (64, 64)
        ph = pygame.Surface((ancho, alto), pygame.SRCALPHA)
        ph.fill((40, 40, 40, 200))
        pygame.draw.rect(ph, (220, 0, 220), ph.get_rect(), 3)
        return ph
    try:
        imagen = pygame.image.load(ruta)
        imagen = _quitar_fondo_solido(imagen)
    except pygame.error as err:
        print(f"[Error al cargar imagen] {ruta} {err}")
        ancho, alto = escala if escala else (64, 64)
        ph = pygame.Surface((ancho, alto), pygame.SRCALPHA)
        ph.fill((40, 40, 40, 200))
        pygame.draw.rect(ph, (220, 0, 220), ph.get_rect(), 3)
        return ph
    if escala:
        imagen = pygame.transform.scale(imagen, escala)
    return imagen


def reproducir_musica(ruta: str, volumen: float = 0.5) -> None:
    if not ruta or not os.path.exists(ruta):
        return
    try:
        pygame.mixer.music.load(ruta)
        pygame.mixer.music.set_volume(volumen)
        pygame.mixer.music.play(-1)
    except Exception:
        pass


def reproducir_sonido(ruta: str, volumen: float = 0.6):
    if not ruta or not os.path.exists(ruta):
        return None
    try:
        sonido = pygame.mixer.Sound(ruta)
        sonido.set_volume(volumen)
        return sonido
    except Exception:
        return None


def dibujar_texto_envuelto(pantalla, texto, fuente, color, x, y, ancho_max) -> int:

    palabras     = texto.split(" ")
    linea        = ""
    desplaz_y    = 0
    interlineado = fuente.get_linesize() + 2
    for palabra in palabras:
        prueba = linea + palabra + " "
        if fuente.size(prueba)[0] > ancho_max and linea:
            pantalla.blit(fuente.render(linea.rstrip(), True, color), (x, y + desplaz_y))
            desplaz_y += interlineado
            linea      = palabra + " "
        else:
            linea = prueba
    if linea.strip():
        pantalla.blit(fuente.render(linea.rstrip(), True, color), (x, y + desplaz_y))
        desplaz_y += interlineado
    return desplaz_y


def dibujar_caja(pantalla, rect, color_fondo, color_borde, grosor=2, radio=6): #Dialogo

    sup = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    pygame.draw.rect(sup, color_fondo, sup.get_rect(), border_radius=radio)
    pantalla.blit(sup, rect.topleft)
    pygame.draw.rect(pantalla, color_borde, rect, grosor, border_radius=radio)

#Sección 5 hoja de sprite sheets

class HojaSprites:

    def __init__(self, ruta: str, ancho_cuadro: int, alto_cuadro: int, escala: float = ESCALA_GAMEPLAY):

        self.ancho_cuadro = ancho_cuadro
        self.alto_cuadro  = alto_cuadro
        self.escala       = escala
        self._cache_frames = {}   

        if not ruta or not os.path.exists(ruta):
            if ruta:
                print(f"[HojaSprites] No encontrado: {ruta}")
            self._hoja = self._placeholder(ancho_cuadro, alto_cuadro)
        else:
            try:
                hoja_cruda = pygame.image.load(ruta)
                self._hoja = _quitar_fondo_solido(hoja_cruda)
            except pygame.error as err:
                print(f"[HojaSprites] Error: {ruta} a {err}")
                self._hoja = self._placeholder(ancho_cuadro, alto_cuadro)

        self.total_cuadros = max(1, self._hoja.get_width() // ancho_cuadro)

    @staticmethod #
    def _placeholder(ancho, alto):
        sup = pygame.Surface((ancho, alto), pygame.SRCALPHA)
        sup.fill((40, 40, 40, 220))
        pygame.draw.rect(sup, (220, 0, 220), sup.get_rect(), 2)
        return sup

    def obtener_frame(self, indice: int) -> pygame.Surface:
        indice = indice % self.total_cuadros
        if indice in self._cache_frames:
            return self._cache_frames[indice]

        x_recorte = indice * self.ancho_cuadro
        x_recorte = min(x_recorte, max(0, self._hoja.get_width() - self.ancho_cuadro))
        rect_recorte = pygame.Rect(x_recorte, 0, self.ancho_cuadro, self.alto_cuadro)

        try:
            cuadro = self._hoja.subsurface(rect_recorte).copy()
        except ValueError:
            cuadro = self._placeholder(self.ancho_cuadro, self.alto_cuadro)

        ancho_final = int(self.ancho_cuadro * self.escala)
        alto_final  = int(self.alto_cuadro  * self.escala)
        cuadro_escalado = pygame.transform.scale(cuadro, (ancho_final, alto_final))

        self._cache_frames[indice] = cuadro_escalado
        return cuadro_escalado


#Sección 6 guardado y cargar partida

def guardar_partida(partida: dict, nombre_escena: str, posicion_x: float) -> None:

    datos = {
        "capitulo":          nombre_escena,
        "jugador_x":         posicion_x,
        "honor":             partida["honor"],
        "salud":             partida["salud"],
        "inventario":        partida["inventario"],
        "plantas_conocidas": partida["plantas_conocidas"],
        "cruz_aliado":       partida["cruz_aliado"],
        "decisiones":        partida["decisiones"],
    }
    try:
        with open(ARCHIVO_GUARDADO, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)
        print(f"[Guardado] {ARCHIVO_GUARDADO}")
    except Exception as err:
        print(f"[Error al guardar] {err}")


def cargar_partida():
    if not os.path.exists(ARCHIVO_GUARDADO):
        return None
    try:
        with open(ARCHIVO_GUARDADO, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as err:
        print(f"[Error al cargar] {err}")
        return None


# Seccion 7 gestor y estado partida

class GestorEscenas:

    def __init__(self, pantalla: pygame.Surface):
        self.pantalla      = pantalla
        self._mapa         = {}
        self.escena_actual = None
        self.nombre_escena = "menu"
        self.partida = {
            "honor":             0,
            "salud":             SALUD_INICIAL,
            "inventario":        [],
            "plantas_conocidas": [],
            "cruz_aliado":       False,
            "decisiones":        {},
        }

    def registrar(self, nombre: str, clase) -> None:
        self._mapa[nombre] = clase

    def cambiar(self, nombre: str, **argumentos) -> None:
        if nombre not in self._mapa:
            raise KeyError(f"Escena '{nombre}' no registrada.")
        self.nombre_escena = nombre
        self.escena_actual = self._mapa[nombre](self, **argumentos)

    def sumar_honor(self, delta: int) -> None:
        self.partida["honor"] = max(0, min(HONOR_MAXIMO,
                                           self.partida["honor"] + delta))

    def aplicar_guardado(self, datos: dict) -> None:
        for clave in ("honor", "salud", "inventario",
                      "plantas_conocidas", "cruz_aliado", "decisiones"):
            if clave in datos:
                self.partida[clave] = datos[clave]


class EscenaBase: #Base de todas las escenas

    def __init__(self, gestor: GestorEscenas):
        self.gestor = gestor

    def manejar_evento(self, evento: pygame.event.Event) -> None:
        pass

    def actualizar(self, dt: float) -> None:
        pass

    def dibujar(self, pantalla: pygame.Surface) -> None:
        pass

# Seccion 8 sistema dialogo

class LineaDialogo:
    def __init__(self, hablante: str, texto: str):
        self.hablante = hablante
        self.texto    = texto


class Opcion:
    def __init__(self, texto: str, efecto_honor: int = 0, resultado: str = ""):
        self.texto        = texto
        self.efecto_honor = efecto_honor
        self.resultado    = resultado


class SistemaDialogo:

    RELLENO    = 22
    ALTO_CAJA  = 210
    MARGEN_INF = 18
    VEL_CHARS  = 2

    def __init__(self):
        self.activo            = False
        self._lineas           = []
        self._opciones         = []
        self._indice           = 0
        self._chars            = 0
        self._tick             = 0
        self._modo_opciones    = False
        self._seleccion        = 0
        self._callback_cerrar  = None

        self._fn  = pygame.font.SysFont("Arial", 18, bold=True)
        self._ft  = pygame.font.SysFont("Arial", 17)
        self._fo  = pygame.font.SysFont("Arial", 16)
        self._fp  = pygame.font.SysFont("Arial", 13)

    def iniciar(self, lineas: list, opciones: list = None,
                callback_cerrar=None) -> None:
        self._lineas           = lineas
        self._opciones         = opciones or []
        self._indice           = 0
        self._chars            = 0
        self._tick             = 0
        self._modo_opciones    = False
        self._seleccion        = 0
        self._callback_cerrar  = callback_cerrar
        self.activo            = True

    def cerrar(self) -> None:
        self.activo = False

    def actualizar(self, dt: float) -> None:
        if not self.activo or self._modo_opciones:
            return
        self._tick += 1
        if self._tick % 2 == 0:
            self._chars = min(self._chars + self.VEL_CHARS,
                              len(self._lineas[self._indice].texto))

    def procesar_evento(self, evento: pygame.event.Event):

        if not self.activo:
            return None

        # Soporte mouse
        if self._modo_opciones and evento.type == pygame.MOUSEBUTTONDOWN:
            return self._click_opcion(evento.pos)

        if evento.type != pygame.KEYDOWN:
            return None
        if self._modo_opciones:
            return self._navegar(evento.key)
        if evento.key in (pygame.K_SPACE, pygame.K_RETURN, pygame.K_z):
            self._avanzar()
        return None

    def _avanzar(self) -> None:
        linea = self._lineas[self._indice]
        if self._chars < len(linea.texto):
            self._chars = len(linea.texto)
            return
        self._indice += 1
        if self._indice >= len(self._lineas):
            if self._opciones:
                self._modo_opciones = True
                self._seleccion     = 0
            else:
                self.activo = False
                cb = self._callback_cerrar
                self._callback_cerrar = None
                if cb:
                    cb()
        else:
            self._chars = 0
            self._tick  = 0

    def _navegar(self, tecla):
        if tecla == pygame.K_UP:
            self._seleccion = max(0, self._seleccion - 1)
        elif tecla == pygame.K_DOWN:
            self._seleccion = min(len(self._opciones) - 1, self._seleccion + 1)
        elif tecla in (pygame.K_SPACE, pygame.K_RETURN, pygame.K_z):
            elegida     = self._opciones[self._seleccion]
            self.activo = False
            return elegida
        return None

    def _click_opcion(self, pos_mouse):
        y0   = ALTO_PANTALLA - self.ALTO_CAJA - self.MARGEN_INF
        caja = pygame.Rect(self.RELLENO, y0,
                           ANCHO_PANTALLA - self.RELLENO * 2, self.ALTO_CAJA)
        p = self.RELLENO
        for i, _ in enumerate(self._opciones):
            y_op = caja.y + p + 38 + i * 36
            rect_opcion = pygame.Rect(caja.x + p - 4, y_op - 4,
                                      caja.width - p * 2 + 8, 32)
            if rect_opcion.collidepoint(pos_mouse):
                elegida     = self._opciones[i]
                self.activo = False
                return elegida
        return None

    def dibujar(self, pantalla: pygame.Surface) -> None:
        if not self.activo:
            return
        y0   = ALTO_PANTALLA - self.ALTO_CAJA - self.MARGEN_INF
        caja = pygame.Rect(self.RELLENO, y0,
                           ANCHO_PANTALLA - self.RELLENO * 2, self.ALTO_CAJA)
        dibujar_caja(pantalla, caja, COLOR_CAJA_DLG, COLOR_TIERRA_BORDE, 2, 8)
        if self._modo_opciones:
            self._dibujar_opciones(pantalla, caja)
        else:
            self._dibujar_linea(pantalla, caja)

    def _dibujar_linea(self, pantalla, caja):
        p     = self.RELLENO
        linea = self._lineas[self._indice]
        nombre_s = self._fn.render(linea.hablante, True, COLOR_HONOR_ORO)
        pantalla.blit(nombre_s, (caja.x + p, caja.y + p))
        sep_y = caja.y + p + nombre_s.get_height() + 4
        pygame.draw.line(pantalla, COLOR_TIERRA_BORDE,
                         (caja.x + p, sep_y), (caja.right - p, sep_y), 1)
        texto_vis = linea.texto[:self._chars]
        dibujar_texto_envuelto(pantalla, texto_vis, self._ft, COLOR_BLANCO,
                               caja.x + p, sep_y + 8, caja.width - p * 2)
        if self._chars >= len(linea.texto):
            if (pygame.time.get_ticks() // 500) % 2 == 0:
                pista = self._fp.render(" Espacio", True, (175, 175, 175))
                pantalla.blit(pista, (caja.right - pista.get_width() - p,
                                      caja.bottom - pista.get_height() - p))

    def _dibujar_opciones(self, pantalla, caja):
        p   = self.RELLENO
        tit = self._fn.render("¿Qué haces?", True, COLOR_HONOR_ORO)
        pantalla.blit(tit, (caja.x + p, caja.y + p))
        for i, op in enumerate(self._opciones):
            y_op   = caja.y + p + 38 + i * 36
            es_sel = (i == self._seleccion)
            if es_sel:
                r = pygame.Rect(caja.x + p - 4, y_op - 4,
                                caja.width - p * 2 + 8, 32)
                dibujar_caja(pantalla, r, (*COLOR_TIERRA, 180),
                             COLOR_HONOR_ORO, 1, 4)
            color = COLOR_HONOR_ORO if es_sel else COLOR_BLANCO
            pref  = " " if es_sel else "  "
            pantalla.blit(self._fo.render(pref + op.texto, True, color),
                          (caja.x + p + 6, y_op))
        op_a = self._opciones[self._seleccion]
        if op_a.efecto_honor != 0:
            signo = "+" if op_a.efecto_honor > 0 else ""
            col   = COLOR_VERDE_VIDA if op_a.efecto_honor > 0 else COLOR_ROJO_DANIO
            h_txt = self._fp.render(f"Honor: {signo}{op_a.efecto_honor}", True, col)
            pantalla.blit(h_txt, (caja.right - h_txt.get_width() - p,
                                  caja.bottom - h_txt.get_height() - p))


# Seccion 9 HUD

class HUD: #Barras de vida y honor, inventario de plantas, mensajes temporales

    ANCHO_BARRA = 140
    ALTO_BARRA  = 12
    RELLENO     = 10

    def __init__(self):
        self._fs = pygame.font.SysFont("Arial", 14)
        self._fi = pygame.font.SysFont("Arial", 13)
        self._fm = pygame.font.SysFont("Arial", 16, bold=True)
        self._mensaje        = ""
        self._tiempo_mensaje = 0.0
        self._duracion_msg   = 3.5

    def mostrar_mensaje(self, texto: str) -> None:
        self._mensaje        = texto
        self._tiempo_mensaje = self._duracion_msg

    def actualizar(self, dt: float) -> None:
        if self._tiempo_mensaje > 0:
            self._tiempo_mensaje -= dt

    def dibujar(self, pantalla, salud, honor, inventario) -> None:
        p = self.RELLENO
        dibujar_caja(pantalla, pygame.Rect(p - 4, p - 4, 265, 56),
                     (0, 0, 0, 165), COLOR_TIERRA_BORDE, 1, 6)
        self._barra(pantalla, p + 4, p + 4,  salud, SALUD_MAXIMA, COLOR_VERDE_VIDA, "Vida")
        self._barra(pantalla, p + 4, p + 22, honor, HONOR_MAXIMO, COLOR_HONOR_ORO,  "Honor")
        self._dibujar_inventario(pantalla, inventario)
        if self._tiempo_mensaje > 0:
            prog  = self._tiempo_mensaje / self._duracion_msg
            alpha = int(min(255, 255 * min(prog * 3, 1)))
            sup   = self._fm.render(self._mensaje, True, COLOR_HONOR_ORO)
            sup.set_alpha(alpha)
            pantalla.blit(sup, ((ANCHO_PANTALLA - sup.get_width()) // 2, 48))

    def _barra(self, pantalla, x, y, valor, maximo, color, etiqueta):
        pantalla.blit(self._fs.render(f"{etiqueta}:", True, COLOR_BLANCO), (x, y))
        bx = x + 52
        pygame.draw.rect(pantalla, (50, 50, 50), (bx, y + 2, self.ANCHO_BARRA, self.ALTO_BARRA))
        relleno = max(0, int(self.ANCHO_BARRA * valor / maximo))
        if relleno:
            pygame.draw.rect(pantalla, color, (bx, y + 2, relleno, self.ALTO_BARRA))
        pygame.draw.rect(pantalla, (180, 180, 180), (bx, y + 2, self.ANCHO_BARRA, self.ALTO_BARRA), 1)
        pantalla.blit(self._fs.render(str(valor), True, COLOR_BLANCO),
                      (bx + self.ANCHO_BARRA + 4, y))

    def _dibujar_inventario(self, pantalla, inventario):
        plantas = inventario.listar()
        if not plantas:
            return
        xb = ANCHO_PANTALLA - 215
        yb = self.RELLENO
        dibujar_caja(pantalla,
                     pygame.Rect(xb - 6, yb - 4, 209, 20 + len(plantas[:5]) * 16),
                     (0, 0, 0, 160), COLOR_TIERRA_BORDE, 1, 5)
        pantalla.blit(self._fi.render("Plantas:", True, COLOR_HONOR_ORO), (xb, yb))
        for i, pl in enumerate(plantas[:5]):
            pantalla.blit(
                self._fi.render(f"{pl['nombre']}  +{pl.get('curacion', 0)}",
                                True, COLOR_BLANCO),
                (xb, yb + 17 + i * 16))


#Seccion 10 inventario plantas

class Inventario:

    def __init__(self, datos_iniciales: list = None):
        self._plantas = list(datos_iniciales or [])

    def agregar(self, datos: dict) -> None:
        self._plantas.append(dict(datos))

    def listar(self) -> list:
        return list(self._plantas)

    def a_lista(self) -> list:
        return list(self._plantas)

    def puede_curar(self, salud_actual: int) -> bool:
        return bool(self._plantas) and salud_actual < SALUD_MAXIMA

    def obtener(self, indice: int):
        if 0 <= indice < len(self._plantas):
            return self._plantas[indice]
        return None

    def usar_indice(self, indice: int, salud_actual: int):
        if not self.puede_curar(salud_actual):
            return None
        if 0 <= indice < len(self._plantas):
            return self._plantas.pop(indice)
        return None

    def usar_indices(self, indices: list, salud_actual: int) -> list:
        if not self.puede_curar(salud_actual):
            return []
        usadas = []
        for indice in sorted(indices, reverse=True):
            if 0 <= indice < len(self._plantas):
                usadas.append(self._plantas.pop(indice))
        usadas.reverse()
        return usadas

    def usar_mejor_planta(self, salud_actual: int) -> int:
        if not self.puede_curar(salud_actual):
            return 0
        mejor = max(self._plantas, key=lambda p: p.get("curacion", 0))
        self._plantas.remove(mejor)
        return mejor.get("curacion", 0)

    def __len__(self):
        return len(self._plantas)



class MenuCuracion:

    RECETAS = {
        frozenset(("jarilla", "marcela")): ("Cataplasma Curativo", 50),
        frozenset(("jarilla", "tola serrana")): ("Ungüento Serrano", 60),
        frozenset(("marcela", "paja colorada")): ("Infusión Reconfortante", 40),
    }

    def __init__(self):
        self.activo = False
        self._fuente_titulo = pygame.font.SysFont("Georgia", 24, bold=True)
        self._fuente = pygame.font.SysFont("Arial", 16)
        self._fuente_chica = pygame.font.SysFont("Arial", 13)
        self._rect_panel = pygame.Rect(130, 70, 1020, 560)
        self._rect_mezcla = pygame.Rect(430, 205, 300, 230)
        self._rect_lista = pygame.Rect(815, 115, 285, 430)
        self._items_rect = []
        self._seleccionadas = []
        self._arrastrando = None
        self._pos_mouse = (0, 0)
        
        self._imagenes_plantas = {

        "Jarilla":
            pygame.image.load(
                RUTA_JARILLA
            ).convert_alpha(),

        "Marcela":
            pygame.image.load(
                RUTA_MARCELA
            ).convert_alpha(),

        "Paja Colorada":
            pygame.image.load(
                RUTA_PAJA_COLORADA
            ).convert_alpha(),

        "Tola Serrana":
            pygame.image.load(
                RUTA_TOLA_SERRANA
            ).convert_alpha()
    }

    def abrir(self) -> None:
        self.activo = True
        self._seleccionadas = []
        self._arrastrando = None

    def cerrar(self) -> None:
        self.activo = False
        self._seleccionadas = []
        self._arrastrando = None

    def manejar_evento(self, evento, inventario, jugador, hud) -> bool:
        if not self.activo:
            return False

        if evento.type == pygame.KEYDOWN and evento.key in (pygame.K_q, pygame.K_ESCAPE):
            self.cerrar()
            return True

        if evento.type == pygame.MOUSEMOTION:
            self._pos_mouse = evento.pos
            return True

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            self._pos_mouse = evento.pos
            for indice, rect in self._items_rect:
                if rect.collidepoint(evento.pos):
                    self._arrastrando = indice
                    return True
            if not self._rect_panel.collidepoint(evento.pos):
                self.cerrar()
            return True

        if evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
            self._pos_mouse = evento.pos
            if self._arrastrando is None:
                return True
            indice = self._arrastrando
            self._arrastrando = None
            if self._rect_mezcla.collidepoint(evento.pos):
                self._agregar_a_mezcla(indice, inventario, jugador, hud)
            else:
                self._usar_planta(indice, inventario, jugador, hud)
            return True

        return True

    def _normalizar(self, nombre: str) -> str:
        return nombre.strip().lower()

    def _usar_planta(self, indice, inventario, jugador, hud) -> None:
        if jugador.salud >= SALUD_MAXIMA:
            hud.mostrar_mensaje("Vida al máximo.")
            return
        planta = inventario.usar_indice(indice, jugador.salud)
        if not planta:
            return
        curacion = planta.get("curacion", 0)
        jugador.curar(curacion)
        hud.mostrar_mensaje(
            f"{planta['nombre']}  +{curacion} vida  ({jugador.salud}/{SALUD_MAXIMA})")
        self.cerrar()

    def _agregar_a_mezcla(self, indice, inventario, jugador, hud) -> None:
        if indice in self._seleccionadas:
            return
        planta = inventario.obtener(indice)
        if not planta:
            return
        self._seleccionadas.append(indice)
        if len(self._seleccionadas) >= 2:
            self._mezclar(inventario, jugador, hud)

    def _mezclar(self, inventario, jugador, hud) -> None:
        plantas = [inventario.obtener(i) for i in self._seleccionadas[:2]]
        if any(planta is None for planta in plantas):
            self._seleccionadas = []
            return
        clave = frozenset(self._normalizar(planta["nombre"]) for planta in plantas)
        receta = self.RECETAS.get(clave)
        if not receta:
            hud.mostrar_mensaje("Esa mezcla no tiene efecto curativo.")
            self._seleccionadas = []
            return
        if jugador.salud >= SALUD_MAXIMA:
            hud.mostrar_mensaje("Vida al máximo.")
            self._seleccionadas = []
            return

        nombre, curacion = receta
        usadas = inventario.usar_indices(self._seleccionadas[:2], jugador.salud)
        if len(usadas) == 2:
            jugador.curar(curacion)
            hud.mostrar_mensaje(
                f"{nombre}  +{curacion} vida  ({jugador.salud}/{SALUD_MAXIMA})")
            self.cerrar()

    def dibujar(self, pantalla, inventario, jugador) -> None:
        if not self.activo:
            return

        sombra = pygame.Surface((ANCHO_PANTALLA, ALTO_PANTALLA), pygame.SRCALPHA)
        sombra.fill((0, 0, 0, 175))
        pantalla.blit(sombra, (0, 0))

        dibujar_caja(pantalla, self._rect_panel, (12, 10, 8, 235), COLOR_TIERRA_BORDE, 2, 8)
        pantalla.blit(self._fuente_titulo.render("Botiquín", True, COLOR_HONOR_ORO),
                      (self._rect_panel.x + 28, self._rect_panel.y + 24))
        pantalla.blit(self._fuente.render(f"Vida: {jugador.salud}/{SALUD_MAXIMA}", True, COLOR_BLANCO),
                      (self._rect_panel.x + 30, self._rect_panel.y + 64))

        dibujar_caja(pantalla, self._rect_mezcla, (25, 20, 15, 210), COLOR_HONOR_ORO, 2, 8)
        titulo = self._fuente.render("Mezcla", True, COLOR_HONOR_ORO)
        pantalla.blit(titulo, (self._rect_mezcla.centerx - titulo.get_width() // 2,
                               self._rect_mezcla.y + 18))
        pygame.draw.circle(pantalla, (80, 60, 42), self._rect_mezcla.center, 58)
        pygame.draw.circle(pantalla, COLOR_TIERRA_BORDE, self._rect_mezcla.center, 58, 3)

        y_sel = self._rect_mezcla.y + 165
        for indice in self._seleccionadas:
            planta = inventario.obtener(indice)
            if planta:
                txt = self._fuente_chica.render(planta["nombre"], True, COLOR_BLANCO)
                pantalla.blit(txt, (self._rect_mezcla.x + 24, y_sel))
                y_sel += 20

        dibujar_caja(pantalla, self._rect_lista, (18, 15, 12, 225), COLOR_TIERRA_BORDE, 2, 8)
        pantalla.blit(self._fuente.render("Inventario", True, COLOR_HONOR_ORO),
                      (self._rect_lista.x + 18, self._rect_lista.y + 16))
        self._dibujar_lista(pantalla, inventario)

        ayuda = self._fuente_chica.render(
            "Clic: curar con una planta   |   Arrastrá dos al centro: combinar   |   Q/Esc: cerrar",
            True, (190, 180, 165))
        pantalla.blit(ayuda, (self._rect_panel.x + 28, self._rect_panel.bottom - 34))

        if self._arrastrando is not None:
            planta = inventario.obtener(self._arrastrando)
            if planta:
                self._dibujar_tarjeta(pantalla, planta,
                                      pygame.Rect(self._pos_mouse[0] - 90,
                                                  self._pos_mouse[1] - 24, 180, 48),
                                      True)

    def _dibujar_lista(self, pantalla, inventario) -> None:
        self._items_rect = []
        plantas = inventario.listar()
        y = self._rect_lista.y + 54
        for indice, planta in enumerate(plantas):
            rect = pygame.Rect(self._rect_lista.x + 16, y, self._rect_lista.width - 32, 44)
            self._items_rect.append((indice, rect))
            ocultar = indice == self._arrastrando
            if not ocultar:
                self._dibujar_tarjeta(pantalla, planta, rect, indice in self._seleccionadas)
            y += 52

    def _dibujar_tarjeta(self, pantalla, planta, rect, seleccionada=False) -> None:

        fondo = (42, 34, 24, 230) if not seleccionada else (72, 55, 32, 240)
        borde = COLOR_HONOR_ORO if seleccionada else COLOR_TIERRA_BORDE

        dibujar_caja(
            pantalla,
            rect,
            fondo,
            borde,
            1,
            5
        )

        # Obtener imagen de la planta
        imagen = self._imagenes_plantas.get(
            planta["nombre"]
        )

        if imagen:

            miniatura = pygame.transform.scale(
                imagen,
                (32, 32)
            )

            pantalla.blit(
                miniatura,
                (
                    rect.x + 6,
                    rect.y + 6
                )
            )

        nombre = self._fuente.render(
            planta["nombre"],
            True,
            COLOR_BLANCO
        )

        cura = self._fuente_chica.render(
            f"+{planta.get('curacion', 0)}",
            True,
            COLOR_VERDE_VIDA
        )
        pantalla.blit(
            nombre,
            (
                rect.x + 48,
                rect.y + 7
            )
        )
        pantalla.blit(
            cura,
            (
                rect.right - cura.get_width() - 12,
                rect.y + 13
            )
        )


#Seccion 11 camara horizontal

class Camara:
    def __init__(self):
        self.desplaz_x=0

    def actualizar(self,pos_jugador_x:float)->None:
        objetivo=pos_jugador_x-MARGEN_CAM_X
        self.desplaz_x=max(0,min(objetivo,ANCHO_MUNDO-ANCHO_PANTALLA))

    def aplicar_x(self,x_mundo:float)->int:
        return int(x_mundo-self.desplaz_x)


#Seccion 12 Chicha

class Jugador:
    ANCHO_CAJA = int(ANCHO_VIS_PERSONAJE * 0.55)
    ALTO_CAJA  = ALTO_VIS_PERSONAJE

    def __init__(self, x_mundo: float, salud: int = SALUD_INICIAL, honor: int = 0):
        self.x       = float(x_mundo)
        self.salud   = salud
        self.honor   = honor
        self.vivo    = True

        self.velocidad_x = 0.0
        self.mirando_der = True
        self.en_combate  = False   # True durante combate

        self._hoja_normal   = HojaSprites(RUTA_CHICHA_NORMAL,ancho_cuadro=400, alto_cuadro=393)
        self._hoja_rengueo  = HojaSprites(RUTA_CHICHA_RENGUEANDO, ancho_cuadro= 400, alto_cuadro=396)
        self._hoja_combate  = HojaSprites(RUTA_CHICHA_COMBATE, ancho_cuadro=400, alto_cuadro=393)
        self._hoja_curacion = HojaSprites(RUTA_CHICHA_CURACION,
                                          ANCHO_CUADRO_CURACION,
                                          ALTO_CUADRO_CURACION,
                                          escala=0.29) ##

        self._cuadro        = 0
        self._timer_anim    = 0.0
        self._vel_anim      = 0.13
        self._en_movimiento = False
        self._curando       = False
        self._cuadro_curacion = 0
        self._timer_curacion  = 0.0
        self._atacando        = False
        self._cuadro_ataque   = 0
        self._timer_ataque    = 0.0

        self.rect = pygame.Rect(
            int(self.x) + (ANCHO_VIS_PERSONAJE - self.ANCHO_CAJA) // 2,
            SUELO - self.ALTO_CAJA,
            self.ANCHO_CAJA, self.ALTO_CAJA
        )

    @property
    def esta_herido(self) -> bool:
        return self.salud < UMBRAL_VIDA_HERIDO

    @property
    def velocidad_actual(self) -> float:
        return VELOCIDAD_HERIDO if self.esta_herido else VELOCIDAD_NORMAL

    @property
    def hoja_activa(self) -> HojaSprites:
        if self.esta_herido:
            return self._hoja_rengueo
        return self._hoja_normal

    def procesar_entrada(self, teclas) -> None:
        if self._curando or self._atacando:
            self.velocidad_x = 0.0
            self._en_movimiento = False
            return

        self.velocidad_x = 0.0
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            self.velocidad_x = -self.velocidad_actual
            self.mirando_der = False
        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            self.velocidad_x =  self.velocidad_actual
            self.mirando_der = True
        self._en_movimiento = (self.velocidad_x != 0)

    def actualizar(self, dt: float) -> None:
        self.x = max(0.0, min(ANCHO_MUNDO - ANCHO_VIS_PERSONAJE,
                              self.x + self.velocidad_x))
        self.rect.x      = int(self.x) + (ANCHO_VIS_PERSONAJE - self.ANCHO_CAJA) // 2
        self.rect.bottom = SUELO

        if self._curando:
            self._timer_curacion += dt
            if self._timer_curacion >= VEL_ANIM_CURACION:
                self._timer_curacion = 0.0
                self._cuadro_curacion += 1
                if self._cuadro_curacion >= FRAMES_CURACION:
                    self._curando = False
                    self._cuadro_curacion = 0
            return

        if self._atacando:
            self._timer_ataque += dt
            if self._timer_ataque >= self._vel_anim:
                self._timer_ataque = 0.0
                self._cuadro_ataque += 1
                if self._cuadro_ataque >= FRAMES_SPRITESHEET_4:
                    self._atacando = False
                    self._cuadro_ataque = 0
            return

        self._timer_anim += dt
        if self._timer_anim >= self._vel_anim:
            self._timer_anim = 0.0
            if self._en_movimiento:
                self._cuadro = (self._cuadro % 3) + 1
            else:
                self._cuadro = 0

    def curar(self, cantidad: int) -> None:

        self.salud = min(SALUD_MAXIMA, self.salud + cantidad)
        self.iniciar_animacion_curacion()

    def iniciar_animacion_curacion(self) -> None:
        self._curando = True
        self._cuadro_curacion = 0
        self._timer_curacion = 0.0
        self.velocidad_x = 0.0
        self._en_movimiento = False

    def iniciar_animacion_ataque(self) -> None:
        self._atacando = True
        self._cuadro_ataque = 0
        self._timer_ataque = 0.0
        self.velocidad_x = 0.0
        self._en_movimiento = False

    def recibir_danio(self, cantidad: int) -> None:
        self.salud = max(0, self.salud - cantidad)
        if self.salud == 0:
            self.vivo = False

    def dibujar(self, pantalla: pygame.Surface, camara: Camara) -> None:
        if self._curando:
            frame = self._hoja_curacion.obtener_frame(self._cuadro_curacion)
        elif self._atacando:
            frame = self._hoja_combate.obtener_frame(self._cuadro_ataque)
        else:
            frame = self.hoja_activa.obtener_frame(self._cuadro)
        if not self.mirando_der:
            frame = pygame.transform.flip(frame, True, False)
        x_pan = camara.aplicar_x(self.x)
        x_pan += (ANCHO_VIS_PERSONAJE - frame.get_width()) // 2
        y_pan = SUELO - frame.get_height()
        pantalla.blit(frame, (x_pan, y_pan))

    def cerca_de(self, rect_mundo: pygame.Rect, dist: int = 90) -> bool:
        return self.rect.colliderect(rect_mundo.inflate(dist, dist))

#Seccion 13 npc Llancay

class Llancay:

    ESCALA_LLANCAY    = 0.15
    ANCHO_VIS_LLANCAY = int(1024 * ESCALA_LLANCAY)
    ALTO_VIS_LLANCAY  = int(1024 * ESCALA_LLANCAY)
    ANCHO_CAJA        = int(ANCHO_VIS_LLANCAY * 0.5)
    ALTO_CAJA         = ALTO_VIS_LLANCAY

    def __init__(self, x_mundo: float):
        self.x_mundo = float(x_mundo)
        self.nombre  = "Llancay"
        self.activo  = True
        self._imagen = cargar_imagen(RUTA_LLANCAY,
                                     (self.ANCHO_VIS_LLANCAY, self.ALTO_VIS_LLANCAY))
        self._tick    = 0
        self._desplaz = 0
        self._fuente  = pygame.font.SysFont("Arial", 13)

        self.rect = pygame.Rect(
            int(self.x_mundo) + (self.ANCHO_VIS_LLANCAY - self.ANCHO_CAJA) // 2,
            SUELO - self.ALTO_CAJA,
            self.ANCHO_CAJA, self.ALTO_CAJA
        )

    def actualizar(self, dt: float) -> None:
        self._tick    += 1
        self._desplaz  = int(math.sin(self._tick * 0.04) * 1.5)

    def cerca_de(self, rect_jugador: pygame.Rect, dist: int = 100) -> bool:
        return self.rect.colliderect(rect_jugador.inflate(dist, dist))

    def dibujar(self, pantalla: pygame.Surface, camara: Camara) -> None:
        if not self.activo:
            return
        x_pan = camara.aplicar_x(self.x_mundo)
        y_pan = SUELO - self.ALTO_VIS_LLANCAY + self._desplaz
        pantalla.blit(self._imagen, (x_pan, y_pan))
        etq   = self._fuente.render(f"â–¼ {self.nombre}", True, COLOR_BLANCO)
        ex    = x_pan + self.ANCHO_VIS_LLANCAY // 2 - etq.get_width() // 2
        ey    = y_pan - 18
        fondo = pygame.Surface((etq.get_width() + 8, etq.get_height() + 4), pygame.SRCALPHA)
        fondo.fill((0, 0, 0, 145))
        pantalla.blit(fondo, (ex - 4, ey - 2))
        pantalla.blit(etq,   (ex, ey))

#Sección 14 npc Cruz

class Cruz:

    ANCHO_CAJA = int(ANCHO_VIS_PERSONAJE * 0.55)
    ALTO_CAJA  = ALTO_VIS_PERSONAJE

    def __init__(self, x_mundo: float):
        self.x_mundo = float(x_mundo)
        self.nombre  = "Cruz"
        self.activo  = True
        self.atado   = True
        self.vivo    = True

        #Vida propia Cruz
        self.salud = SELUD_CRUZ_INICIAL

        self._mirando_der = True   #controla el flip del sprite al moverse

        self._hoja_atado = HojaSprites(RUTA_CRUZ_ATADO,
                                       ANCHO_CUADRO_CRUZ_ATADO,
                                       ALTO_CUADRO_CRUZ_ATADO) ##
        self._hoja_libre = HojaSprites(RUTA_CRUZ_LIBRE, ancho_cuadro=516, alto_cuadro=512, escala=0.27)
        self._cuadro     = 0
        self._tick       = 0
        self._timer_anim = 0.0
        self._fuente      = pygame.font.SysFont("Arial", 13)
        self._fuente_vida = pygame.font.SysFont("Arial", 11)

        self.rect = pygame.Rect(
            int(self.x_mundo) + (ANCHO_VIS_PERSONAJE - self.ANCHO_CAJA) // 2,
            SUELO - self.ALTO_CAJA,
            self.ANCHO_CAJA, self.ALTO_CAJA
        )

    def liberar(self) -> None:
        self.atado = False

    def recibir_danio(self, cantidad: int) -> None:
        if self.atado:
            return
        self.salud = max(0, self.salud - cantidad)
        if self.salud == 0:
            self.vivo = False

    def actualizar(self, dt: float, objetivo_x: float = None) -> None:
        self._tick += 1

        #Solo sigue a Chicha si está libre, vivo, y se le pasa la posición objetivo
        if not self.atado and self.vivo and objetivo_x is not None:
            diferencia = objetivo_x - self.x_mundo

            #Se mueve solo si está más lejos que la distancia de seguimiento
            if abs(diferencia) > DISTANCIA_SEGUIR:
                if diferencia > 0:
                    self.x_mundo     += VELOCIDAD_CRUZ
                    self._mirando_der = True
                else:
                    self.x_mundo     -= VELOCIDAD_CRUZ
                    self._mirando_der = False

            #Mantener dentro de los límites del mundo
            self.x_mundo = max(0.0, min(ANCHO_MUNDO - ANCHO_VIS_PERSONAJE, self.x_mundo))

            #Actualizar el rect de colisión con la nueva posición
            self.rect.x      = int(self.x_mundo) + (ANCHO_VIS_PERSONAJE - self.ANCHO_CAJA) // 2
            self.rect.bottom = SUELO

        #Velocidad de animación
        vel_anim = 0.65 if self.atado else 0.15
        self._timer_anim += dt
        if self._timer_anim >= vel_anim:
            self._timer_anim = 0.0
            self._cuadro = (self._cuadro + 1) % FRAMES_SPRITESHEET_4

    def cerca_de(self, rect_jugador: pygame.Rect, dist: int = 85) -> bool:
        return self.rect.colliderect(rect_jugador.inflate(dist, dist))

    def dibujar(self, pantalla: pygame.Surface, camara: Camara) -> None:
        if not self.activo:
            return
        hoja  = self._hoja_libre if not self.atado else self._hoja_atado
        frame = hoja.obtener_frame(self._cuadro)

        # Voltear el sprite según la dirección
        if not self.atado and not self._mirando_der:
            frame = pygame.transform.flip(frame, True, False)

        x_pan = camara.aplicar_x(self.x_mundo)
        x_pan += (ANCHO_VIS_PERSONAJE - frame.get_width()) // 2
        y_pan = SUELO - frame.get_height()
        pantalla.blit(frame, (x_pan, y_pan))

        #Etiqueta con nombre
        etq   = self._fuente.render(f"▼ {self.nombre}", True, COLOR_BLANCO)
        ex    = x_pan + ANCHO_VIS_PERSONAJE // 2 - etq.get_width() // 2
        ey    = y_pan - 38
        fondo = pygame.Surface((etq.get_width() + 8, etq.get_height() + 4), pygame.SRCALPHA)
        fondo.fill((0, 0, 0, 145))
        pantalla.blit(fondo, (ex - 4, ey - 2))
        pantalla.blit(etq,   (ex, ey))

        #Barra de vida flotante
        if not self.atado and self.vivo:
            self._dibujar_barra_vida(pantalla, x_pan, y_pan)

    def _dibujar_barra_vida(self, pantalla: pygame.Surface, x_pan: int, y_pan: int) -> None:
        ANCHO_BARRA = 60
        ALTO_BARRA  = 7
        bx = x_pan + ANCHO_VIS_PERSONAJE // 2 - ANCHO_BARRA // 2
        by = y_pan - 22   # justo debajo de la etiqueta del nombre

        # Fondo oscuro
        pygame.draw.rect(pantalla, (40, 40, 40), (bx, by, ANCHO_BARRA, ALTO_BARRA))

        # Relleno que cambia de color según la vida restante
        relleno = max(0, int(ANCHO_BARRA * self.salud / SALUD_CRUZ_MAXIMA))
        if relleno:
            porcentaje = self.salud / SALUD_CRUZ_MAXIMA
            if porcentaje > 0.5:
                color_vida = (60, 180, 60)    # verde
            elif porcentaje > 0.25:
                color_vida = (220, 160, 20)   # naranja
            else:
                color_vida = (200, 40, 40)    # rojo
            pygame.draw.rect(pantalla, color_vida, (bx, by, relleno, ALTO_BARRA))

        # Borde de la barra
        pygame.draw.rect(pantalla, (180, 180, 180), (bx, by, ANCHO_BARRA, ALTO_BARRA), 1)

        # Número de vida en texto pequeño encima de la barra
        txt = self._fuente_vida.render(f"{self.salud}/{SALUD_CRUZ_MAXIMA}", True, COLOR_BLANCO)
        pantalla.blit(txt, (bx + ANCHO_BARRA // 2 - txt.get_width() // 2, by - 13))

#Seccion 15 soldados y boleadoras

class Soldado:

    ANCHO_CAJA = int(ANCHO_VIS_PERSONAJE * 0.55)
    ALTO_CAJA  = ALTO_VIS_PERSONAJE

    def __init__(self, x_mundo: float):
        self.x_mundo = float(x_mundo)
        self.estado  = "avanzando"
        self.activo  = True

        self._hoja_avance = HojaSprites(RUTA_SOLDADO_AVANCE, ancho_cuadro=400, alto_cuadro=396)
        self._hoja_caido  = HojaSprites(RUTA_SOLDADO_CAIDO, ancho_cuadro=400, alto_cuadro=393)
        self._cuadro       = 0
        self._timer_anim   = 0.0

        self.rect = pygame.Rect(
            int(self.x_mundo) + (ANCHO_VIS_PERSONAJE - self.ANCHO_CAJA) // 2,
            SUELO - self.ALTO_CAJA,
            self.ANCHO_CAJA, self.ALTO_CAJA
        )

    def actualizar(self, dt: float, objetivo_x: float) -> bool:

        hizo_contacto = False

        if self.estado == "avanzando":

            if self.x_mundo > objetivo_x:
                self.x_mundo -= VELOCIDAD_SOLDADO
            else:
                self.x_mundo += VELOCIDAD_SOLDADO

            self.rect.x = int(self.x_mundo) + (
                ANCHO_VIS_PERSONAJE - self.ANCHO_CAJA
            ) // 2

            if abs(self.x_mundo - objetivo_x) <= DISTANCIA_ATAQUE_SOLDADO:
                hizo_contacto = True

            self._timer_anim += dt

            if self._timer_anim >= 0.18:
                self._timer_anim = 0.0
                self._cuadro = (self._cuadro + 1) % 4

        elif self.estado == "caido":

            self._timer_anim += dt

            if self._timer_anim >= 0.18:

                self._timer_anim = 0.0

                if self._cuadro < 3:
                    self._cuadro += 1
                else:
                    self._cuadro=3

        return hizo_contacto

    def recibir_impacto(self) -> None:

        self.estado = "caido"
        self._cuadro = 0
        self._timer_anim = 0.0

    def dibujar(self, pantalla: pygame.Surface, camara: Camara) -> None:
        if not self.activo:
            return
        hoja  = self._hoja_caido if self.estado == "caido" else self._hoja_avance
        frame = hoja.obtener_frame(self._cuadro)
        x_pan = camara.aplicar_x(self.x_mundo)
        y_pan = SUELO - ALTO_VIS_PERSONAJE
        pantalla.blit(frame, (x_pan, y_pan))


class Boleadora:

    ANCHO = 68
    ALTO  = 68

    def __init__(self, x_mundo: float, direccion: int):
        self.x_mundo   = float(x_mundo)
        self.direccion = direccion
        self.activo    = True

        ruta_img = RUTA_BOLEADORA
        if ruta_img and os.path.exists(ruta_img):
            cruda = pygame.image.load(ruta_img)
            self._imagen = _quitar_fondo_solido(cruda)
            self._imagen = pygame.transform.scale(self._imagen, (self.ANCHO, self.ALTO))
        else:
            #Circulo marron
            self._imagen = pygame.Surface((self.ANCHO, self.ALTO), pygame.SRCALPHA)
            pygame.draw.circle(self._imagen, (120, 90, 50),
                               (self.ANCHO // 2, self.ALTO // 2), self.ANCHO // 2)
            pygame.draw.circle(self._imagen, (60, 40, 20),
                               (self.ANCHO // 2, self.ALTO // 2), self.ANCHO // 2, 2)

        self.rect = pygame.Rect(int(self.x_mundo), SUELO - 120, self.ANCHO, self.ALTO)

    def actualizar(self, dt: float) -> None:
        self.x_mundo += VELOCIDAD_BOLEADORA * self.direccion
        self.rect.x   = int(self.x_mundo)
        if self.x_mundo < -100 or self.x_mundo > ANCHO_MUNDO + 100:
            self.activo = False

    def dibujar(self, pantalla: pygame.Surface, camara: Camara) -> None:
        if not self.activo:
            return
        x_pan = camara.aplicar_x(self.x_mundo)
        pantalla.blit(self._imagen, (x_pan, self.rect.y))


#Seccion 16 plantas

class PlantaMundo:
    DIST_RECOGIDA = 80

    def __init__(self, datos: dict, x_mundo: float):
        self.datos    = datos
        self.nombre   = datos["nombre"]
        self.recogida = False

        ruta_img = datos.get("imagen", "")
        if ruta_img and os.path.exists(ruta_img):
            cruda = pygame.image.load(ruta_img)
            img   = _quitar_fondo_solido(cruda)
            self._imagen = pygame.transform.scale(img, (ANCHO_VIS_PLANTA, ALTO_VIS_PLANTA))
        else:
            self._imagen = pygame.Surface((ANCHO_VIS_PLANTA, ALTO_VIS_PLANTA), pygame.SRCALPHA)
            self._imagen.fill((55, 155, 45, 220))
            pygame.draw.rect(self._imagen, (140, 255, 90), self._imagen.get_rect(), 3)

        self.rect = pygame.Rect(
            int(x_mundo) - ANCHO_VIS_PLANTA // 2,
            SUELO - ALTO_VIS_PLANTA,
            ANCHO_VIS_PLANTA, ALTO_VIS_PLANTA
        )
        self._tick   = 0
        self._fuente = pygame.font.SysFont("Arial", 11)

    def actualizar(self, dt) -> None:
        self._tick += 1

    def puede_recoger(self, rect_jugador: pygame.Rect) -> bool:
        return not self.recogida and self.rect.colliderect(
            rect_jugador.inflate(self.DIST_RECOGIDA, self.DIST_RECOGIDA))

    def dibujar(self, pantalla: pygame.Surface, camara: Camara) -> None:
        if self.recogida:
            return
        offset_y = int(math.sin(self._tick * 0.07) * 4)
        x_pan    = camara.aplicar_x(self.rect.x)
        y_pan    = self.rect.y + offset_y

        halo_r = ANCHO_VIS_PLANTA // 2 + 8
        halo   = pygame.Surface((halo_r * 2, halo_r * 2), pygame.SRCALPHA)
        pygame.draw.circle(halo, (80, 200, 70, 55), (halo_r, halo_r), halo_r)
        pantalla.blit(halo, (x_pan - 8, y_pan - 8))
        pantalla.blit(self._imagen, (x_pan, y_pan))

        etq = self._fuente.render(self.nombre, True, COLOR_BLANCO)
        pantalla.blit(etq, (x_pan + ANCHO_VIS_PLANTA // 2 - etq.get_width() // 2,
                            y_pan - 14))


#Seccion de datos (plantas e historia ranquel)

PLANTAS_LLANCAY = [
    {
        "nombre": "Marcela", "nombre_cient": "Achyrocline satureioides",
        "propiedad": "Antiinflamatoria", "curacion": 25,
        "imagen": RUTA_MARCELA,
        "descripcion": (
            "bla bla bla dialogo dialogo"
            "bla bla bla"
            "dialogo dialogo bla bla"
        ),
    },
    {
        "nombre": "Paja colorada", "nombre_cient": "Cortaderia selloana",
        "propiedad": "Vendaje natural", "curacion": 10,
        "imagen": RUTA_PAJA_COLORADA,
        "descripcion": (
            "Sus hojas largas y resistentes, bien secas, sirven para "
            "envolver heridas y detener el sangrado cuando no hay tela."
        ),
    },
    {
        "nombre": "Jarilla", "nombre_cient": "Larrea divaricata",
        "propiedad": "Antiseptica", "curacion": 15,
        "imagen": RUTA_JARILLA,
        "descripcion": (
            "El aceite de jarilla limpia las heridas y evita que se "
            "infecten. Frotala directo sobre el corte antes de vendarlo."
        ),
    },
    {
        "nombre": "Tola serrana", "nombre_cient": "Baccharis boliviensis",
        "propiedad": "Alivia el cansancio y el dolor de cabeza",
        "curacion": 30, "imagen": RUTA_TOLA_SERRANA,
        "descripcion": (
            "La tola serrana vive entre las piedras de las sierras. "
            "bla bla bla dialogo dialogo"
            "bla bla dialogo"
        ),
    },
]

HISTORIA_RANQUEL = (
    "Dialogo bla bla bla."
    "Dialogo bla bla bla."
    "Dialogo bla bla bla."
    "bla bla bla."
)

COMBINACIONES_DIARIO = [
    {
        "nombre":       "Cataplasma curativo",
        "ingredientes": ["Jarilla", "Marcela"],
        "efecto":       "Cura 50 puntos. Limpia la infeccion y baja la inflamacion.",
    },
    {
        "nombre":       "Unguento serrano",
        "ingredientes": ["Jarilla", "Tola serrana"],
        "efecto":       "Cura 60 puntos. Ideal para heridas de camino largo.",
    },
    {
        "nombre":       "Infusion reconfortante",
        "ingredientes": ["Marcela", "Paja colorada"],
        "efecto":       "Cura 40 puntos. Calma el cuerpo y detiene el sangrado.",
    },
]

# Reflexiones de Chicha sobre los pueblos originarios.
# La "clave" identifica cuándo se desbloquea cada entrada.
REFLEXIONES_DIARIO = [
    {
        "clave":  "llancay_ranquel",
        "titulo": "Sobre Llancay y los ranqueles",
        "texto":  (
            "Nunca pense que la pampa tuviera duenos antes que nosotros. "
            "Llancay me hablo de los ranqueles como si estuvieran aca ayer nomas. "
            "Y en cierta forma tienen razon: la tierra guarda memoria aunque "
            "los hombres hagamos todo lo posible por borrarla. "
            "Me pregunto cuantas cosas mas me ensenaron mal."
        ),
    },
    {
        "clave":  "reflexion_cruz",
        "titulo": "Sobre Cruz y lo que carga",
        "texto":  (
            "Cruz dice que el Coronel lo dejo atado de escarmiento. "
            "El mismo ejercito que me persigue a mi es el que aplasto "
            "a los pueblos de esta tierra. Eso me cambia algo adentro. "
            "No se bien que todavia, pero algo."
        ),
    },
]

# ══════════════════════════════════════════════════════
# DIARIO DE CHICHA
# ══════════════════════════════════════════════════════

class Diario:
    PESTANIA_PLANTAS     = 0
    PESTANIA_REFLEXIONES = 1

    # ── Geometría del diario (ajustá si la imagen cambia de tamaño) ──────────
    # El diario se escala para ocupar casi toda la pantalla
    ANCHO_DIARIO = 1150
    ALTO_DIARIO  = 480

    # Márgenes internos de CADA página respecto al borde de la imagen escalada
    # Página izquierda: desde el borde izq hasta el centro (espiral)
    # Página derecha:   desde el centro hasta el borde derecho
    MARGEN_IZQ_PAG    = 110    # margen izq dentro de la página izquierda
    MARGEN_DER_PAG    = 55    # margen der dentro de la página derecha
    MARGEN_SUPERIOR   = 52    # desde dónde empieza el primer renglón con texto
    MARGEN_ESPIRAL    = 55   # zona muerta alrededor de la espiral central

    # Altura de cada renglón en la imagen (medida visual de los renglones del cuaderno)
    # Ajustá este valor hasta que el texto quede centrado en cada línea
    ALTO_RENGLON = 21

    # Primer renglón con texto (en píxeles desde el tope del área de página)
    PRIMER_RENGLON_Y = 55

    # Animación del diario
    VEL_ANIM_DIARIO = 0.22   # segundos por frame

    def __init__(self):
        self.abierto   = False
        self._pestania = self.PESTANIA_PLANTAS
        self._scroll   = 0   # en unidades de renglón (no píxeles)
        self._animando_enter = False

        # Entradas desbloqueadas
        self.plantas_descubiertas      = []
        self.reflexiones_desbloqueadas = []

        # Fuentes (manuscrita sobre renglones → cursiva, tamaño que entre en el renglón)
        self._f_titulo    = pygame.font.SysFont("Georgia", 18, bold=True)
        self._f_subtitulo = pygame.font.SysFont("Georgia", 15, bold=True)
        self._f_texto     = pygame.font.SysFont("Georgia", 13)
        self._f_cient     = pygame.font.SysFont("Georgia", 12, italic=True)
        self._f_pestania  = pygame.font.SysFont("Arial",   13, bold=True)
        self._f_bloqueado = pygame.font.SysFont("Arial",   12)
        self._f_pista     = pygame.font.SysFont("Arial",   11)

        # Colores de tinta sobre papel amarillento
        self._color_titulo    = (80, 45, 10)      # marrón oscuro
        self._color_texto     = (55, 35, 10)      # sepia
        self._color_cient     = (70, 90, 50)      # verde oliva
        self._color_bloqueado = (160, 145, 120)   # gris arena
        self._color_combo     = (40, 80, 40)      # verde oscuro
        self._color_pestania_act = (80, 45, 10)
        self._color_pestania_no  = (150, 125, 95)

        # Cargar imagen de fondo del diario
        self._fondo_diario = None
        if RUTA_FONDO_DIARIO and os.path.exists(RUTA_FONDO_DIARIO):
            img = pygame.image.load(RUTA_FONDO_DIARIO).convert_alpha()
            self._fondo_diario = pygame.transform.scale(
                img, (self.ANCHO_DIARIO, self.ALTO_DIARIO))
        else:
            # Placeholder: rectángulo color papel si no hay imagen
            self._fondo_diario = pygame.Surface(
                (self.ANCHO_DIARIO, self.ALTO_DIARIO), pygame.SRCALPHA)
            self._fondo_diario.fill((210, 195, 155))
            pygame.draw.rect(self._fondo_diario, (140, 100, 60),
                             self._fondo_diario.get_rect(), 4)

        # Spritesheet de animación
        self._hoja_anim    = None
        self._cuadro_anim  = 0
        self._timer_anim   = 0.0
        self._total_frames = 4
        if (RUTA_ANIM_DIARIO and os.path.exists(RUTA_ANIM_DIARIO)
                and ANCHO_CUADRO_ANIM_DIARIO > 0):
            hoja_cruda = pygame.image.load(RUTA_ANIM_DIARIO).convert_alpha()
            hoja_cruda.set_colorkey(COLOR_LLAVE)
            self._hoja_anim = HojaSprites(
                RUTA_ANIM_DIARIO,
                ANCHO_CUADRO_ANIM_DIARIO,
                ALTO_CUADRO_ANIM_DIARIO,
                escala=0.55   # ajustá para que quepa en la página izquierda
            )
            self._total_frames = self._hoja_anim.total_cuadros

        # Posición del panel del diario (centrado en pantalla)
        self._dx = (ANCHO_PANTALLA - self.ANCHO_DIARIO) // 2
        self._dy = (ALTO_PANTALLA  - self.ALTO_DIARIO)  // 2

        # Centro horizontal del diario (donde está la espiral)
        self._centro_x = self._dx + self.ANCHO_DIARIO // 2

        # Áreas de texto de cada página en coordenadas de PANTALLA
        # Página izquierda: plantas / reflexiones
        self._area_izq = pygame.Rect(
            self._dx + self.MARGEN_IZQ_PAG,
            self._dy + self.PRIMER_RENGLON_Y,
            self._centro_x - self._dx - self.MARGEN_IZQ_PAG - self.MARGEN_ESPIRAL,
            self.ALTO_DIARIO - self.PRIMER_RENGLON_Y - 30,
        )
        # Página derecha: continuación del contenido
        self._area_der = pygame.Rect(
            self._centro_x + self.MARGEN_ESPIRAL,
            self._dy + self.PRIMER_RENGLON_Y,
            self.ANCHO_DIARIO // 2 - self.MARGEN_DER_PAG - self.MARGEN_ESPIRAL,
            self.ALTO_DIARIO - self.PRIMER_RENGLON_Y - 30,
        )

        # Pestañas (encima del diario, arriba a la izquierda y derecha)
        self._rect_p_plantas     = pygame.Rect(self._dx + 110,  self._dy - 30, 130, 30)
        self._rect_p_reflexiones = pygame.Rect(self._dx + 248, self._dy - 30, 155, 30)

    def _y_renglon(self, area: pygame.Rect, numero: int) -> int:

        return area.y + numero * self.ALTO_RENGLON + self.ALTO_RENGLON // 2

    def _renglones_disponibles(self, area: pygame.Rect) -> int:
        return area.height // self.ALTO_RENGLON

    def descubrir_planta(self, nombre: str) -> None:
        if nombre not in self.plantas_descubiertas:
            self.plantas_descubiertas.append(nombre)

    def desbloquear_reflexion(self, clave: str) -> None:
        if clave not in self.reflexiones_desbloqueadas:
            self.reflexiones_desbloqueadas.append(clave)

    def alternar(self) -> None:
        self.abierto = not self.abierto
        if self.abierto:
            self._scroll = 0

    def manejar_evento(self, evento: pygame.event.Event) -> bool:
        if not self.abierto:
            return False

        if evento.type == pygame.KEYDOWN:
            # Si presiona ENTER, activamos la animación y reiniciamos el contador de cuadros
            if evento.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                self._animando_enter = True
                self._cuadro_anim = 0
                return True
                
            if evento.key in (TECLA_DIARIO, pygame.K_ESCAPE):
                self.abierto = False
                return True
            if evento.key == pygame.K_UP:
                self._scroll = max(0, self._scroll - 1)
                return True
            if evento.key == pygame.K_DOWN:
                self._scroll += 1
                return True

        if evento.type == pygame.MOUSEWHEEL:
            self._scroll = max(0, self._scroll - evento.y)
            return True

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if self._rect_p_plantas.collidepoint(evento.pos):
                self._pestania = self.PESTANIA_PLANTAS
                self._scroll   = 0
                return True
            if self._rect_p_reflexiones.collidepoint(evento.pos):
                self._pestania = self.PESTANIA_REFLEXIONES
                self._scroll   = 0
                return True

        return True


    def actualizar(self, dt: float) -> None:
        if not self.abierto or self._hoja_anim is None:
            return
        self._timer_anim += dt
        if self._timer_anim >= self.VEL_ANIM_DIARIO:
            self._timer_anim  = 0.0
            self._cuadro_anim = (self._cuadro_anim + 1) % self._total_frames


    def dibujar(self, pantalla: pygame.Surface) -> None:
        if not self.abierto:
            return

        sombra = pygame.Surface((ANCHO_PANTALLA, ALTO_PANTALLA), pygame.SRCALPHA)
        sombra.fill((0, 0, 0, 200))
        pantalla.blit(sombra, (0, 0))

        pantalla.blit(self._fondo_diario, (self._dx, self._dy))

        self._dibujar_pestania(pantalla) ##

        renglones = self._construir_renglones()
        renglones_visibles = renglones[self._scroll:]

        cap_izq = self._renglones_disponibles(self._area_izq)
        cap_der = self._renglones_disponibles(self._area_der)


        reng_izq = renglones_visibles[:cap_izq]
        for i, renglon in enumerate(reng_izq):
            self._dibujar_renglon(pantalla, renglon, self._area_izq, i)

        # Página derecha
        reng_der = renglones_visibles[cap_izq:cap_izq + cap_der]
        for i, renglon in enumerate(reng_der):
            self._dibujar_renglon(pantalla, renglon, self._area_der, i)

        if getattr(self, "_animando_enter", False) and self._hoja_anim is not None:
            frame = self._hoja_anim.obtener_frame(self._cuadro_anim)
            if frame:
                x_anim = self._area_izq.right - frame.get_width() - 8
                y_anim = self._area_izq.bottom - frame.get_height() - 4
                pantalla.blit(frame, (x_anim, y_anim))
                self._cuadro_anim += 1
            else:
                self._animando_enter = False

        pista = self._f_pista.render(
            "Enter: animar | Rueda / flechas: pasar pagina | J / Esc: cerrar",
            True, (120, 95, 60))
        px = self._dx + self.ANCHO_DIARIO // 2 - pista.get_width() // 2
        py = self._dy + self.ALTO_DIARIO - 16
        pantalla.blit(pista, (px, py))

        # Página derecha
        reng_der = renglones_visibles[cap_izq:cap_izq + cap_der]
        for i, renglon in enumerate(reng_der):
            self._dibujar_renglon(pantalla, renglon, self._area_der, i)

        if self._animando_enter and self._hoja_anim is not None:
            frame = self._hoja_anim.obtener_frame(self._cuadro_anim)
            
            if frame:
                x_anim = self._area_izq.right - frame.get_width() - 8
                y_anim = self._area_izq.bottom - frame.get_height() - 4
                pantalla.blit(frame, (x_anim, y_anim))
                self._cuadro_anim += 1  # Avanzar cuadro
            else:

                self._animando_enter = False


        pista = self._f_pista.render(
            "Enter: animar | Rueda / flechas: pasar pagina | J / Esc: cerrar",
            True, (120, 95, 60))
        px = self._dx + self.ANCHO_DIARIO // 2 - pista.get_width() // 2
        py = self._dy + self.ALTO_DIARIO - 16
        pantalla.blit(pista, (px, py))


    def _construir_renglones(self) -> list:
        renglones = []

        if self._pestania == self.PESTANIA_PLANTAS:
            for datos in PLANTAS_LLANCAY:
                nombre   = datos["nombre"]
                conocida = nombre in self.plantas_descubiertas

                if conocida:
                    renglones.append({"tipo": "titulo",  "texto": f"* {nombre}"})
                    renglones.append({"tipo": "cient",   "texto": datos["nombre_cient"]})
                    renglones.append({"tipo": "texto",   "texto": f"Propiedad: {datos['propiedad']}"})

                    for frag in self._partir_texto(datos["descripcion"], 52):
                        renglones.append({"tipo": "texto", "texto": frag})

                    combos = [
                        c for c in COMBINACIONES_DIARIO
                        if nombre in c["ingredientes"]
                        and all(ing in self.plantas_descubiertas
                                for ing in c["ingredientes"])
                    ]
                    for c in combos:
                        ingr  = " + ".join(c["ingredientes"])
                        for frag in self._partir_texto(
                                f"Mezcla: {c['nombre']} ({ingr}) -> {c['efecto']}", 52):
                            renglones.append({"tipo": "combo", "texto": frag})
                else:
                    renglones.append({"tipo": "bloqueado",
                                      "texto": f"* {nombre}  [no descubierta]"})
                renglones.append({"tipo": "separador", "texto": ""})

        else:  # REFLEXIONES
            for ref in REFLEXIONES_DIARIO:
                desbloqueada = ref["clave"] in self.reflexiones_desbloqueadas
                if desbloqueada:
                    renglones.append({"tipo": "titulo", "texto": ref["titulo"]})
                    for frag in self._partir_texto(ref["texto"], 52):
                        renglones.append({"tipo": "texto", "texto": frag})
                else:
                    renglones.append({"tipo": "bloqueado",
                                      "texto": f"{ref['titulo']}  [pendiente]"})
                renglones.append({"tipo": "separador", "texto": ""})

        return renglones

    @staticmethod
    def _partir_texto(texto: str, max_chars: int) -> list:
        """
        Divide un texto en fragmentos de máximo max_chars caracteres,
        respetando los espacios. Así cada fragmento ocupa un renglón.
        """
        palabras   = texto.split()
        fragmentos = []
        linea      = ""
        for palabra in palabras:
            candidata = f"{linea} {palabra}".strip()
            if len(candidata) <= max_chars:
                linea = candidata
            else:
                if linea:
                    fragmentos.append(linea)
                linea = palabra
        if linea:
            fragmentos.append(linea)
        return fragmentos if fragmentos else [""]

    def _dibujar_renglon(self, pantalla, renglon: dict, area: pygame.Rect, numero: int) -> None:
        """
        Dibuja un renglón centrado verticalmente en su línea del cuaderno.
        numero es el índice dentro del área (0 = primer renglón visible).
        """
        tipo  = renglon["tipo"]
        texto = renglon["texto"]

        if tipo == "separador" or not texto:
            return   # renglón en blanco, no se dibuja nada

        # Elegir fuente y color según el tipo
        if tipo == "titulo":
            fuente = self._f_subtitulo
            color  = self._color_titulo
        elif tipo == "cient":
            fuente = self._f_cient
            color  = self._color_cient
        elif tipo == "combo":
            fuente = self._f_texto
            color  = self._color_combo
        elif tipo == "bloqueado":
            fuente = self._f_bloqueado
            color  = self._color_bloqueado
        else:   # "texto"
            fuente = self._f_texto
            color  = self._color_texto

        surf = fuente.render(texto, True, color)

        y_centro = area.y + numero * self.ALTO_RENGLON + self.ALTO_RENGLON // 2
        y_blit   = y_centro - surf.get_height() // 2


        pantalla.blit(surf, (area.x, y_blit))

class CinematicaIntroduccion:

    _ESC_TEXTOS_FECHA = 0
    _ESC_NARRATIVA    = 1
    _ESC_PAMPA_CAM    = 2
    _ESC_RENGUEO      = 3
    _ESC_TITULO       = 4
    _ESC_FIN          = 5

    DURACIONES = {
        0: 5.0,   #"Argentina" / "1870"
        1: 6.0,   #Textos narrativos
        2: 4.0,   #Camara paronamica sola
        3: 8.0,   #Chicha rengueando
        4: 4.0,   #Titulo del capitulo
    }

    TEXTOS_RENGUEO = [
        "Herido y solo...",
        "Debía aprender a sobrevivir.",
        "Las llanuras guardaban peligros.",
        "Pero también esperanza.",
    ]

    def __init__(self, pantalla: pygame.Surface):
        self._pantalla = pantalla
        self._escena   = self._ESC_TEXTOS_FECHA
        self._timer    = 0.0
        self.terminada = False

        self._f_grande = pygame.font.SysFont("Georgia", 72, bold=True)
        self._f_narr   = pygame.font.SysFont("Georgia", 26, italic=True)
        self._f_titulo = pygame.font.SysFont("Georgia", 48, bold=True)
        self._f_subtit = pygame.font.SysFont("Georgia", 32)

        # Hoja de Chicha rengueando
        self._hoja_rengueo = HojaSprites(RUTA_CHICHA_RENGUEANDO,
                                         ANCHO_CUADRO_PERSONAJE, ALTO_CUADRO_PERSONAJE,
                                         ESCALA_CINEMATICA)

        ruta_fondo_cine = RUTA_CINE_PAMPA if RUTA_CINE_PAMPA else RUTA_FONDO_PAMPA
        self._fondo_pampa = cargar_imagen(ruta_fondo_cine, (ANCHO_MUNDO, ALTO_PANTALLA))

        self._cuadro_sprite = 0
        self._timer_sprite  = 0.0
        self._vel_sprite    = 0.18

        self._camara_x   = 0.0
        self._vel_camara = 70.0

        self._indice_texto    = 0
        self._timer_texto     = 0.0
        self._intervalo_texto = 2.0

        self._chicha_x = 200.0

        # viento
        self._sonido_viento = reproducir_sonido(RUTA_SONIDO_VIENTO, volumen=0.4)
        if self._sonido_viento:
            self._sonido_viento.play(loops=-1)

    def actualizar(self, dt: float) -> None:
        if self.terminada:
            return

        self._timer        += dt
        self._timer_sprite  += dt

        if self._timer_sprite >= self._vel_sprite:
            self._timer_sprite  = 0.0
            self._cuadro_sprite = (self._cuadro_sprite + 1) % 4

        duracion = self.DURACIONES.get(self._escena, 3.0)

        if self._escena == self._ESC_PAMPA_CAM:
            self._camara_x = min(self._camara_x + self._vel_camara * dt,
                                 ANCHO_MUNDO - ANCHO_PANTALLA)

        elif self._escena == self._ESC_RENGUEO:
            self._chicha_x = min(self._chicha_x + 55.0 * dt, ANCHO_MUNDO - 200.0)
            self._camara_x = max(0.0, min(self._chicha_x - MARGEN_CAM_X,
                                          ANCHO_MUNDO - ANCHO_PANTALLA))
            self._timer_texto += dt
            if (self._timer_texto >= self._intervalo_texto
                    and self._indice_texto < len(self.TEXTOS_RENGUEO) - 1):
                self._indice_texto += 1
                self._timer_texto   = 0.0

        if self._timer >= duracion:
            self._timer         = 0.0
            self._cuadro_sprite = 0
            self._escena       += 1
            if self._escena == self._ESC_RENGUEO:
                self._indice_texto = 0
                self._timer_texto  = 0.0
            if self._escena >= self._ESC_FIN:
                self.terminada = True
                self._detener_viento()

    def _detener_viento(self) -> None:
        if self._sonido_viento:
            self._sonido_viento.stop()

    def dibujar(self) -> None:
        if self.terminada:
            return

        pantalla = self._pantalla
        duracion = self.DURACIONES.get(self._escena, 3.0)
        progreso = max(0.0, min(1.0, self._timer / duracion))

        #ESCENA 1: "Argentina" "1870"
        if self._escena == self._ESC_TEXTOS_FECHA:
            pantalla.fill(COLOR_NEGRO)
            mitad = duracion / 2
            if self._timer < mitad:
                p_local = self._timer / mitad
                self._texto_fadeio(pantalla, "Argentina", self._f_grande, p_local)
            else:
                p_local = (self._timer - mitad) / mitad
                self._texto_fadeio(pantalla, "1870", self._f_grande, p_local)

        #ESCENA 2: textos narrativos
        elif self._escena == self._ESC_NARRATIVA:
            pantalla.fill(COLOR_NEGRO)
            lineas = [
                "Tras escapar de quienes buscaban capturarlo...",
                "Chicha emprendía una travesía incierta.",
            ]
            for i, linea in enumerate(lineas):
                umbral = (i + 1) / (len(lineas) + 1)
                if progreso >= umbral:
                    sup = self._f_narr.render(linea, True, COLOR_BLANCO)
                    sup.set_alpha(min(255, int(255 * (progreso - umbral) / 0.3)))
                    x = ANCHO_PANTALLA // 2 - sup.get_width() // 2
                    y = ALTO_PANTALLA  // 2 - 30 + i * 55
                    pantalla.blit(sup, (x, y))

        #--ESCENA 3: pampa paronamico, camara, desplazandose
        elif self._escena == self._ESC_PAMPA_CAM:
            pantalla.blit(self._fondo_pampa, (-int(self._camara_x), 0))
            if progreso < 0.25:
                self._overlay(pantalla, int(255 * (1.0 - progreso / 0.25)))

        #--ESCENA 4: Chicha rengueando
        elif self._escena == self._ESC_RENGUEO:
            pantalla.blit(self._fondo_pampa, (-int(self._camara_x), 0))
            frame    = self._hoja_rengueo.obtener_frame(self._cuadro_sprite)
            x_chicha = int(self._chicha_x - self._camara_x)
            y_chicha = SUELO - frame.get_height()
            pantalla.blit(frame, (x_chicha, y_chicha))
            for i in range(self._indice_texto + 1):
                sup = self._f_narr.render(self.TEXTOS_RENGUEO[i], True, COLOR_HONOR_ORO)
                pantalla.blit(sup, (ANCHO_PANTALLA // 2 - sup.get_width() // 2,
                                    120 + i * 45))

        #--ESCENA 5: titulo del Capitulo
        elif self._escena == self._ESC_TITULO:
            alpha_bg = min(255, int(255 * progreso * 3))
            ov = pygame.Surface((ANCHO_PANTALLA, ALTO_PANTALLA))
            ov.set_alpha(alpha_bg)
            ov.fill(COLOR_NEGRO)
            pantalla.blit(ov, (0, 0))
            if progreso > 0.25:
                alpha_t = min(255, int(255 * (progreso - 0.25) / 0.4))
                t1 = self._f_titulo.render("Capítulo 1", True, COLOR_HONOR_ORO)
                t2 = self._f_subtit.render("La Pampa", True, COLOR_BLANCO)
                t1.set_alpha(alpha_t)
                t2.set_alpha(alpha_t)
                pantalla.blit(t1, (ANCHO_PANTALLA // 2 - t1.get_width() // 2,
                                   ALTO_PANTALLA  // 2 - 60))
                pantalla.blit(t2, (ANCHO_PANTALLA // 2 - t2.get_width() // 2,
                                   ALTO_PANTALLA  // 2 + 10))

    def _texto_fadeio(self, pantalla, texto, fuente, progreso):
        if progreso < 0.3:
            alpha = int(255 * (progreso / 0.3))
        elif progreso > 0.7:
            alpha = int(255 * (1.0 - (progreso - 0.7) / 0.3))
        else:
            alpha = 255
        sup = fuente.render(texto, True, COLOR_BLANCO)
        sup.set_alpha(alpha)
        pantalla.blit(sup, (ANCHO_PANTALLA // 2 - sup.get_width() // 2,
                            ALTO_PANTALLA  // 2 - sup.get_height() // 2))

    def _overlay(self, pantalla, alpha):
        ov = pygame.Surface((ANCHO_PANTALLA, ALTO_PANTALLA))
        ov.set_alpha(alpha)
        ov.fill(COLOR_NEGRO)
        pantalla.blit(ov, (0, 0))

    def finalizar(self) -> None:
        self.terminada = True
        self._detener_viento()


#Seccion 19 ayudas pantalla

def _dibujar_intro_textual(pantalla, titulo, paginas, pagina, f_tit, f_ital, f_ctrl):
    overlay = pygame.Surface((ANCHO_PANTALLA, ALTO_PANTALLA), pygame.SRCALPHA)
    overlay.fill(COLOR_OVERLAY_INTRO)
    pantalla.blit(overlay, (0, 0))
    tit = f_tit.render(titulo, True, COLOR_HONOR_ORO)
    pantalla.blit(tit, (ANCHO_PANTALLA // 2 - tit.get_width() // 2, 90))
    if pagina < len(paginas):
        for i, linea in enumerate(paginas[pagina].split("\n")):
            s = f_ital.render(linea, True, COLOR_BLANCO)
            pantalla.blit(s, (ANCHO_PANTALLA // 2 - s.get_width() // 2, 268 + i * 40))
    pista = f_ctrl.render("[Espacio] continuar", True, (140, 140, 140))
    pantalla.blit(pista, (ANCHO_PANTALLA // 2 - pista.get_width() // 2, ALTO_PANTALLA - 52))


def _dibujar_fundido(pantalla, timer, duracion, texto, fuente):
    progreso = 1.0 - timer / duracion
    alpha    = int(255 * max(0.0, min(1.0, progreso)))
    ov = pygame.Surface((ANCHO_PANTALLA, ALTO_PANTALLA))
    ov.set_alpha(alpha)
    ov.fill(COLOR_NEGRO)
    pantalla.blit(ov, (0, 0))
    if alpha > 100:
        sup = fuente.render(texto, True, COLOR_HONOR_ORO)
        sup.set_alpha(alpha)
        pantalla.blit(sup, (ANCHO_PANTALLA // 2 - sup.get_width() // 2,
                            ALTO_PANTALLA  // 2))


def _dibujar_etiqueta_capitulo(pantalla, fuente, titulo, region):
    txt   = fuente.render(f"{titulo}  A  {region}", True, (200, 195, 185))
    fondo = pygame.Surface((txt.get_width() + 16, txt.get_height() + 6), pygame.SRCALPHA)
    fondo.fill((0, 0, 0, 130))
    x = ANCHO_PANTALLA // 2 - fondo.get_width() // 2
    pantalla.blit(fondo, (x, 3))
    pantalla.blit(txt,   (x + 8, 6))


#Seccion 20 escena cinematica base

class EscenaCinematica(EscenaBase):

    def __init__(self, gestor: GestorEscenas):
        super().__init__(gestor)
        self._cinematica = CinematicaIntroduccion(gestor.pantalla)
        reproducir_musica(RUTA_MUSICA_CINEMATICA)

    def manejar_evento(self, evento: pygame.event.Event) -> None:
        if evento.type == pygame.KEYDOWN:
            if evento.key in (pygame.K_SPACE, pygame.K_ESCAPE, pygame.K_RETURN):
                self._cinematica.finalizar()

    def actualizar(self, dt: float) -> None:
        self._cinematica.actualizar(dt)
        if self._cinematica.terminada:
            self.gestor.cambiar("capitulo_1")

    def dibujar(self, pantalla: pygame.Surface) -> None:
        self._cinematica.dibujar()
        fuente = pygame.font.SysFont("Arial", 13)
        pista  = fuente.render("Espacio para saltar", True, (80, 80, 80))
        pantalla.blit(pista, (ANCHO_PANTALLA - pista.get_width() - 12,
                              ALTO_PANTALLA  - pista.get_height() - 10))


#Seccion 21 menu principal (imagen limpia + zonas invisibles)

class MenuPrincipal(EscenaBase):

    ZONAS_BOTONES = [
        ("empezar", pygame.Rect(90, 440, 270, 50)),
        ("cargar",  pygame.Rect(90, 502, 270, 50)),
        ("salir",   pygame.Rect(90, 564, 270, 50)),
    ]

    # Dimensiones exactas del spritesheet del menú
    ANCHO_CUADRO_MENU = 333   # 2000 px ÷ 6 frames
    ALTO_CUADRO_MENU  = 666   # alto total del spritesheet
    TOTAL_FRAMES_MENU = 6
    ESCALA_MENU       = 1.0  # ajustá este número para hacer al personaje más grande o más chico

    def __init__(self, gestor: GestorEscenas):
        super().__init__(gestor)
        self._fondo          = cargar_imagen(RUTA_FONDO_MENU, (ANCHO_PANTALLA, ALTO_PANTALLA))
        self._tiene_guardado = os.path.exists(ARCHIVO_GUARDADO)
        self._mostrar_debug  = False

        # Cargar el spritesheet del personaje para el menú
        self._hoja_menu = HojaSprites(
            RUTA_SPRITESHEET_MENU,
            self.ANCHO_CUADRO_MENU,
            self.ALTO_CUADRO_MENU,
            self.ESCALA_MENU
        )

        # Variables de animación
        self._cuadro_menu  = 0       # frame actual
        self._timer_menu   = 0.0     # acumulador de tiempo
        self._vel_anim_menu = 1.0   # segundos por frame (bajá para más rápido, subí para más lento)

        reproducir_musica(RUTA_MUSICA_MENU)

    def manejar_evento(self, evento: pygame.event.Event) -> None:
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            for accion, rect in self.ZONAS_BOTONES:
                if rect.collidepoint(evento.pos):
                    self._ejecutar(accion)
                    break
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                self._ejecutar("empezar")
            elif evento.key == pygame.K_ESCAPE:
                self._ejecutar("salir")

    def _ejecutar(self, accion: str) -> None:
        if accion == "empezar":
            self.gestor.cambiar("cinematica")
        elif accion == "cargar":
            datos = cargar_partida()
            if datos:
                self.gestor.aplicar_guardado(datos)
                self.gestor.cambiar("capitulo_1", jugador_x=datos.get("jugador_x", 200.0))
        elif accion == "salir":
            pygame.quit()
            sys.exit()

    def actualizar(self, dt: float) -> None:
        # Avanzar la animación del personaje
        self._timer_menu += dt
        if self._timer_menu >= self._vel_anim_menu:
            self._timer_menu  = 0.0
            self._cuadro_menu = (self._cuadro_menu + 1) % self.TOTAL_FRAMES_MENU

    def dibujar(self, pantalla: pygame.Surface) -> None:
        # 1. Dibujar el fondo del menú
        pantalla.blit(self._fondo, (0, 0))
        # 2. Dibujar el personaje animado encima del fondo
        frame = self._hoja_menu.obtener_frame(self._cuadro_menu)
        # Posición del personaje en pantalla — ajustá x e y a donde quieras ubicarlo
        x_personaje = ANCHO_PANTALLA - frame.get_width() - 280   # esquina derecha
        y_personaje = ALTO_PANTALLA  - frame.get_height() + 70   # pegado al suelo
        pantalla.blit(frame, (x_personaje, y_personaje))

        # 3. Debug opcional: muestra los Rects de botones en rojo
        if self._mostrar_debug:
            for _, rect in self.ZONAS_BOTONES:
                pygame.draw.rect(pantalla, (255, 0, 0), rect, 2)


#Seccion 22 capítulo 1

_FASE_INTRO          = "intro"
_FASE_EXPLO          = "exploracion"
_FASE_DLG_LL         = "dlg_llancay"
_FASE_DLG_CRUZ_PREV  = "dlg_cruz_previo"
_FASE_DECISION       = "decision_cruz"
_FASE_COMBATE        = "combate"
_FASE_TRANS          = "transicion"

_INTRO_CAP1 = [
    "Argentina, 1870.",
    'Benjamín "Chicha" Pereyra escapa del regimiento\ndel Coronel Ibañez.\nHerido. Sin caballo. Sin provisiones.',
    "Delante: Kilometros y kilometros de pampa húmeda.\nDetrás: el ejercito.",
    "Pero la pampa guarda sus propios secretos\npara quienes saben escucharla.",
]

# Distancia la que aparece Cruz atado al poste
POSICION_CRUZ = 2300


class CapituloPampa(EscenaBase):

    TITULO = "Capitulo 1 La llanura no perdona"
    REGION = "Pampa humeda, Buenos Aires· 1870"
    NOMBRE = "capitulo_1"

    def __init__(self, gestor: GestorEscenas, jugador_x: float = 200.0):
        super().__init__(gestor)

        # Cargar los fondos como extensión del mapa sin estirarlos
        ANCHO_TRAMO = ANCHO_MUNDO // 2  # Cada imagen ocupará la mitad del ancho total del mundo (1920px)
        self._fondos_pampa = [
            cargar_imagen(RUTA_FONDO_PAMPA, (ANCHO_TRAMO, ALTO_PANTALLA)),
            cargar_imagen(RUTA_FONDO_PAMPA2, (ANCHO_TRAMO, ALTO_PANTALLA))
        ]
        self._camara = Camara()

        self._jugador = Jugador(jugador_x, gestor.partida["salud"], gestor.partida["honor"])
        self._llancay = Llancay(1400)
        self._cruz    = Cruz(POSICION_CRUZ)

        self._inventario = Inventario(gestor.partida["inventario"])
        self._plantas_mundo = [
            PlantaMundo(PLANTAS_LLANCAY[0],  550),
            PlantaMundo(PLANTAS_LLANCAY[1],  800),
            PlantaMundo(PLANTAS_LLANCAY[2], 1050),
            PlantaMundo(PLANTAS_LLANCAY[3], 1280),
        ]

        # Sistema de combate: listas dinanmicas de soldados y boleadoras
        self._soldados   = []
        self._boleadoras = []
        self._cooldown_lanzamiento = 0.0
        self._combate_resuelto     = False

        self._dialogo = SistemaDialogo()
        self._hud     = HUD()
        self._menu_curacion = MenuCuracion()
        self._diario = Diario()

        self._fase          = _FASE_INTRO
        self._pagina_intro   = 0
        self._llancay_hablo  = False
        self._cruz_dialogo_disparado = False
        self._timer_trans    = 3.0

        # Spritesheet de Cruz para mini-cinematica
        self._hoja_cruz_cine = HojaSprites(RUTA_CRUZ_CINE,
                                           ANCHO_CUADRO_CRUZ_ATADO,
                                           ALTO_CUADRO_CRUZ_ATADO,
                                           escala=0.8)
        self._cuadro_cruz_cine = 0
        self._timer_cruz_cine  = 0.0

        self._f_tit  = pygame.font.SysFont("Georgia", 28, bold=True)
        self._f_ital = pygame.font.SysFont("Georgia", 20, italic=True)
        self._f_ctrl = pygame.font.SysFont("Arial",   15)
        self._f_etq  = pygame.font.SysFont("Arial",   13)
        self._f_fund = pygame.font.SysFont("Georgia", 22, italic=True)

        reproducir_musica(RUTA_MUSICA_JUEGO)

    #--Eventos

    def manejar_evento(self, evento: pygame.event.Event) -> None:
        # El diario tiene prioridad sobre el resto de eventos
        if self._diario.manejar_evento(evento):
            return
        # Abrir/cerrar con J
        if evento.type == pygame.KEYDOWN and evento.key == TECLA_DIARIO:
            self._diario.alternar()
            return
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_F5:
            self._guardar_rapido()
            return

        if self._dialogo.activo:
            resultado = self._dialogo.procesar_evento(evento)
            if resultado:
                self._resolver_decision(resultado)
            return

        if self._menu_curacion.activo:
            self._menu_curacion.manejar_evento(evento, self._inventario, self._jugador, self._hud)
            return

        if self._fase == _FASE_INTRO:
            if evento.type == pygame.KEYDOWN and evento.key in (pygame.K_SPACE, pygame.K_RETURN):
                self._pagina_intro += 1
                if self._pagina_intro >= len(_INTRO_CAP1):
                    self._fase = _FASE_EXPLO
                    self._hud.mostrar_mensaje(
                        "A / D  mover      E  hablar      Q  usar planta")

        elif self._fase == _FASE_EXPLO:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_e:
                    self._intentar_interaccion()
                elif evento.key == pygame.K_q:
                    self._usar_planta()

        elif self._fase == _FASE_COMBATE:
            if evento.type == pygame.KEYDOWN and evento.key in (pygame.K_SPACE, pygame.K_z):
                self._lanzar_boleadora()

    #--Actualización

    def actualizar(self, dt: float) -> None:
        self._hud.actualizar(dt)
        self._diario.actualizar(dt)
        if self._menu_curacion.activo:
            return

        if self._fase == _FASE_DECISION:
            self._timer_cruz_cine += dt
            if self._timer_cruz_cine >= 0.65: ##
                self._timer_cruz_cine = 0.0
                self._cuadro_cruz_cine = (self._cuadro_cruz_cine + 1) % FRAMES_SPRITESHEET_4

        if self._fase == _FASE_EXPLO:
            teclas = pygame.key.get_pressed()
            self._jugador.procesar_entrada(teclas)
            self._jugador.actualizar(dt)
            self._camara.actualizar(self._jugador.x)
            self._llancay.actualizar(dt)
            self._cruz.actualizar(dt, self._jugador.x)
            for planta in self._plantas_mundo:
                planta.actualizar(dt)
            self._recoger_plantas()

            if (not self._llancay_hablo
                    and self._llancay.cerca_de(self._jugador.rect)):
                self._iniciar_dialogo_llancay()

            #Aparecen dialogos al acercarse a Cruz por primera vez
            if (not self._cruz_dialogo_disparado
                    and self._cruz.cerca_de(self._jugador.rect, dist=140)):
                self._iniciar_dialogo_cruz_previo()

        elif self._fase in (_FASE_DLG_LL, _FASE_DLG_CRUZ_PREV, _FASE_DECISION):
            self._dialogo.actualizar(dt)
            self._llancay.actualizar(dt)
            self._cruz.actualizar(dt, self._jugador.x)

        elif self._fase == _FASE_COMBATE:
            self._actualizar_combate(dt)

        elif self._fase == _FASE_TRANS:
            self._timer_trans -= dt
            if self._timer_trans <= 0:
                self._guardar_y_avanzar()

    def _actualizar_combate(self, dt: float) -> None:
        teclas = pygame.key.get_pressed()
        self._jugador.procesar_entrada(teclas)
        self._jugador.actualizar(dt)
        self._camara.actualizar(self._jugador.x)
        self._cruz.actualizar(dt, self._jugador.x)

        if self._cooldown_lanzamiento > 0:
            self._cooldown_lanzamiento -= dt


        for soldado in self._soldados:
            contacto = soldado.actualizar(dt, self._jugador.x)
            if contacto and soldado.estado == "avanzando":
                # Golpea a quien esté más cerca del soldado
                dist_chicha = abs(soldado.x_mundo - self._jugador.x)
                dist_cruz   = abs(soldado.x_mundo - self._cruz.x_mundo) if not self._cruz.atado else 9999

                if dist_cruz < dist_chicha and self._cruz.vivo:
                    self._cruz.recibir_danio(DAÑO_SOLDADO_A_CRUZ)
                    soldado.recibir_impacto()
                    self._hud.mostrar_mensaje(f"¡Cruz recibió un golpe! -{DAÑO_SOLDADO_A_CRUZ} vida")
                else:
                    self._jugador.recibir_danio(DANIO_SOLDADO)
                    soldado.recibir_impacto()
                    self._hud.mostrar_mensaje(f"¡Recibiste un golpe! -{DANIO_SOLDADO} vida")

        for boleadora in self._boleadoras:
            boleadora.actualizar(dt)
            if boleadora.activo:
                for soldado in self._soldados:
                    if (soldado.estado == "avanzando"
                            and boleadora.rect.colliderect(soldado.rect)):
                        soldado.recibir_impacto()
                        boleadora.activo = False
                        self._hud.mostrar_mensaje("¡Soldado derribado!")
                        break

        self._boleadoras = [b for b in self._boleadoras if b.activo]

        if not self._combate_resuelto and all(s.estado == "caido" for s in self._soldados):
            self._combate_resuelto = True
            self._hud.mostrar_mensaje("El camino está libre. Podes seguir...")
            self._fase = _FASE_TRANS
            self._timer_trans = 3.0

    #--Dibujo

    def dibujar(self, pantalla: pygame.Surface) -> None:
        # Dibujar las extensiones del fondo desplazadas por la cámara
        ANCHO_TRAMO = ANCHO_MUNDO // len(self._fondos_pampa)
        for i, fondo in enumerate(self._fondos_pampa):
            x_mundo = i * ANCHO_TRAMO
            x_pantalla = self._camara.aplicar_x(x_mundo)
            # Solo blittear si está visible en pantalla
            if -ANCHO_TRAMO <= x_pantalla <= ANCHO_PANTALLA:
                pantalla.blit(fondo, (x_pantalla, 0))

        if self._fase == _FASE_INTRO:
            _dibujar_intro_textual(pantalla, self.TITULO, _INTRO_CAP1,
                                   self._pagina_intro, self._f_tit, self._f_ital, self._f_ctrl)
            return

        for planta in self._plantas_mundo:
            planta.dibujar(pantalla, self._camara)

        self._llancay.dibujar(pantalla, self._camara)
        self._cruz.dibujar(pantalla, self._camara)

        for soldado in self._soldados:
            soldado.dibujar(pantalla, self._camara)
        for boleadora in self._boleadoras:
            boleadora.dibujar(pantalla, self._camara)

        self._jugador.dibujar(pantalla, self._camara)
        self._hud.dibujar(pantalla, self._jugador.salud, self._jugador.honor, self._inventario)

        # Mini-cinematica de Cruz en primer plano durante la decision
        if self._fase == _FASE_DECISION:
            self._dibujar_cinematica_cruz(pantalla)

        if self._dialogo.activo:
            self._dialogo.dibujar(pantalla)

        self._menu_curacion.dibujar(pantalla, self._inventario, self._jugador)

        if self._fase == _FASE_COMBATE:
            self._dibujar_aviso_combate(pantalla)

        if self._fase == _FASE_TRANS:
            texto_fundido = ("El camino esta libre" if self._combate_resuelto
                             else "La decision esta tomada...")
            _dibujar_fundido(pantalla, self._timer_trans, 3.0, texto_fundido, self._f_fund)
        # El diario se dibuja encima de todo excepto la etiqueta
        self._diario.dibujar(pantalla)
        _dibujar_etiqueta_capitulo(pantalla, self._f_etq, self.TITULO, self.REGION)
        _dibujar_etiqueta_capitulo(pantalla, self._f_etq, self.TITULO, self.REGION)

    def _dibujar_cinematica_cruz(self, pantalla: pygame.Surface) -> None:
        alto_panel = ALTO_PANTALLA - SistemaDialogo.ALTO_CAJA - SistemaDialogo.MARGEN_INF - 10
        panel = pygame.Surface((ANCHO_PANTALLA, alto_panel), pygame.SRCALPHA)
        panel.fill((0, 0, 0, 150))
        pantalla.blit(panel, (0, 0))

        frame = self._hoja_cruz_cine.obtener_frame(self._cuadro_cruz_cine)
        x_img = ANCHO_PANTALLA // 2 - frame.get_width() // 2
        y_img = (alto_panel - frame.get_height()) // 2
        pantalla.blit(frame, (x_img, y_img))

    def _dibujar_aviso_combate(self, pantalla: pygame.Surface) -> None:
        fuente = pygame.font.SysFont("Arial", 14)
        aviso  = fuente.render("[Espacio] Lanzar boleadora", True, COLOR_HONOR_ORO)
        pantalla.blit(aviso, (ANCHO_PANTALLA // 2 - aviso.get_width() // 2, 70))

    #--Lógica plantas

    def _recoger_plantas(self) -> None:
        for planta in self._plantas_mundo:
            if planta.puede_recoger(self._jugador.rect):
                self._inventario.agregar(planta.datos)
                planta.recogida = True
                self._diario.descubrir_planta(planta.nombre)
                self._hud.mostrar_mensaje(f"Recogiste: {planta.nombre}   (Q) para curar")

    def _usar_planta(self) -> None:
        if len(self._inventario) == 0:
            self._hud.mostrar_mensaje("No tenes plantas en el inventario.")
            return
        if self._jugador.salud >= SALUD_MAXIMA:
            self._hud.mostrar_mensaje("Vida al máximo.")
            return
        self._menu_curacion.abrir()

    #--Interaccion con NPC

    def _intentar_interaccion(self) -> None:
        if self._llancay.activo and self._llancay.cerca_de(self._jugador.rect):
            if not self._llancay_hablo:
                self._iniciar_dialogo_llancay()
            return
        if self._cruz.activo and self._cruz.cerca_de(self._jugador.rect):
            if self._cruz_dialogo_disparado and self._cruz.atado:
                self._iniciar_dialogo_decision()

    #--Dialogo con Llancay

    def _iniciar_dialogo_llancay(self) -> None:
        self._fase          = _FASE_DLG_LL
        self._llancay_hablo = True

        lineas = [
            LineaDialogo("Llancay",
                "Quieto, gaucho. Te va caer desde lejos. "
                "Esas heridas se infectan si no las atendÃ©s hoy."),
            LineaDialogo("Chicha", "¿Por qué me ayudas? No me conoces."),
            LineaDialogo("Llancay",
                "Dialogo bla bla bla. "
                "Dialogo bla bla bla."),
            LineaDialogo("Llancay",
                "bla bla bla"
                "bla bla bla"),
            LineaDialogo("Llancay", HISTORIA_RANQUEL),
            LineaDialogo("Chicha", "No sabía eso. Nunca nadie me contÃ³."),
            LineaDialogo("Llancay",
                "Ahora sabes. La historia que te enseÃ±aron tiene agujeros. "
                "Nosotros somos uno de esos agujeros."),
            LineaDialogo("Llancay",
                "Pero antes de la historia, atendamos tus heridas. "
                "Esta pampa tiene cuatro plantas que necesitas conocer."),
        ]
        for pl in PLANTAS_LLANCAY:
            lineas.append(LineaDialogo(
                "Llancay", f"{pl['nombre']} ({pl['nombre_cient']}): {pl['descripcion']}"))
            lineas.append(LineaDialogo(
                "Llancay",
                f"Propiedad: {pl['propiedad']}. Cura {pl['curacion']} puntos de vida. "
                f"Usala con [Q] cuando estás herido."))
        lineas += [
            LineaDialogo("Llancay",
                "Más adelante hay un hombre encadenado a un poste. "
                "Vas a tener que decidir qué haces con eso."),
            LineaDialogo("Chicha", "Gracias, Llancay."),
            LineaDialogo("Llancay", "Cuidate, gaucho. Y recordá lo que te conté."),
        ]

        def al_cerrar():
            for pl in PLANTAS_LLANCAY:
                self._inventario.agregar(pl)
                if pl["nombre"] not in self.gestor.partida["plantas_conocidas"]:
                    self.gestor.partida["plantas_conocidas"].append(pl["nombre"])
                self._diario.descubrir_planta(pl["nombre"])
            self._diario.desbloquear_reflexion("llancay_ranquel")
            self._hud.mostrar_mensaje(
                "Llancay te entregó 4 plantas  [Q] curar")
            self._fase = _FASE_EXPLO

        self._dialogo.iniciar(lineas, callback_cerrar=al_cerrar)

    #--Dialogo automatico al acercarse a Cruz

    def _iniciar_dialogo_cruz_previo(self) -> None:
        self._fase = _FASE_DLG_CRUZ_PREV
        self._cruz_dialogo_disparado = True

        lineas = [
            LineaDialogo("Chicha",
                "Hay un hombre atado a ese poste. Parece que lleva días así."),
            LineaDialogo("Cruz",
                "¡Eh, vos! ¿Tenes un cuchillo? Estos nudos me están matando."),
            LineaDialogo("Chicha", "¿Quién te hizo esto?"),
            LineaDialogo("Cruz",
                "El Coronel Ibañez, el mismo que seguro te persigue a vos. "
                "Me dejaron aca de escarmiento."),
            LineaDialogo("Cruz",
                "Si me soltas, te juro que te sigo hasta el fin del mundo. "
                "Dos espadas valen más que una, gaucho."),
            LineaDialogo("Chicha",
                "Tengo que pensarlo..."),
        ]

        def al_cerrar():
            self._fase = _FASE_EXPLO
            self._hud.mostrar_mensaje("E para decidir sobre Cruz")

        self._dialogo.iniciar(lineas, callback_cerrar=al_cerrar)

    #--Decision final Cruz

    def _iniciar_dialogo_decision(self) -> None:
        self._fase = _FASE_DECISION
        reproducir_musica(RUTA_MUSICA_DECISION)

        lineas = [
            LineaDialogo("Cruz",
                "Y bien, gaucho.¿Me vas a soltar o me vas a dejar acá pudrirme?"),
            LineaDialogo("Chicha",
                "Un gaucho no abandona a un paisano. "
                "Pero cargar con alguien puede costarme el viaje"),
        ]
        opciones = [
            Opcion("Liberar a Cruz.",
                   efecto_honor=+15, resultado="liberar_cruz"),
            Opcion("Seguir solo.",
                   efecto_honor=-10, resultado="dejar_cruz"),
        ]
        self._dialogo.iniciar(lineas, opciones)

    def _resolver_decision(self, opcion: Opcion) -> None:
        self.gestor.sumar_honor(opcion.efecto_honor)
        self._jugador.honor = self.gestor.partida["honor"]

        if opcion.resultado == "liberar_cruz":
            self.gestor.partida["cruz_aliado"] = True
            self.gestor.partida["decisiones"]["libero_cruz"] = True
            self._cruz.liberar()
            self._diario.desbloquear_reflexion("reflexion_cruz")
            self._hud.mostrar_mensaje("Cruz se une al viaje.  +15 Honor")
            self._iniciar_combate()
        else:
            self.gestor.partida["cruz_aliado"] = False
            self.gestor.partida["decisiones"]["libero_cruz"] = False
            self._hud.mostrar_mensaje("Seguirás solo hacia el sur.  -10 Honor")
            self._fase = _FASE_TRANS
            self._timer_trans = 3.0

    # -- Sistema de combate

    def _iniciar_combate(self) -> None:
        #Después de liberar a Cruz.
        #activa el spritesheet de combate de Chicha.

        self._fase            = _FASE_COMBATE
        self._combate_resuelto   = False
        reproducir_musica(RUTA_MUSICA_COMBATE)

        # Tres soldados aparecen adelante de la posición de Chicha
        base_x = self._jugador.x + 350
        self._soldados = [
            Soldado(base_x),
            Soldado(base_x + 180),
            Soldado(base_x + 360),
        ]
        self._hud.mostrar_mensaje("¡Soldados a la vista! (Espacio) para lanzar boleadoras")

    def _lanzar_boleadora(self) -> None:
        if self._cooldown_lanzamiento > 0:
            return
        direccion = 1 if self._jugador.mirando_der else -1
        x_inicio  = self._jugador.x + (ANCHO_VIS_PERSONAJE if direccion > 0 else 0)
        self._boleadoras.append(Boleadora(x_inicio, direccion))
        self._cooldown_lanzamiento = COOLDOWN_LANZAMIENTO
        self._jugador.iniciar_animacion_ataque()

    #Guardado

    def _sincronizar_partida(self) -> None:
        self.gestor.partida["salud"]      = self._jugador.salud
        self.gestor.partida["honor"]      = self._jugador.honor
        self.gestor.partida["inventario"] = self._inventario.a_lista()

    def _guardar_y_avanzar(self) -> None:
        self._sincronizar_partida()
        self.gestor.cambiar("fin_demo")

    def _guardar_rapido(self) -> None:
        self._sincronizar_partida()
        guardar_partida(self.gestor.partida, self.NOMBRE, self._jugador.x)
        self._hud.mostrar_mensaje("Partida guardada  [F5]")


# Sección 23 fin demo

class FinDemo(EscenaBase):
  #Pantalla dividida
  #Izquierda: Chicha spritesheet
  #Derecha: texto con titulo "Fin de la Demo", plantas recolectadas y decisiones.
  #Tecla Espacio,Enter,Escape para volver al menú principal.


    ESCALA_ESCENA_FINAL = 0.65 ##  # Más grande que en combate
    ANCHO_CHICHA_FINAL  = int(ANCHO_CUADRO_PERSONAJE * ESCALA_ESCENA_FINAL)
    ALTO_CHICHA_FINAL   = int(ALTO_CUADRO_PERSONAJE  * ESCALA_ESCENA_FINAL)

    # Volver al menú
    RECT_BOTON_VOLVER = pygame.Rect(ANCHO_PANTALLA - 230, ALTO_PANTALLA - 60, 200, 44)

    def __init__(self, gestor: GestorEscenas):
        super().__init__(gestor)

        self._fondo = cargar_imagen(RUTA_FONDO_ATARDECER, (ANCHO_PANTALLA, ALTO_PANTALLA))
        self._hoja_sentado = HojaSprites(RUTA_CHICHA_SENTADO,
                                         ANCHO_CUADRO_CHICHA_FINAL,
                                         ALTO_CUADRO_CHICHA_FINAL,
                                         self.ESCALA_ESCENA_FINAL)
        self._cuadro      = 0
        self._timer_anim  = 0.0
        self._vel_anim    = 1.25 ##  #Animacion lenta

        self._honor   = gestor.partida["honor"]
        self._salud   = gestor.partida["salud"]
        self._plantas = gestor.partida["plantas_conocidas"]
        self._decisiones = gestor.partida["decisiones"]

        self._f_titulo = pygame.font.SysFont("Georgia", 34, bold=True)
        self._f_stat   = pygame.font.SysFont("Arial",   17)
        self._f_sub    = pygame.font.SysFont("Arial",   15)
        self._f_ctrl   = pygame.font.SysFont("Arial",   13)

        reproducir_musica(RUTA_MUSICA_FINAL_HONOR_ALTO)

    def manejar_evento(self, evento: pygame.event.Event) -> None:
        if evento.type == pygame.KEYDOWN:
            if evento.key in (pygame.K_RETURN, pygame.K_SPACE, pygame.K_ESCAPE):
                self.gestor.cambiar("menu")
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if self.RECT_BOTON_VOLVER.collidepoint(evento.pos):
                self.gestor.cambiar("menu")

    def actualizar(self, dt: float) -> None:
        self._timer_anim += dt
        if self._timer_anim >= self._vel_anim:
            self._timer_anim = 0.0
            self._cuadro = (self._cuadro + 1) % 4   # Bucle de respiracion y poncho

    def dibujar(self, pantalla: pygame.Surface) -> None:
        pantalla.blit(self._fondo, (0, 0))

        #Mitad izquierda: Chicha sentado mirando el atardecer
        frame = self._hoja_sentado.obtener_frame(self._cuadro)
        x_chicha = ANCHO_PANTALLA // 4 - frame.get_width() // 2
        y_chicha = SUELO - frame.get_height()
        pantalla.blit(frame, (x_chicha, y_chicha))

        #Mitad derecha: panel de estadi­sticas
        panel_x = ANCHO_PANTALLA // 2 + 20
        panel_w = ANCHO_PANTALLA // 2 - 60
        panel = pygame.Rect(panel_x, 60, panel_w, ALTO_PANTALLA - 140)
        dibujar_caja(pantalla, panel, (10, 6, 2, 210), COLOR_TIERRA_BORDE, 2, 10)

        tit = self._f_titulo.render("Fin de la Demo", True, COLOR_HONOR_ORO)
        pantalla.blit(tit, (panel.x + 24, panel.y + 22))

        y_actual = panel.y + 80

        # Estadi­sticas generales
        for txt in [
            f"Honor acumulado:   {self._honor} / {HONOR_MAXIMO}",
            f"Vida al terminar:  {self._salud} / {SALUD_MAXIMA}",
        ]:
            pantalla.blit(self._f_stat.render(txt, True, COLOR_BLANCO), (panel.x + 24, y_actual))
            y_actual += 28

        y_actual += 10
        pygame.draw.line(pantalla, COLOR_TIERRA_BORDE,
                         (panel.x + 24, y_actual), (panel.right - 24, y_actual), 1)
        y_actual += 20

        # Plantas medicinales recolectadas
        pantalla.blit(self._f_stat.render("Plantas medicinales:", True, COLOR_HONOR_ORO),
                      (panel.x + 24, y_actual))
        y_actual += 26
        if self._plantas:
            for nombre_planta in self._plantas:
                pantalla.blit(self._f_sub.render(f"{nombre_planta}", True, (180, 220, 160)),
                              (panel.x + 36, y_actual))
                y_actual += 22
        else:
            pantalla.blit(self._f_sub.render("Ninguna planta recolectada.", True, (170, 150, 150)),
                          (panel.x + 36, y_actual))
            y_actual += 22

        y_actual += 14
        pygame.draw.line(pantalla, COLOR_TIERRA_BORDE,
                         (panel.x + 24, y_actual), (panel.right - 24, y_actual), 1)
        y_actual += 20

        # Decisiones tomadas
        pantalla.blit(self._f_stat.render("Decisiones tomadas:", True, COLOR_HONOR_ORO),
                      (panel.x + 24, y_actual))
        y_actual += 26
        if self._decisiones:
            for clave, valor in self._decisiones.items():
                etiqueta = clave.replace("_", " ").capitalize()
                resultado = "Sí" if valor else "No"
                pantalla.blit(
                    self._f_sub.render(f"{etiqueta}: {resultado}", True, (220, 200, 180)),
                    (panel.x + 36, y_actual))
                y_actual += 22
        else:
            pantalla.blit(self._f_sub.render("Sin decisiones registradas.", True, (170, 150, 150)),
                          (panel.x + 36, y_actual))
            y_actual += 22

        # Pista / boton para volver
        ctrl = self._f_ctrl.render("(Espacio / Enter / Clic)  volver al menu principal",
                                   True, (170, 160, 145))
        pantalla.blit(ctrl, (panel.x + 24, panel.bottom - 30))



#Seccion 24 principal

def main():
    pygame.init()
    pygame.mixer.init()

    pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
    pygame.display.set_caption("Los Hijos de Nadie: Capí­tulo 1")
    reloj = pygame.time.Clock()

    gestor = GestorEscenas(pantalla)
    gestor.registrar("menu",       MenuPrincipal)
    gestor.registrar("cinematica", EscenaCinematica)
    gestor.registrar("capitulo_1", CapituloPampa)
    gestor.registrar("fin_demo",   FinDemo)
    gestor.cambiar("menu")

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # F9
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_F9:
                datos = cargar_partida()
                if datos:
                    gestor.aplicar_guardado(datos)
                    gestor.cambiar("capitulo_1", jugador_x=datos.get("jugador_x", 200.0))
                continue

            gestor.escena_actual.manejar_evento(evento)

        dt = reloj.tick(FPS) / 1000.0
        gestor.escena_actual.actualizar(dt)
        gestor.escena_actual.dibujar(pantalla)
        pygame.display.flip()


if __name__ == "__main__":
    main()