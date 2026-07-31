import pygame
import os
import math


from los_hijos_de_nadie import (
    ANCHO_PANTALLA, ALTO_PANTALLA, FPS, SUELO, ANCHO_MUNDO, MARGEN_CAM_X,
    ANCHO_CUADRO_PERSONAJE, ALTO_CUADRO_PERSONAJE, ANCHO_VIS_PERSONAJE,
    ALTO_VIS_PERSONAJE, ESCALA_GAMEPLAY, FRAMES_SPRITESHEET_4,
    SALUD_MAXIMA, HONOR_MAXIMO, UMBRAL_HONOR_ALTO, VELOCIDAD_NORMAL,
    VELOCIDAD_HERIDO, UMBRAL_VIDA_HERIDO,
    VELOCIDAD_BOLEADORA, VELOCIDAD_SOLDADO, DANIO_BOLEADORA,
    DISTANCIA_ATAQUE_SOLDADO, DANIO_SOLDADO, COOLDOWN_LANZAMIENTO,
    SALUD_CRUZ_MAXIMA, SELUD_CRUZ_INICIAL, DISTANCIA_SEGUIR,
    VELOCIDAD_CRUZ, DAÑO_SOLDADO_A_CRUZ,
    COLOR_BLANCO, COLOR_NEGRO, COLOR_TIERRA, COLOR_TIERRA_BORDE,
    COLOR_VERDE_VIDA, COLOR_ROJO_DANIO, COLOR_HONOR_ORO,
    COLOR_CAJA_DLG, COLOR_OVERLAY_INTRO, COLOR_LLAVE,
    cargar_imagen, reproducir_musica, dibujar_texto_envuelto,
    dibujar_caja, _quitar_fondo_solido, guardar_partida, ARCHIVO_GUARDADO,
    GestorEscenas, EscenaBase, HojaSprites, Camara, Jugador, Cruz,
    Soldado, Boleadora, Inventario, SistemaDialogo, LineaDialogo, Opcion,
    HUD, MenuCuracion, Diario,
    _dibujar_intro_textual, _dibujar_fundido, _dibujar_etiqueta_capitulo,
    RUTA_CHICHA_NORMAL, RUTA_CHICHA_RENGUEANDO, RUTA_CHICHA_COMBATE,
    RUTA_CHICHA_CURACION, RUTA_SOLDADO_AVANCE, RUTA_SOLDADO_CAIDO,
    RUTA_BOLEADORA, RUTA_MUSICA_COMBATE, RUTA_MUSICA_DECISION,
    RUTA_CRUZ_LIBRE, RUTA_CRUZ_ATADO,
    ANCHO_CUADRO_CURACION, ALTO_CUADRO_CURACION,
    TECLA_DIARIO,
)


RUTA_FONDO_SIERRAS_1  = r"" 
RUTA_FONDO_SIERRAS_2  = r""


RUTA_TORO_GRANDE_IMG  = r"" 
RUTA_TORO_GRANDE_SS   = r""

#Sargento
RUTA_QUIROGA_AVANCE   = r""

#Plantas medicinales
RUTA_TOLA_SERRANA_IMG = r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Objetos\Tola_Serrana.png"   # ← PON TU RUTA AQUÍ  (ej: Tola_Serrana.png)

#Música
RUTA_MUSICA_SIERRAS   = r"" 
RUTA_MUSICA_ESPÍA     = r"" 

#Fondo final del Cap.2 (pantalla de transición al Cap.3)
RUTA_FONDO_TRANS_C2   = r""


POS_TORO_GRANDE    = 900 
POS_ESPÍA          = 2100 
POS_QUIROGA        = 2800
POS_PLANTA_TOLA    = 600


ESCALA_TORO        = 0.15
ANCHO_VIS_TORO     = int(1024 * ESCALA_TORO)   #154 px
ALTO_VIS_TORO      = int(1024 * ESCALA_TORO)   #154 px
ESCALA_QUIROGA     = ESCALA_GAMEPLAY   # igual que el resto de personajes


VELOCIDAD_QUIROGA  = 1.8
SALUD_QUIROGA_MAX  = 3   # 3 impactos de boleadora para derribarlo
DISTANCIA_MUSICA_ESPIA = 400
DEMORA_QUIROGA     = 3.0   # segundos

#Planta medicinal del Cap.2
DATOS_TOLA_SERRANA = {
    "nombre":       "Tola Serrana",
    "nombre_cient": "Parastrephia lepidophylla",
    "propiedad":    "Alivia el cansancio y el dolor de cabeza",
    "descripcion":  (
        "La tola serrana crece entre las rocas de las sierras. "
        "Los querandíes la usaban para recuperar fuerzas en largas caminatas. "
        "Se prepara como infusión y alivia el cansancio en pocas horas."
    ),
    "curacion":     35,
}

PLANTAS_SIERRAS = [DATOS_TOLA_SERRANA]

DIALOGO_HISTORIA_QUERANDÍ = (
    "Mi pueblo, los querandíes, dominó estas tierras mucho antes de "
    "que llegaran los españoles. Resistimos sus ataques durante años. "
    "Nos llamaban guerreros. Después... nos borraron de los libros. "
    "Pero la sierra recuerda."
)

REFLEXION_TORO_GRANDE = {
    "clave":  "toro_querandí",
    "titulo": "Sobre Toro Grande y los querandíes",
    "texto":  (
        "Toro Grande me habló de su pueblo como si lo hubieran borrado de un plumazo. "
        "Los querandíes resistieron a los españoles más de lo que nos contaron en la escuela. "
        "Y después los borraron de los libros. "
        "Me pregunto cuántos pueblos más corrieron la misma suerte."
    ),
}

PAGINAS_INTRO_CAP2 = [
    "Sierras Bonaerenses, 1870.",
    "Tras escapar de la pampa,\nChicha llega a las sierras buscando\nun caballo y una ruta segura al sur.",
    "El pueblo de Tres Lagunas parece tranquilo.\nPero el Coronel tiene ojos en todos lados.",
    "Un hombre que no conoce\npuede ser un aliado... o una trampa.",
]

_FASE_INTRO_C2      = "intro"
_FASE_EXPLORA_C2    = "exploracion"
_FASE_DLG_TORO      = "dialogo_toro_grande"
_FASE_CERCA_ESPÍA   = "cerca_espía"
_FASE_DECISION_ESPÍA= "decision_espía"
_FASE_COMBATE_C2    = "combate_quiroga"
_FASE_TRANS_C2      = "transicion"

class PlantaMundoC2:

    RADIO = 13

    def __init__(self, datos: dict, x_mundo: float,
                 ruta_imagen: str = ""):
        self.datos    = datos
        self.nombre   = datos["nombre"]
        self.recogida = False
        self._x       = float(x_mundo)
        self._tick    = 0
        self._fuente  = pygame.font.SysFont("Arial", 11)

        self._imagen = None
        if ruta_imagen and os.path.exists(ruta_imagen):
            img = pygame.image.load(ruta_imagen).convert_alpha()
            self._imagen = pygame.transform.scale(img, (32, 32))

        self.rect = pygame.Rect(
            int(x_mundo) - self.RADIO,
            SUELO - self.RADIO * 2 - 4,
            self.RADIO * 2,
            self.RADIO * 2,
        )

    def actualizar(self, dt: float) -> None:
        self._tick += 1

    def puede_recoger(self, rect_jugador: pygame.Rect) -> bool:
        return not self.recogida and self.rect.colliderect(
            rect_jugador.inflate(55, 55))

    def dibujar(self, pantalla: pygame.Surface, camara: Camara) -> None:
        if self.recogida:
            return
        radio = self.RADIO + int(math.sin(self._tick * 0.08) * 2)
        cx    = camara.aplicar_x(int(self._x))
        cy    = SUELO - self.RADIO * 2 - 4

        if self._imagen:
            x_img = cx - 16
            y_img = cy - 16
            pantalla.blit(self._imagen, (x_img, y_img))
        else:
            color_planta = (60, 160, 120)
            for r, a in [(radio + 7, 30), (radio + 3, 70)]:
                halo = pygame.Surface((r * 2, r * 2), pygame.SRCALPHA)
                pygame.draw.circle(halo, (*color_planta, a), (r, r), r)
                pantalla.blit(halo, (cx - r, cy - r))
            pygame.draw.circle(pantalla, color_planta,  (cx, cy), radio)
            pygame.draw.circle(pantalla, COLOR_BLANCO,  (cx, cy), radio, 2)
            ltr = self._fuente.render(self.nombre[0], True, COLOR_BLANCO)
            pantalla.blit(ltr, (cx - ltr.get_width() // 2,
                                cy - ltr.get_height() // 2))

        # Etiqueta flotante
        etq = self._fuente.render(self.nombre, True, COLOR_BLANCO)
        pantalla.blit(etq, (cx - etq.get_width() // 2, cy - radio - 15))


class ToroGrande:

    ANCHO_CAJA = int(ANCHO_VIS_TORO * 0.5)
    ALTO_CAJA  = ALTO_VIS_TORO

    def __init__(self, x_mundo: float):
        self.x_mundo  = float(x_mundo)
        self.nombre   = "Toro Grande"
        self.activo   = True
        self._tick    = 0
        self._desplaz = 0
        self._fuente  = pygame.font.SysFont("Arial", 13)

        self._imagen_estatica = None
        self._hoja_ss= None
        self._cuadro_ss = 0
        self._timer_ss        = 0.0

        if RUTA_TORO_GRANDE_IMG and os.path.exists(RUTA_TORO_GRANDE_IMG):

            self._imagen_estatica = cargar_imagen(
                RUTA_TORO_GRANDE_IMG, (ANCHO_VIS_TORO, ALTO_VIS_TORO))
        elif RUTA_TORO_GRANDE_SS and os.path.exists(RUTA_TORO_GRANDE_SS):

            self._hoja_ss = HojaSprites(
                RUTA_TORO_GRANDE_SS,
                ANCHO_CUADRO_PERSONAJE,
                ALTO_CUADRO_PERSONAJE,
                ESCALA_GAMEPLAY,
            )
        else:
            self._imagen_estatica = cargar_imagen("", (ANCHO_VIS_TORO, ALTO_VIS_TORO))

        self.rect = pygame.Rect(
            int(self.x_mundo) + (ANCHO_VIS_TORO - self.ANCHO_CAJA) // 2,
            SUELO - self.ALTO_CAJA,
            self.ANCHO_CAJA,
            self.ALTO_CAJA,
        )

    def actualizar(self, dt: float) -> None:
        self._tick    += 1
        self._desplaz  = int(math.sin(self._tick * 0.04) * 1.5)

        if self._hoja_ss is not None:
            self._timer_ss += dt
            if self._timer_ss >= 0.65:
                self._timer_ss  = 0.0
                self._cuadro_ss = (self._cuadro_ss + 1) % FRAMES_SPRITESHEET_4

    def cerca_de(self, rect_jugador: pygame.Rect, dist: int = 110) -> bool:
        return self.rect.colliderect(rect_jugador.inflate(dist, dist))

    def dibujar(self, pantalla: pygame.Surface, camara: Camara) -> None:
        if not self.activo:
            return

        x_pan = camara.aplicar_x(self.x_mundo)
        y_pan = SUELO - ALTO_VIS_TORO + self._desplaz

        if self._imagen_estatica is not None:
            pantalla.blit(self._imagen_estatica, (x_pan, y_pan))
        elif self._hoja_ss is not None:
            frame = self._hoja_ss.obtener_frame(self._cuadro_ss)
            x_pan += (ANCHO_VIS_PERSONAJE - frame.get_width()) // 2
            pantalla.blit(frame, (x_pan, y_pan))

        etq   = self._fuente.render(f"▼ {self.nombre}", True, COLOR_BLANCO)
        ex    = x_pan + ANCHO_VIS_TORO // 2 - etq.get_width() // 2
        ey    = y_pan - 18
        fondo = pygame.Surface((etq.get_width() + 8, etq.get_height() + 4),
                               pygame.SRCALPHA)
        fondo.fill((0, 0, 0, 145))
        pantalla.blit(fondo, (ex - 4, ey - 2))
        pantalla.blit(etq,   (ex, ey))


class EspiaCoronel:

    ANCHO_CAJA = int(ANCHO_VIS_PERSONAJE * 0.55)
    ALTO_CAJA  = ALTO_VIS_PERSONAJE

    def __init__(self, x_mundo: float):
        self.x_mundo       = float(x_mundo)
        self.nombre        = "Hombre sospechoso"
        self.activo        = True
        self.descubierto   = False
        self._tick         = 0
        self._cuadro       = 0
        self._timer_anim   = 0.0
        self._fuente       = pygame.font.SysFont("Arial", 13)

        self._hoja = HojaSprites(
            RUTA_SOLDADO_AVANCE,
            ANCHO_CUADRO_PERSONAJE,
            ALTO_CUADRO_PERSONAJE,
            ESCALA_GAMEPLAY,
        )

        self.rect = pygame.Rect(
            int(self.x_mundo) + (ANCHO_VIS_PERSONAJE - self.ANCHO_CAJA) // 2,
            SUELO - self.ALTO_CAJA,
            self.ANCHO_CAJA,
            self.ALTO_CAJA,
        )

    def actualizar(self, dt: float) -> None:
        self._tick += 1
        self._timer_anim += dt
        if self._timer_anim >= 1.2:
            self._timer_anim = 0.0
            self._cuadro     = (self._cuadro + 1) % FRAMES_SPRITESHEET_4

    def cerca_de(self, rect_jugador: pygame.Rect, dist: int = 150) -> bool:
        return self.rect.colliderect(rect_jugador.inflate(dist, dist))

    def dibujar(self, pantalla: pygame.Surface, camara: Camara) -> None:
        if not self.activo:
            return

        x_pan = camara.aplicar_x(self.x_mundo)
        frame = self._hoja.obtener_frame(self._cuadro)
        frame = pygame.transform.flip(frame, True, False)

        x_pan += (ANCHO_VIS_PERSONAJE - frame.get_width()) // 2
        y_pan  = SUELO - frame.get_height()
        pantalla.blit(frame, (x_pan, y_pan))

        color_etq = COLOR_ROJO_DANIO if self.descubierto else (200, 200, 80)
        nombre_vis = "Espía del Coronel" if self.descubierto else self.nombre
        etq   = self._fuente.render(f"▼ {nombre_vis}", True, color_etq)
        ex    = x_pan + ANCHO_VIS_PERSONAJE // 2 - etq.get_width() // 2
        ey    = y_pan - 18
        fondo = pygame.Surface((etq.get_width() + 8, etq.get_height() + 4),
                               pygame.SRCALPHA)
        fondo.fill((0, 0, 0, 145))
        pantalla.blit(fondo, (ex - 4, ey - 2))
        pantalla.blit(etq,   (ex, ey))


class SargentoQuiroga:


    ANCHO_CAJA = int(ANCHO_VIS_PERSONAJE * 0.55)
    ALTO_CAJA  = ALTO_VIS_PERSONAJE

    def __init__(self, x_mundo: float):
        self.x_mundo    = float(x_mundo)
        self.nombre     = "Sgto. Quiroga"
        self.activo     = True
        self.caido      = False
        self.salud      = SALUD_QUIROGA_MAX
        self._cuadro    = 0
        self._timer_anim= 0.0
        self._vel_anim  = 0.18
        self._fuente    = pygame.font.SysFont("Arial", 13)
        self._fuente_vida = pygame.font.SysFont("Arial", 11)

        ruta = RUTA_QUIROGA_AVANCE if RUTA_QUIROGA_AVANCE and os.path.exists(RUTA_QUIROGA_AVANCE) \
               else RUTA_SOLDADO_AVANCE
        self._hoja_avance = HojaSprites(
            ruta,
            ANCHO_CUADRO_PERSONAJE,
            ALTO_CUADRO_PERSONAJE,
            ESCALA_GAMEPLAY,
        )
        self._hoja_caido = HojaSprites(
            RUTA_SOLDADO_CAIDO,
            ANCHO_CUADRO_PERSONAJE,
            ALTO_CUADRO_PERSONAJE,
            ESCALA_GAMEPLAY,
        )

        self.rect = pygame.Rect(
            int(self.x_mundo) + (ANCHO_VIS_PERSONAJE - self.ANCHO_CAJA) // 2,
            SUELO - self.ALTO_CAJA,
            self.ANCHO_CAJA,
            self.ALTO_CAJA,
        )

    def recibir_impacto(self) -> bool:
        if self.caido:
            return False
        self.salud -= 1
        if self.salud <= 0:
            self.caido = True
            return True
        return False

    def actualizar(self, dt: float, pos_jugador_x: float) -> None:
        if self.caido:
            return

        if self.x_mundo > pos_jugador_x + ANCHO_VIS_PERSONAJE:
            self.x_mundo -= VELOCIDAD_QUIROGA
            self.rect.x   = int(self.x_mundo) + (ANCHO_VIS_PERSONAJE - self.ANCHO_CAJA) // 2
            self.rect.bottom = SUELO

        self._timer_anim += dt
        if self._timer_anim >= self._vel_anim:
            self._timer_anim = 0.0
            self._cuadro     = (self._cuadro + 1) % FRAMES_SPRITESHEET_4

    def toca_al_jugador(self, rect_jugador: pygame.Rect) -> bool:
        return not self.caido and self.rect.colliderect(rect_jugador)

    def colisiona_con_boleadora(self, rect_bol: pygame.Rect) -> bool:
        return not self.caido and self.rect.colliderect(rect_bol)

    def dibujar(self, pantalla: pygame.Surface, camara: Camara) -> None:
        if not self.activo:
            return

        hoja  = self._hoja_caido if self.caido else self._hoja_avance
        frame = hoja.obtener_frame(self._cuadro)

        if not self.caido:
            frame = pygame.transform.flip(frame, True, False)

        x_pan = camara.aplicar_x(self.x_mundo)
        x_pan += (ANCHO_VIS_PERSONAJE - frame.get_width()) // 2
        y_pan  = SUELO - frame.get_height()
        pantalla.blit(frame, (x_pan, y_pan))

        etq   = self._fuente.render(f"▼ {self.nombre}", True, COLOR_ROJO_DANIO)
        ex    = x_pan + ANCHO_VIS_PERSONAJE // 2 - etq.get_width() // 2
        ey    = y_pan - 38
        fondo = pygame.Surface((etq.get_width() + 8, etq.get_height() + 4),
                               pygame.SRCALPHA)
        fondo.fill((0, 0, 0, 145))
        pantalla.blit(fondo, (ex - 4, ey - 2))
        pantalla.blit(etq,   (ex, ey))

        if not self.caido:
            self._dibujar_resistencia(pantalla, x_pan, y_pan)

    def _dibujar_resistencia(self, pantalla, x_pan, y_pan):
        RADIO_BOLITA = 6
        GAP          = 16
        total        = SALUD_QUIROGA_MAX
        xb = x_pan + ANCHO_VIS_PERSONAJE // 2 - (total * GAP) // 2
        yb = y_pan - 22
        for i in range(total):
            color = COLOR_ROJO_DANIO if i < self.salud else (60, 60, 60)
            pygame.draw.circle(pantalla, color, (xb + i * GAP, yb), RADIO_BOLITA)
            pygame.draw.circle(pantalla, COLOR_BLANCO, (xb + i * GAP, yb), RADIO_BOLITA, 1)



class CinematicaIntroduccionCap2:


    DUR_TOTAL     = 6.0
    VEL_PANORAMICA= 80.0

    def __init__(self, pantalla: pygame.Surface, fondo_sierras: pygame.Surface):
        self._pantalla      = pantalla
        self._fondo         = fondo_sierras
        self._timer         = 0.0
        self.terminada      = False
        self._scroll_x      = 0.0
        self._chicha_x      = -ANCHO_VIS_PERSONAJE
        self._cuadro        = 0
        self._timer_anim    = 0.0

        self._hoja_rengueo = HojaSprites(
            RUTA_CHICHA_RENGUEANDO,
            ANCHO_CUADRO_PERSONAJE,
            ALTO_CUADRO_PERSONAJE,
            ESCALA_GAMEPLAY,
        )

        self._f_titulo = pygame.font.SysFont("Georgia", 42, bold=True)
        self._f_subtit = pygame.font.SysFont("Georgia", 26, italic=True)

    def actualizar(self, dt: float) -> None:
        if self.terminada:
            return

        self._timer     += dt
        self._scroll_x  += self.VEL_PANORAMICA * dt
        self._chicha_x  += VELOCIDAD_HERIDO

        self._timer_anim += dt
        if self._timer_anim >= 0.15:
            self._timer_anim = 0.0
            self._cuadro     = (self._cuadro % 3) + 1

        if self._timer >= self.DUR_TOTAL:
            self.terminada = True

    def dibujar(self) -> None:
        scroll = min(int(self._scroll_x), ANCHO_MUNDO - ANCHO_PANTALLA)
        self._pantalla.blit(self._fondo, (-scroll, 0))

        frame   = self._hoja_rengueo.obtener_frame(self._cuadro)
        x_chicha = int(self._chicha_x)
        y_chicha = SUELO - frame.get_height()
        self._pantalla.blit(frame, (x_chicha, y_chicha))

        progreso = self._timer / self.DUR_TOTAL
        if progreso > 0.2:
            alpha = min(255, int(255 * (progreso - 0.2) / 0.3))
            t1 = self._f_titulo.render("Capítulo 2", True, COLOR_HONOR_ORO)
            t2 = self._f_subtit.render("Las Sierras Bonaerenses", True, COLOR_BLANCO)
            t1.set_alpha(alpha)
            t2.set_alpha(alpha)
            self._pantalla.blit(t1, (ANCHO_PANTALLA // 2 - t1.get_width() // 2,
                                     ALTO_PANTALLA  // 2 - 60))
            self._pantalla.blit(t2, (ANCHO_PANTALLA // 2 - t2.get_width() // 2,
                                     ALTO_PANTALLA  // 2 + 10))

        if progreso < 0.15:
            alpha_fondo = int(255 * (1.0 - progreso / 0.15))
            ov = pygame.Surface((ANCHO_PANTALLA, ALTO_PANTALLA))
            ov.set_alpha(alpha_fondo)
            ov.fill(COLOR_NEGRO)
            self._pantalla.blit(ov, (0, 0))



class CapituloSierras(EscenaBase):

    TITULO = "Capítulo 2 — Las Sierras Bonaerenses"
    REGION = "Sierras Bonaerenses, Buenos Aires · 1870"
    NOMBRE = "capitulo_2"

    POS_INICIAL_JUGADOR = 150.0

    def __init__(self, gestor: GestorEscenas,
                 jugador_x: float = None):
        super().__init__(gestor)

        ANCHO_TRAMO = ANCHO_MUNDO // 2
        self._fondos = [
            cargar_imagen(RUTA_FONDO_SIERRAS_1, (ANCHO_TRAMO, ALTO_PANTALLA)),
            cargar_imagen(RUTA_FONDO_SIERRAS_2, (ANCHO_TRAMO, ALTO_PANTALLA)),
        ]

        self._camara = Camara()

        x_inicial = jugador_x if jugador_x is not None else self.POS_INICIAL_JUGADOR
        self._jugador = Jugador(
            x_inicial,
            gestor.partida["salud"],
            gestor.partida["honor"],
        )

        self._toro_grande = ToroGrande(POS_TORO_GRANDE)
        self._espía       = EspiaCoronel(POS_ESPÍA)
        self._quiroga     = SargentoQuiroga(POS_QUIROGA)
        self._quiroga.activo = False

        self._cruz = None
        if gestor.partida.get("cruz_aliado"):
            self._cruz = Cruz(max(0.0, x_inicial - 150))

        self._inventario    = Inventario(gestor.partida["inventario"])
        self._plantas_mundo = [
            PlantaMundoC2(DATOS_TOLA_SERRANA, POS_PLANTA_TOLA,
                          RUTA_TOLA_SERRANA_IMG),
        ]

        self._boleadoras           = []
        self._soldados_extra       = []
        self._cooldown_lanzamiento = 0.0

        self._dialogo       = SistemaDialogo()
        self._hud           = HUD()
        self._menu_curacion = MenuCuracion()
        self._diario        = Diario()

        for nombre_planta in gestor.partida.get("plantas_conocidas", []):
            self._diario.descubrir_planta(nombre_planta)

        self._fase               = _FASE_INTRO_C2
        self._pagina_intro       = 0
        self._toro_hablo         = False
        self._música_espía_puesta= False
        self._demora_quiroga     = DEMORA_QUIROGA
        self._quiroga_en_camino  = False
        self._timer_trans        = 3.5

        self._cinematica = CinematicaIntroduccionCap2(
            gestor.pantalla, self._fondos[0])

        self._f_tit  = pygame.font.SysFont("Georgia", 28, bold=True)
        self._f_ital = pygame.font.SysFont("Georgia", 20, italic=True)
        self._f_ctrl = pygame.font.SysFont("Arial",   15)
        self._f_etq  = pygame.font.SysFont("Arial",   13)
        self._f_fund = pygame.font.SysFont("Georgia", 22, italic=True)

        reproducir_musica(RUTA_MUSICA_SIERRAS or RUTA_MUSICA_COMBATE, 0.45)


    def manejar_evento(self, evento: pygame.event.Event) -> None:

        if self._diario.manejar_evento(evento):
            return

        if evento.type == pygame.KEYDOWN and evento.key == TECLA_DIARIO:
            self._diario.alternar()
            return
        
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_F5:
            self._guardar_rapido()
            return

        if self._fase == _FASE_INTRO_C2:
            if evento.type == pygame.KEYDOWN and evento.key in (
                    pygame.K_SPACE, pygame.K_RETURN, pygame.K_ESCAPE):
                self._cinematica.terminada = True
            return

        if self._dialogo.activo:
            resultado = self._dialogo.procesar_evento(evento)
            if resultado:
                self._resolver_decision(resultado)
            return

        if self._menu_curacion.activo:
            self._menu_curacion.manejar_evento(
                evento, self._inventario, self._jugador, self._hud)
            return

        if evento.type != pygame.KEYDOWN:
            return

        if self._fase == _FASE_INTRO_C2 and self._cinematica.terminada:
            if evento.key in (pygame.K_SPACE, pygame.K_RETURN):
                self._pagina_intro += 1
                if self._pagina_intro >= len(PAGINAS_INTRO_CAP2):
                    self._fase = _FASE_EXPLORA_C2
                    self._hud.mostrar_mensaje(
                        "A / D  mover      E  hablar      Q  curar      J  diario")

        elif self._fase == _FASE_EXPLORA_C2:
            if evento.key == pygame.K_e:
                self._intentar_interaccion()
            elif evento.key == pygame.K_q:
                self._usar_planta()

        elif self._fase == _FASE_CERCA_ESPÍA:
            if evento.key == pygame.K_e:
                self._iniciar_decision_espía()
            elif evento.key == pygame.K_q:
                self._usar_planta()

        elif self._fase == _FASE_COMBATE_C2:
            if evento.key in (pygame.K_SPACE, pygame.K_z):
                self._lanzar_boleadora()
            elif evento.key == pygame.K_q:
                self._usar_planta()


    def actualizar(self, dt: float) -> None:
        self._hud.actualizar(dt)
        self._diario.actualizar(dt)

        if self._menu_curacion.activo:
            return

        if self._fase == _FASE_INTRO_C2:
            self._cinematica.actualizar(dt)
            return

        if self._dialogo.activo:
            self._dialogo.actualizar(dt)

        if self._fase in (_FASE_EXPLORA_C2, _FASE_CERCA_ESPÍA):
            teclas = pygame.key.get_pressed()
            self._jugador.procesar_entrada(teclas)
            self._jugador.actualizar(dt)
            self._camara.actualizar(self._jugador.x)

            # Actualizar NPCs
            self._toro_grande.actualizar(dt)
            self._espía.actualizar(dt)
            if self._cruz:
                self._cruz.actualizar(dt, self._jugador.x)

            # Actualizar plantas
            for planta in self._plantas_mundo:
                planta.actualizar(dt)

            # Recolectar plantas
            self._recoger_plantas()


            if (not self._toro_hablo
                    and self._toro_grande.cerca_de(self._jugador.rect)):
                self._iniciar_dialogo_toro()

            if (self._fase == _FASE_EXPLORA_C2
                    and not self._música_espía_puesta
                    and self._espía.cerca_de(self._jugador.rect,
                                             DISTANCIA_MUSICA_ESPIA)):
                self._música_espía_puesta = True
                self._fase = _FASE_CERCA_ESPÍA
                reproducir_musica(RUTA_MUSICA_ESPÍA or RUTA_MUSICA_DECISION, 0.5)
                self._hud.mostrar_mensaje(
                    "Hay alguien mirándote raro...  [E] acercarte")

        elif self._fase == _FASE_COMBATE_C2:
            self._actualizar_combate(dt)

        elif self._fase == _FASE_TRANS_C2:
            self._timer_trans -= dt
            if self._timer_trans <= 0:
                self._guardar_y_avanzar()

    def _actualizar_combate(self, dt: float) -> None:
        teclas = pygame.key.get_pressed()
        self._jugador.procesar_entrada(teclas)
        self._jugador.actualizar(dt)
        self._camara.actualizar(self._jugador.x)

        # Cruz también lucha si está libre
        if self._cruz:
            self._cruz.actualizar(dt, self._jugador.x)

        # Enfriamiento de boleadora
        if self._cooldown_lanzamiento > 0:
            self._cooldown_lanzamiento -= dt

        if self._quiroga_en_camino:
            self._demora_quiroga -= dt
            if self._demora_quiroga <= 0:
                self._quiroga.activo   = True
                self._quiroga_en_camino = False

        # Actualizar Quiroga
        if self._quiroga.activo:
            self._quiroga.actualizar(dt, self._jugador.x)

            # Daño al jugador
            if self._quiroga.toca_al_jugador(self._jugador.rect):
                self._jugador.recibir_danio(DANIO_SOLDADO)

            if self._cruz and not self._cruz.atado:
                if self._quiroga.rect.colliderect(self._cruz.rect):
                    self._cruz.recibir_danio(DAÑO_SOLDADO_A_CRUZ)

        # Actualizar boleadoras
        for bol in self._boleadoras:
            bol.actualizar(dt)

            if (self._quiroga.activo
                    and self._quiroga.colisiona_con_boleadora(bol.rect)):
                bol.activa = False
                derribado  = self._quiroga.recibir_impacto()
                if derribado:
                    self._hud.mostrar_mensaje(
                        "¡Quiroga cayó! La sierra es tuya.")

        self._boleadoras = [b for b in self._boleadoras if b.activa]

        self._recoger_plantas()

        if self._quiroga.activo and self._quiroga.caido:
            self._fase = _FASE_TRANS_C2

    def dibujar(self, pantalla: pygame.Surface) -> None:

        if self._fase == _FASE_INTRO_C2 and not self._cinematica.terminada:
            self._cinematica.dibujar()
            return

        self._dibujar_fondos(pantalla)

        if self._fase == _FASE_INTRO_C2 and self._cinematica.terminada:
            _dibujar_intro_textual(pantalla, self.TITULO,
                                   PAGINAS_INTRO_CAP2, self._pagina_intro,
                                   self._f_tit, self._f_ital, self._f_ctrl)
            return

        for planta in self._plantas_mundo:
            planta.dibujar(pantalla, self._camara)

        self._toro_grande.dibujar(pantalla, self._camara)
        self._espía.dibujar(pantalla, self._camara)
        if self._quiroga.activo:
            self._quiroga.dibujar(pantalla, self._camara)

        if self._cruz:
            self._cruz.dibujar(pantalla, self._camara)

        for bol in self._boleadoras:
            bol.dibujar(pantalla, self._camara)

        self._jugador.dibujar(pantalla, self._camara)

        self._hud.dibujar(pantalla,
                          self._jugador.salud,
                          self._jugador.honor,
                          self._inventario)

        if self._dialogo.activo:
            self._dialogo.dibujar(pantalla)

        self._diario.dibujar(pantalla)

        if self._fase == _FASE_COMBATE_C2:
            self._dibujar_hud_combate(pantalla)

        if self._fase == _FASE_TRANS_C2:
            _dibujar_fundido(pantalla, self._timer_trans, 3.5,
                             "Rumbo al litoral...", self._f_fund)

        _dibujar_etiqueta_capitulo(pantalla, self._f_etq,
                                   self.TITULO, self.REGION)

    def _dibujar_fondos(self, pantalla: pygame.Surface) -> None:
        ANCHO_TRAMO = ANCHO_MUNDO // 2   # 1920
        for idx, fondo in enumerate(self._fondos):
            x_en_mundo    = idx * ANCHO_TRAMO
            x_en_pantalla = self._camara.aplicar_x(float(x_en_mundo))
            # Solo dibujar si está dentro de la ventana
            if -ANCHO_TRAMO < x_en_pantalla < ANCHO_PANTALLA:
                pantalla.blit(fondo, (x_en_pantalla, 0))

    def _dibujar_hud_combate(self, pantalla: pygame.Surface) -> None:
        f = pygame.font.SysFont("Arial", 14)
        cd = max(0.0, self._cooldown_lanzamiento)
        if cd > 0:
            txt = f.render(f"Boleadora: {cd:.1f}s", True, COLOR_HONOR_ORO)
        else:
            txt = f.render("Boleadora: lista  [Espacio / Z]", True, COLOR_HONOR_ORO)
        pantalla.blit(txt, (ANCHO_PANTALLA // 2 - txt.get_width() // 2,
                            ALTO_PANTALLA - SistemaDialogo.ALTO_CAJA - 55))


    def _recoger_plantas(self) -> None:
        for planta in self._plantas_mundo:
            if planta.puede_recoger(self._jugador.rect):
                self._inventario.agregar(planta.datos)
                planta.recogida = True
                # Registrar en el diario
                nombre = planta.datos["nombre"]
                self._diario.descubrir_planta(nombre)
                if nombre not in self.gestor.partida["plantas_conocidas"]:
                    self.gestor.partida["plantas_conocidas"].append(nombre)
                self._hud.mostrar_mensaje(
                    f"Recogiste: {nombre}  ·  [Q] para curar  ·  [J] diario")

    def _usar_planta(self) -> None:
        if not len(self._inventario):
            self._hud.mostrar_mensaje("No tenés plantas en el inventario.")
            return
        self._menu_curacion.abrir()

    def _lanzar_boleadora(self) -> None:
        if self._cooldown_lanzamiento > 0:
            return
        dir_x     = 1 if self._jugador.mirando_der else -1
        x_inicio  = self._jugador.x + (ANCHO_VIS_PERSONAJE if dir_x > 0 else 0)
        self._boleadoras.append(Boleadora(x_inicio, dir_x))
        self._cooldown_lanzamiento = COOLDOWN_LANZAMIENTO
        self._jugador.iniciar_animacion_ataque()

    def _intentar_interaccion(self) -> None:
        if (not self._toro_hablo
                and self._toro_grande.cerca_de(self._jugador.rect)):
            self._iniciar_dialogo_toro()
        elif (self._fase in (_FASE_CERCA_ESPÍA, _FASE_EXPLORA_C2)
              and self._espía.cerca_de(self._jugador.rect, 90)):
            self._iniciar_decision_espía()


    def _iniciar_dialogo_toro(self) -> None:

        self._fase       = _FASE_DLG_TORO
        self._toro_hablo = True

        lineas = [
            # Presentación
            LineaDialogo("Toro Grande",
                "No muchos pasan por acá sin propósito. "
                "¿De dónde venís, gaucho?"),
            LineaDialogo("Chicha",
                "De la pampa. Escapé del Coronel Ibáñez. "
                "Voy al sur."),
            LineaDialogo("Toro Grande",
                "Ibáñez. Lo conozco. Ese hombre cree que construir "
                "una nación significa borrar lo que ya estaba."),

            # Historia oral querandí
            LineaDialogo("Toro Grande", DIALOGO_HISTORIA_QUERANDÍ),
            LineaDialogo("Toro Grande",
                "Pero acá estoy yo todavía. Y las sierras también. "
                "Algunas cosas no se pueden borrar del todo."),
            LineaDialogo("Chicha",
                "No sabía que ustedes... que su pueblo había resistido tanto."),
            LineaDialogo("Toro Grande",
                "Pocos lo saben. Los libros que escriben los vencedores "
                "no suelen hablar de los que les hicieron frente."),

            # Enseñanza de la planta medicinal
            LineaDialogo("Toro Grande",
                "Venís cansado. Te veo. Hay algo que te puede ayudar."),
            LineaDialogo("Toro Grande",
                f"{DATOS_TOLA_SERRANA['nombre']} "
                f"({DATOS_TOLA_SERRANA['nombre_cient']}). "
                f"{DATOS_TOLA_SERRANA['descripcion']}"),
            LineaDialogo("Toro Grande",
                f"Propiedad: {DATOS_TOLA_SERRANA['propiedad']}. "
                f"Cura {DATOS_TOLA_SERRANA['curacion']} puntos de vida. "
                "La encontrás entre las rocas de por acá."),

            # Advertencia sobre el espía
            LineaDialogo("Toro Grande",
                "Una cosa más antes de que sigas. "
                "Hay un hombre en la plaza que no es del pueblo. "
                "Lo vi anoche hablando en voz baja con un mensajero. "
                "Cuidado con ese."),
            LineaDialogo("Chicha",
                "¿Un espía del Coronel?"),
            LineaDialogo("Toro Grande",
                "No lo sé con certeza. Pero huelo cuando algo no cierra. "
                "Y ese hombre no cierra."),
        ]

        self._dialogo.iniciar(
            lineas,
            callback_cerrar=self._finalizar_dialogo_toro
        )

        self._diario.desbloquear_reflexion(REFLEXION_TORO_GRANDE["clave"])

    def _finalizar_dialogo_toro(self) -> None:
        self._fase = _FASE_EXPLORA_C2
        self._hud.mostrar_mensaje(
            "Buscá la tola serrana en las rocas. Y cuidado con el hombre de la plaza.")

    def _iniciar_decision_espía(self) -> None:
        self._fase = _FASE_DECISION_ESPÍA
        reproducir_musica(RUTA_MUSICA_DECISION, 0.55)

        lineas_base = [
            LineaDialogo("Chicha",
                "Ese hombre lleva un rato mirándome. "
                "Toro Grande me avisó de alguien sospechoso..."),
            LineaDialogo("Chicha",
                "Si es un espía del Coronel, ya sabe que estoy acá. "
                "¿Lo enfrento o me hago el desentendido?"),
        ]

        lineas_cruz = []
        if self._cruz and not self._cruz.atado:
            lineas_cruz = [
                LineaDialogo("Cruz",
                    "Chicha, si lo confrontás va a alertar a Quiroga. "
                    "Pero si te quedás callado, tampoco sabés cuánto sabe."),
            ]

        opciones = [
            Opcion(
                "Confrontar al espía. Quiero saber qué sabe.",
                efecto_honor=+15,
                resultado="confrontar",
            ),
            Opcion(
                "Irse en silencio. No vale la pena el riesgo.",
                efecto_honor=-5,
                resultado="huir",
            ),
        ]

        self._dialogo.iniciar(lineas_base + lineas_cruz, opciones)

    def _resolver_decision(self, opcion: Opcion) -> None:
        self.gestor.sumar_honor(opcion.efecto_honor)
        self._jugador.honor = self.gestor.partida["honor"]

        if opcion.resultado == "confrontar":

            self.gestor.partida["decisiones"]["confronto_espía"] = True
            self._espía.descubierto = True

            self._fase               = _FASE_COMBATE_C2
            self._quiroga_en_camino  = True
            self._hud.mostrar_mensaje(
                "¡El espía escapó y alertó a Quiroga! "
                "Usá las boleadoras. [Espacio / Z]")
            reproducir_musica(RUTA_MUSICA_COMBATE, 0.6)

        elif opcion.resultado == "huir":
            # Registrar decisión
            self.gestor.partida["decisiones"]["confronto_espía"] = False
            self._hud.mostrar_mensaje(
                "Pasaste desapercibido. Seguís tu camino.")
            # Ir directo a la transición (sin combate)
            self._fase = _FASE_TRANS_C2
            reproducir_musica(RUTA_MUSICA_SIERRAS, 0.4)

    def _sincronizar_partida(self) -> None:
        self.gestor.partida["salud"]      = self._jugador.salud
        self.gestor.partida["honor"]      = self._jugador.honor
        self.gestor.partida["inventario"] = self._inventario.a_lista()

    def _guardar_rapido(self) -> None:
        self._sincronizar_partida()
        guardar_partida(self.gestor.partida, self.NOMBRE, self._jugador.x)
        self._hud.mostrar_mensaje("Partida guardada  [F5]")

    def _guardar_y_avanzar(self) -> None:
        self._sincronizar_partida()

        self.gestor.cambiar("fin_demo")