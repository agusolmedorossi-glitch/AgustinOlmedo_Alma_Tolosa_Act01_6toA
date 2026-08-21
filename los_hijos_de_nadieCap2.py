import pygame
import os
import math

from los_hijos_de_nadie import (
    ANCHO_PANTALLA, ALTO_PANTALLA, FPS, SUELO,
    ANCHO_MUNDO, MARGEN_CAM_X,
    ANCHO_CUADRO_PERSONAJE, ALTO_CUADRO_PERSONAJE,
    ANCHO_VIS_PERSONAJE, ALTO_VIS_PERSONAJE,
    ESCALA_GAMEPLAY, FRAMES_SPRITESHEET_4,
    ANCHO_CUADRO_CURACION, ALTO_CUADRO_CURACION,
    SALUD_MAXIMA, HONOR_MAXIMO, UMBRAL_HONOR_ALTO,
    VELOCIDAD_NORMAL, VELOCIDAD_HERIDO, UMBRAL_VIDA_HERIDO,
    SALUD_INICIAL,
    VELOCIDAD_BOLEADORA, VELOCIDAD_SOLDADO, DANIO_BOLEADORA,
    DISTANCIA_ATAQUE_SOLDADO, DANIO_SOLDADO, COOLDOWN_LANZAMIENTO,
    SALUD_CRUZ_MAXIMA, SELUD_CRUZ_INICIAL, DISTANCIA_SEGUIR,
    VELOCIDAD_CRUZ, DAÑO_SOLDADO_A_CRUZ,
    COLOR_BLANCO, COLOR_NEGRO, COLOR_TIERRA, COLOR_TIERRA_BORDE,
    COLOR_VERDE_VIDA, COLOR_ROJO_DANIO, COLOR_HONOR_ORO,
    COLOR_CAJA_DLG, COLOR_OVERLAY_INTRO, COLOR_LLAVE,
    cargar_imagen, reproducir_musica, dibujar_texto_envuelto,
    dibujar_caja, _quitar_fondo_solido, guardar_partida, ARCHIVO_GUARDADO,
    GestorEscenas, EscenaBase, HojaSprites, Camara,
    Jugador, Cruz, Soldado, Boleadora,
    Inventario, SistemaDialogo, LineaDialogo, Opcion,
    HUD, MenuCuracion, Diario,
    _dibujar_intro_textual, _dibujar_fundido, _dibujar_etiqueta_capitulo,
    RUTA_CHICHA_NORMAL, RUTA_CHICHA_RENGUEANDO, RUTA_CHICHA_COMBATE,
    RUTA_CHICHA_CURACION, RUTA_SOLDADO_AVANCE, RUTA_SOLDADO_CAIDO,
    RUTA_BOLEADORA, RUTA_MUSICA_COMBATE, RUTA_MUSICA_DECISION,
    RUTA_CRUZ_LIBRE, RUTA_CRUZ_ATADO,
    TECLA_DIARIO,
)

RUTA_FONDO_SIERRAS_1 = r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Paisajes\sierras.png"
RUTA_FONDO_SIERRAS_2 = r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Paisajes\Sierra02.png"
RUTA_FONDO_PUEBLO    = r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Paisajes\SierrasPueblo.png"

RUTA_TORO_GRANDE_IMG = r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Npc_Personajes\ToroGrande.png"
RUTA_TORO_GRANDE_SS  = r""
RUTA_ESPIA           = r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Npc_Personajes\espia.png"
RUTA_QUIROGA         = r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Npc_Personajes\SargentoQuiroga.png"

RUTA_SPRITESHEET_CABALLO = r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Npc_Personajes\caballo.jpg"  # ← RUTA

RUTA_SPRITESHEET_ARBUSTOS = r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Objetos\arbustos_cap2.png"  # ← RUTA

RUTA_TOLA_SERRANA_IMG = r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Objetos\Tola_Serrana.png"       # ← RUTA

RUTA_MUSICA_SIERRAS           = r"C:\Users\almat\OneDrive\Documentos\LosHijosDeNadie\Media\Musica\Sierras_Cap2.ogg" 
RUTA_MUSICA_ESPIA             = r""
RUTA_MUSICA_MINIJUEGO_CABALLO = r""
RUTA_MUSICA_SIGILO            = r""

POS_YANIS          = 450
POS_TORO_GRANDE    = 1100
POS_PLANTA_TOLA    = 1400
POS_ARBUSTO_1      = 1800
POS_ARBUSTO_2      = 2050
POS_ARBUSTO_3      = 2300
POS_ESPIA          = 2550
POS_QUIROGA        = 3200


UMBRAL_FONDO_PUEBLO = 2200

ESCALA_TORO    = 0.15
ANCHO_VIS_TORO = int(1024 * ESCALA_TORO)
ALTO_VIS_TORO  = int(1024 * ESCALA_TORO)

# Quiroga
VELOCIDAD_QUIROGA = 1.8
SALUD_QUIROGA_MAX = 3       # impactos de boleadora para derribarlo
DEMORA_QUIROGA    = 3.0     # segundos de espera antes de que aparezca

# Distancias de activación
DISTANCIA_MUSICA_ESPIA  = 450
DISTANCIA_TRIGGER_YANIS = 130

# Caballo Yanis
ANCHO_CUADRO_CABALLO    = 200
ALTO_CUADRO_CABALLO     = 200
CANTIDAD_FRAMES_CABALLO = 4
ESCALA_CABALLO_MAPA     = 0.70
ESCALA_CABALLO_MJ       = 0.55   # minijuego

# Minijuego del caballo
VEL_CURSOR_MJ    = 200    # px/seg del cursor automático
VEL_OBJETIVO_MJ  = 90     # px/seg del objetivo
ANCHO_OBJETIVO_MJ= 120    # px de ancho del rectángulo objetivo
ANCHO_BARRA_MJ   = 700    # px de ancho total de la barra
ALTO_BARRA_MJ    = 30
TIEMPO_NECES_MJ  = 2.5    # segundos dentro del objetivo para ganar
DUR_MAX_MJ       = 25.0   # tiempo máximo antes de fracasar
IMPULSO_ESPACIO  = 180    # cuánto empuja ESPACIO al cursor

ESTADO_MJ_JUGANDO = "jugando"
ESTADO_MJ_EXITO   = "exito"
ESTADO_MJ_FRACASO = "fracaso"

# Arbustos
ANCHO_CUADRO_ARBUSTO = 80
ALTO_CUADRO_ARBUSTO  = 80
ESCALA_ARBUSTO       = 0.90

# Sistema de sospecha
DIST_DETECCION        = 300   # px radio normal de detección
DIST_DETECCION_OCULTO = 80    # px radio cuando Chicha está oculto
VEL_SOSPECHA          = 18    # puntos/seg que sube
VEL_BAJA_SOSPECHA     = 10    # puntos/seg que baja
SOSPECHA_MAXIMA       = 100
SOSPECHA_ARBUSTO      = 12    # bonus al entrar/salir de arbusto cerca del espía
ALPHA_OCULTO          = 140   # transparencia de Chicha mientras está escondido


DATOS_TOLA_SERRANA = {
    "nombre":       "Tola Serrana",
    "nombre_cient": "Parastrephia lepidophylla",
    "propiedad":    "Alivia el cansancio y el dolor de cabeza",
    "descripcion": (
        "La tola serrana crece entre las rocas de las sierras. "
        "Los querandíes la usaban para recuperar fuerzas en largas caminatas. "
        "Se prepara como infusión y alivia el cansancio en pocas horas."
    ),
    "curacion": 35,
    "imagen":   RUTA_TOLA_SERRANA_IMG,
}

DIALOGO_HISTORIA_QUERANDI = (
    "Mi pueblo, los querandíes, dominó estas tierras mucho antes de "
    "que llegaran los españoles. Resistimos sus ataques durante años. "
    "Nos llamaban guerreros. Después nos borraron de los libros. "
    "Pero la sierra recuerda."
)

REFLEXION_TORO_GRANDE = {
    "clave":  "toro_querandi",
    "titulo": "Sobre Toro Grande y los querandíes",
    "texto": (
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


_FASE_INTRO_C2       = "intro"
_FASE_EXPLORA_C2     = "exploracion"
_FASE_MINIJUEGO_C2   = "minijuego_caballo"
_FASE_DLG_TORO       = "dialogo_toro_grande"
_FASE_PUEBLO_C2      = "pueblo"
_FASE_EXPLORA_ESPIA  = "exploracion_espia"
_FASE_CERCA_ESPIA    = "cerca_espia"
_FASE_DECISION_ESPIA = "decision_espia"
_FASE_COMBATE_C2     = "combate_quiroga"
_FASE_TRANS_C2       = "transicion"

class Caballo:
    """
    Yanis, el caballo de Chicha.
    Nivel 1: control básico e interacción simple (Capítulo 2).
    Los niveles 2 y 3 quedan como arquitectura para capítulos futuros.
    """

    NIVEL_VINCULO_1 = 1   # Cap.2 — control básico
    NIVEL_VINCULO_2 = 2   # Cap.3 — recolección desde la montura (futuro)
    NIVEL_VINCULO_3 = 3   # Cap.4 — desarme y rescate (futuro)

    def __init__(self, x_mundo: float):
        self.nombre        = "Yanis"
        self.x             = float(x_mundo)
        self.activo        = True
        self.montado       = False
        self.nivel_vinculo = 0    # sin vínculo al inicio
        self.confianza     = 0    # 0-100

        self._hoja = HojaSprites(
            RUTA_SPRITESHEET_CABALLO,
            ANCHO_CUADRO_CABALLO,
            ALTO_CUADRO_CABALLO,
            ESCALA_CABALLO_MAPA,
        )
        self._cuadro      = 0
        self._timer_anim  = 0.0
        self._vel_anim    = 0.20
        self._tick        = 0
        self._fuente      = pygame.font.SysFont("Arial", 13)

        self.rect = pygame.Rect(
            int(self.x),
            SUELO - int(ALTO_CUADRO_CABALLO * ESCALA_CABALLO_MAPA),
            int(ANCHO_CUADRO_CABALLO * ESCALA_CABALLO_MAPA),
            int(ALTO_CUADRO_CABALLO  * ESCALA_CABALLO_MAPA),
        )

    def ganar_confianza(self, puntos: int) -> None:

        self.confianza = min(100, self.confianza + puntos)
        if self.confianza >= 100 and self.nivel_vinculo < self.NIVEL_VINCULO_1:
            self.nivel_vinculo = self.NIVEL_VINCULO_1

    def cerca_de(self, rect_jugador: pygame.Rect, dist: int = 130) -> bool:
        return self.rect.colliderect(rect_jugador.inflate(dist, dist))

    def actualizar(self, dt: float) -> None:
        self._tick += 1
        self._timer_anim += dt
        if self._timer_anim >= self._vel_anim:
            self._timer_anim = 0.0
            self._cuadro     = (self._cuadro + 1) % CANTIDAD_FRAMES_CABALLO

    def dibujar(self, pantalla: pygame.Surface, camara: Camara) -> None:
        if not self.activo or self.montado:
            return
        frame = self._hoja.obtener_frame(self._cuadro)
        x_pan = camara.aplicar_x(self.x)
        y_pan = SUELO - frame.get_height()
        pantalla.blit(frame, (x_pan, y_pan))

        etq   = self._fuente.render(f"▼ {self.nombre}", True, COLOR_HONOR_ORO)
        ex    = x_pan + frame.get_width() // 2 - etq.get_width() // 2
        ey    = y_pan - 18
        fondo = pygame.Surface((etq.get_width() + 8, etq.get_height() + 4), pygame.SRCALPHA)
        fondo.fill((0, 0, 0, 145))
        pantalla.blit(fondo, (ex - 4, ey - 2))
        pantalla.blit(etq, (ex, ey))

class MinijuegoCaballo:
    """
    Minijuego para ganarse la confianza de Yanis.
    El jugador mantiene el cursor rojo dentro del rectángulo objetivo
    durante TIEMPO_NECES_MJ segundos.
    ESPACIO impulsa el cursor hacia el centro del objetivo.
    """

    def __init__(self, pantalla: pygame.Surface, caballo: Caballo):
        self._pantalla       = pantalla
        self._caballo        = caballo
        self.estado          = ESTADO_MJ_JUGANDO
        self._espacio_held   = False

        # Spritesheet de Yanis para la pantalla del minijuego (escala diferente)
        self._hoja_yanis = HojaSprites(
            RUTA_SPRITESHEET_CABALLO,
            ANCHO_CUADRO_CABALLO,
            ALTO_CUADRO_CABALLO,
            ESCALA_CABALLO_MJ,
        )
        self._cuadro_anim = 0
        self._timer_anim  = 0.0

        # Geometría de la barra centrada
        self._barra_x = (ANCHO_PANTALLA - ANCHO_BARRA_MJ) // 2
        self._barra_y = ALTO_PANTALLA - 150

        # Posiciones flotantes del cursor y el objetivo
        self._cursor_x    = float(self._barra_x)
        self._dir_cursor  = 1
        self._objetivo_x  = float(self._barra_x + ANCHO_BARRA_MJ // 2)
        self._dir_obj     = 1

        # Contadores de tiempo
        self._tiempo_dentro   = 0.0
        self._tiempo_total    = 0.0
        self._timer_resultado = 0.0
        self._dur_resultado   = 2.5

        self._f_titulo    = pygame.font.SysFont("Georgia", 28, bold=True)
        self._f_pista     = pygame.font.SysFont("Arial",   14)
        self._f_resultado = pygame.font.SysFont("Georgia", 22, italic=True)

    # ── Propiedades calculadas ────────────────────────────────────────────────

    @property
    def _cx(self) -> int:
        """Cursor clampeado a la barra, en coordenadas de pantalla."""
        return int(max(self._barra_x,
                       min(self._cursor_x, self._barra_x + ANCHO_BARRA_MJ - 12)))

    @property
    def _ox(self) -> int:
        """Objetivo clampeado a la barra."""
        return int(max(self._barra_x,
                       min(self._objetivo_x,
                           self._barra_x + ANCHO_BARRA_MJ - ANCHO_OBJETIVO_MJ)))

    @property
    def _cursor_en_objetivo(self) -> bool:
        return self._cx >= self._ox and self._cx <= self._ox + ANCHO_OBJETIVO_MJ

    @property
    def terminado(self) -> bool:
        return (self.estado != ESTADO_MJ_JUGANDO and
                self._timer_resultado >= self._dur_resultado)

    def manejar_evento(self, evento: pygame.event.Event) -> None:
        if self.estado != ESTADO_MJ_JUGANDO:
            return
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            self._espacio_held = True
        if evento.type == pygame.KEYUP and evento.key == pygame.K_SPACE:
            self._espacio_held = False

    def actualizar(self, dt: float) -> None:
        # Animación del caballo
        self._timer_anim += dt
        if self._timer_anim >= 0.18:
            self._timer_anim  = 0.0
            self._cuadro_anim = (self._cuadro_anim + 1) % CANTIDAD_FRAMES_CABALLO

        if self.estado == ESTADO_MJ_JUGANDO:
            self._tiempo_total += dt

            # Mover cursor: ESPACIO lo atrae al objetivo; sin ESPACIO oscila
            if self._espacio_held:
                centro_obj = self._ox + ANCHO_OBJETIVO_MJ // 2
                self._cursor_x += (IMPULSO_ESPACIO if self._cursor_x < centro_obj
                                   else -IMPULSO_ESPACIO) * dt
            else:
                self._cursor_x += VEL_CURSOR_MJ * self._dir_cursor * dt

            # Rebotar en extremos
            if self._cursor_x <= self._barra_x:
                self._cursor_x  = float(self._barra_x)
                self._dir_cursor = 1
            elif self._cursor_x >= self._barra_x + ANCHO_BARRA_MJ - 12:
                self._cursor_x  = float(self._barra_x + ANCHO_BARRA_MJ - 12)
                self._dir_cursor = -1

            # Mover objetivo
            self._objetivo_x += VEL_OBJETIVO_MJ * self._dir_obj * dt
            if self._objetivo_x <= self._barra_x:
                self._objetivo_x = float(self._barra_x)
                self._dir_obj    = 1
            elif self._objetivo_x >= self._barra_x + ANCHO_BARRA_MJ - ANCHO_OBJETIVO_MJ:
                self._objetivo_x = float(self._barra_x + ANCHO_BARRA_MJ - ANCHO_OBJETIVO_MJ)
                self._dir_obj    = -1

            # Acumular o perder tiempo en objetivo
            if self._cursor_en_objetivo:
                self._tiempo_dentro += dt
            else:
                self._tiempo_dentro = max(0.0, self._tiempo_dentro - dt * 0.8)

            # Verificar resultado
            if self._tiempo_dentro >= TIEMPO_NECES_MJ:
                self.estado = ESTADO_MJ_EXITO
            elif self._tiempo_total >= DUR_MAX_MJ:
                self.estado = ESTADO_MJ_FRACASO

        else:
            self._timer_resultado += dt

    def reiniciar(self) -> None:
        self.estado           = ESTADO_MJ_JUGANDO
        self._cursor_x        = float(self._barra_x)
        self._dir_cursor      = 1
        self._objetivo_x      = float(self._barra_x + ANCHO_BARRA_MJ // 2)
        self._dir_obj         = 1
        self._tiempo_dentro   = 0.0
        self._tiempo_total    = 0.0
        self._timer_resultado = 0.0
        self._espacio_held    = False

    def dibujar(self) -> None:
        pantalla = self._pantalla

        # Oscurecer el fondo del juego
        ov = pygame.Surface((ANCHO_PANTALLA, ALTO_PANTALLA), pygame.SRCALPHA)
        ov.fill((0, 0, 0, 195))
        pantalla.blit(ov, (0, 0))

        # Yanis centrado en pantalla
        frame   = self._hoja_yanis.obtener_frame(self._cuadro_anim)
        x_yanis = ANCHO_PANTALLA // 2 - frame.get_width() // 2
        y_yanis = ALTO_PANTALLA  // 2 - frame.get_height() - 60
        pantalla.blit(frame, (x_yanis, y_yanis))

        # Título y pista
        tit = self._f_titulo.render("Calma a Yanis", True, COLOR_HONOR_ORO)
        pantalla.blit(tit, (ANCHO_PANTALLA // 2 - tit.get_width() // 2, 60))
        pts = self._f_pista.render(
            "Mantené ESPACIO para llevar el cursor al área dorada",
            True, (190, 175, 145))
        pantalla.blit(pts, (ANCHO_PANTALLA // 2 - pts.get_width() // 2, 105))

        if self.estado == ESTADO_MJ_JUGANDO:
            self._dibujar_barra(pantalla)
            self._dibujar_progreso(pantalla)
        elif self.estado == ESTADO_MJ_EXITO:
            for i, txt in enumerate(["Yanis comienza a confiar en vos.",
                                     "Conseguiste una montura."]):
                s = self._f_resultado.render(txt, True, COLOR_HONOR_ORO)
                pantalla.blit(s, (ANCHO_PANTALLA // 2 - s.get_width() // 2,
                                  ALTO_PANTALLA  // 2 + i * 40))
        elif self.estado == ESTADO_MJ_FRACASO:
            for i, txt in enumerate(["El caballo se apartó.",
                                     "Presioná cualquier tecla para volver a intentarlo."]):
                s = self._f_resultado.render(txt, True, (200, 160, 100))
                pantalla.blit(s, (ANCHO_PANTALLA // 2 - s.get_width() // 2,
                                  ALTO_PANTALLA  // 2 + i * 40))

    def _dibujar_barra(self, pantalla):
        bx, by = self._barra_x, self._barra_y
        # Fondo de barra
        pygame.draw.rect(pantalla, (50, 42, 30),
                         (bx, by, ANCHO_BARRA_MJ, ALTO_BARRA_MJ), border_radius=4)
        # Objetivo dorado
        pygame.draw.rect(pantalla, (160, 130, 40),
                         (self._ox, by, ANCHO_OBJETIVO_MJ, ALTO_BARRA_MJ), border_radius=3)
        pygame.draw.rect(pantalla, COLOR_HONOR_ORO,
                         (self._ox, by, ANCHO_OBJETIVO_MJ, ALTO_BARRA_MJ), 2, border_radius=3)
        # Cursor rojo
        pygame.draw.rect(pantalla, COLOR_ROJO_DANIO,
                         (self._cx, by - 4, 12, ALTO_BARRA_MJ + 8), border_radius=3)
        # Borde
        pygame.draw.rect(pantalla, COLOR_TIERRA_BORDE,
                         (bx, by, ANCHO_BARRA_MJ, ALTO_BARRA_MJ), 2, border_radius=4)

    def _dibujar_progreso(self, pantalla):
        if TIEMPO_NECES_MJ <= 0:
            return
        prog       = self._tiempo_dentro / TIEMPO_NECES_MJ
        ancho_prog = int(300 * min(1.0, prog))
        bx = ANCHO_PANTALLA // 2 - 150
        by = self._barra_y + ALTO_BARRA_MJ + 24
        pygame.draw.rect(pantalla, (40, 40, 40), (bx, by, 300, 14), border_radius=3)
        if ancho_prog > 0:
            color = (60, 180, 60) if prog < 0.8 else COLOR_HONOR_ORO
            pygame.draw.rect(pantalla, color, (bx, by, ancho_prog, 14), border_radius=3)
        pygame.draw.rect(pantalla, COLOR_TIERRA_BORDE, (bx, by, 300, 14), 1, border_radius=3)
        etq = self._f_pista.render("Confianza", True, (160, 150, 130))
        pantalla.blit(etq, (bx + 150 - etq.get_width() // 2, by - 18))


# =============================================================================
# SECCIÓN 7 — ARBUSTO ESCONDITE
# =============================================================================

class ArbustoEscondite:
    """
    Objeto interactivo en el mapa que sirve como escondite para Chicha.
    Usa coordenadas del mundo y se desplaza con la cámara.
    """

    def __init__(self, x_mundo: float, hoja: HojaSprites, indice_frame: int = 0):
        self.x       = float(x_mundo)
        self.activo  = True
        self.ocupado = False   # True cuando Chicha está escondido aquí
        self.nivel_ocultamiento = 0.75   # factor que reduce la detección

        self._hoja   = hoja
        self._frame  = indice_frame % max(1, hoja.total_cuadros)
        self._fuente = pygame.font.SysFont("Arial", 12)

        frame_muestra = hoja.obtener_frame(self._frame)
        self.rect = pygame.Rect(
            int(self.x),
            SUELO - frame_muestra.get_height(),
            frame_muestra.get_width(),
            frame_muestra.get_height(),
        )

    def puede_ocultar(self, rect_jugador: pygame.Rect) -> bool:
        """True si el jugador está suficientemente cerca para esconderse."""
        return self.activo and self.rect.colliderect(rect_jugador.inflate(80, 80))

    def actualizar(self, dt: float) -> None:
        pass   # arbustos estáticos; se podría animar el movimiento del viento aquí

    def dibujar(self, pantalla: pygame.Surface, camara: Camara,
                jugador_oculto: bool = False) -> None:
        if not self.activo:
            return
        frame = self._hoja.obtener_frame(self._frame)
        x_pan = camara.aplicar_x(self.x)
        y_pan = SUELO - frame.get_height()
        pantalla.blit(frame, (x_pan, y_pan))

        # Indicación contextual de la tecla E
        if self.puede_ocultar(pygame.Rect(x_pan, y_pan, 1, 1)):
            txt = "E — Salir" if jugador_oculto else "E — Esconderse"
            s   = self._fuente.render(txt, True, COLOR_HONOR_ORO)
            pantalla.blit(s, (x_pan + frame.get_width() // 2 - s.get_width() // 2,
                               y_pan - 20))


# =============================================================================
# SECCIÓN 8 — BARRA DE SOSPECHA
# =============================================================================

class BarraSospecha:
    """
    Nivel de sospecha de un enemigo/espía individual (0-100).
    Se dibuja flotando sobre el NPC cuando tiene valor > 0.
    """

    def __init__(self):
        self.valor          = 0.0
        self.estado_soldado = "patrullando"
        self._fuente        = pygame.font.SysFont("Arial", 11)

    def aumentar(self, cantidad: float) -> None:
        self.valor = min(SOSPECHA_MAXIMA, self.valor + cantidad)
        self._actualizar_estado()

    def disminuir(self, cantidad: float) -> None:
        self.valor = max(0.0, self.valor - cantidad)
        self._actualizar_estado()

    def reiniciar(self) -> None:
        self.valor          = 0.0
        self.estado_soldado = "patrullando"

    def _actualizar_estado(self) -> None:
        if self.estado_soldado == "neutralizado":
            return
        if self.valor >= SOSPECHA_MAXIMA:
            self.estado_soldado = "persiguiendo"
        elif self.valor >= 75:
            self.estado_soldado = "alerta"
        elif self.valor >= 50:
            self.estado_soldado = "buscando"
        elif self.valor >= 25:
            self.estado_soldado = "investigando"
        else:
            self.estado_soldado = "patrullando"

    @property
    def descubierto(self) -> bool:
        return self.valor >= SOSPECHA_MAXIMA

    def dibujar_sobre_npc(self, pantalla: pygame.Surface,
                          x_pantalla: int, y_pantalla: int) -> None:
        if self.valor <= 0:
            return
        ANC, ALT = 50, 6
        bx = x_pantalla - ANC // 2
        by = y_pantalla - 30
        pygame.draw.rect(pantalla, (30, 30, 30), (bx, by, ANC, ALT))
        rel = int(ANC * self.valor / SOSPECHA_MAXIMA)
        if rel:
            p = self.valor / SOSPECHA_MAXIMA
            col = (60, 160, 60) if p < 0.4 else (210, 155, 20) if p < 0.7 else COLOR_ROJO_DANIO
            pygame.draw.rect(pantalla, col, (bx, by, rel, ALT))
        pygame.draw.rect(pantalla, (140, 120, 90), (bx, by, ANC, ALT), 1)
        if self.valor >= 25:
            etq = self._fuente.render("!", True, (220, 200, 80))
            pantalla.blit(etq, (bx + ANC + 3, by - 1))


# =============================================================================
# SECCIÓN 9 — NPC TORO GRANDE
# =============================================================================

class ToroGrande:
    """
    Personaje querandí. Acepta imagen estática o spritesheet.
    Si no hay ninguno disponible, usa el placeholder de cargar_imagen.
    """

    ANCHO_CAJA = int(ANCHO_VIS_TORO * 0.5)
    ALTO_CAJA  = ALTO_VIS_TORO

    def __init__(self, x_mundo: float):
        self.x_mundo = float(x_mundo)
        self.nombre  = "Toro Grande"
        self.activo  = True
        self._tick   = 0
        self._desplaz= 0
        self._fuente = pygame.font.SysFont("Arial", 13)

        self._imagen_estatica = None
        self._hoja_ss         = None
        self._cuadro_ss       = 0
        self._timer_ss        = 0.0

        if RUTA_TORO_GRANDE_IMG and os.path.exists(RUTA_TORO_GRANDE_IMG):
            self._imagen_estatica = cargar_imagen(RUTA_TORO_GRANDE_IMG,
                                                  (ANCHO_VIS_TORO, ALTO_VIS_TORO))
        elif RUTA_TORO_GRANDE_SS and os.path.exists(RUTA_TORO_GRANDE_SS):
            self._hoja_ss = HojaSprites(RUTA_TORO_GRANDE_SS,
                                        ANCHO_CUADRO_PERSONAJE,
                                        ALTO_CUADRO_PERSONAJE,
                                        ESCALA_GAMEPLAY)
        else:
            self._imagen_estatica = cargar_imagen("", (ANCHO_VIS_TORO, ALTO_VIS_TORO))

        self.rect = pygame.Rect(
            int(self.x_mundo) + (ANCHO_VIS_TORO - self.ANCHO_CAJA) // 2,
            SUELO - self.ALTO_CAJA,
            self.ANCHO_CAJA, self.ALTO_CAJA,
        )

    def actualizar(self, dt: float) -> None:
        self._tick    += 1
        self._desplaz  = int(math.sin(self._tick * 0.04) * 1.5)
        if self._hoja_ss:
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
        if self._imagen_estatica:
            pantalla.blit(self._imagen_estatica, (x_pan, y_pan))
        elif self._hoja_ss:
            pantalla.blit(self._hoja_ss.obtener_frame(self._cuadro_ss), (x_pan, y_pan))
        etq   = self._fuente.render(f"▼ {self.nombre}", True, COLOR_BLANCO)
        ex    = x_pan + ANCHO_VIS_TORO // 2 - etq.get_width() // 2
        ey    = y_pan - 18
        fondo = pygame.Surface((etq.get_width() + 8, etq.get_height() + 4), pygame.SRCALPHA)
        fondo.fill((0, 0, 0, 145))
        pantalla.blit(fondo, (ex - 4, ey - 2))
        pantalla.blit(etq, (ex, ey))


# =============================================================================
# SECCIÓN 10 — ESPÍA DEL CORONEL
# =============================================================================

class EspiaCoronel:
    """
    Espía que patrulla y acumula sospecha cuando detecta a Chicha.
    Usa RUTA_ESPIA si existe; si no, usa el spritesheet del soldado.
    """

    ANCHO_CAJA = int(ANCHO_VIS_PERSONAJE * 0.55)
    ALTO_CAJA  = ALTO_VIS_PERSONAJE

    def __init__(self, x_mundo: float):
        self.x_mundo     = float(x_mundo)
        self.nombre      = "Hombre sospechoso"
        self.activo      = True
        self.descubierto = False
        self._cuadro     = 0
        self._timer_anim = 0.0
        self._fuente     = pygame.font.SysFont("Arial", 13)

        # Rango de patrulla
        self._x_min    = x_mundo - 200
        self._x_max    = x_mundo + 200
        self._dir      = 1
        self._vel      = 0.6

        self.sospecha  = BarraSospecha()

        ruta = (RUTA_ESPIA if RUTA_ESPIA and os.path.exists(RUTA_ESPIA)
                else RUTA_SOLDADO_AVANCE)
        self._hoja = HojaSprites(ruta, ANCHO_CUADRO_PERSONAJE,
                                 ALTO_CUADRO_PERSONAJE, ESCALA_GAMEPLAY)

        self.rect = pygame.Rect(
            int(self.x_mundo) + (ANCHO_VIS_PERSONAJE - self.ANCHO_CAJA) // 2,
            SUELO - self.ALTO_CAJA,
            self.ANCHO_CAJA, self.ALTO_CAJA,
        )

    def actualizar(self, dt: float, jugador_x: float,
                   jugador_oculto: bool, arbustos: list) -> None:
        # Patrulla o persigue según el estado de sospecha
        if self.sospecha.estado_soldado not in ("persiguiendo", "neutralizado"):
            self.x_mundo += self._vel * self._dir
            if self.x_mundo >= self._x_max:
                self._dir = -1
            elif self.x_mundo <= self._x_min:
                self._dir = 1
        elif self.sospecha.estado_soldado == "persiguiendo":
            self.x_mundo += self._vel * 1.8 * (1 if self.x_mundo < jugador_x else -1)
        self.rect.x = int(self.x_mundo) + (ANCHO_VIS_PERSONAJE - self.ANCHO_CAJA) // 2

        # Detección: radio reducido si Chicha está oculto con cobertura
        dist         = abs(self.x_mundo - jugador_x)
        radio        = DIST_DETECCION_OCULTO if jugador_oculto else DIST_DETECCION
        hay_cobertura= jugador_oculto and any(
            abs(a.x - jugador_x) < a.rect.width for a in arbustos if a.ocupado)

        if dist <= radio and not hay_cobertura:
            self.sospecha.aumentar(VEL_SOSPECHA * dt)
        else:
            self.sospecha.disminuir(VEL_BAJA_SOSPECHA * dt)

        # Animación
        self._timer_anim += dt
        if self._timer_anim >= 0.65:
            self._timer_anim = 0.0
            self._cuadro     = (self._cuadro + 1) % FRAMES_SPRITESHEET_4

    def cerca_de(self, rect_jugador: pygame.Rect, dist: int = 150) -> bool:
        return self.rect.colliderect(rect_jugador.inflate(dist, dist))

    def dibujar(self, pantalla: pygame.Surface, camara: Camara) -> None:
        if not self.activo:
            return
        x_pan = camara.aplicar_x(self.x_mundo)
        frame = self._hoja.obtener_frame(self._cuadro)
        if self._dir < 0:
            frame = pygame.transform.flip(frame, True, False)
        x_pan += (ANCHO_VIS_PERSONAJE - frame.get_width()) // 2
        y_pan  = SUELO - frame.get_height()
        pantalla.blit(frame, (x_pan, y_pan))

        color_etq  = COLOR_ROJO_DANIO if self.descubierto else (200, 200, 80)
        nom_vis    = "Espía del Coronel" if self.descubierto else self.nombre
        etq        = self._fuente.render(f"▼ {nom_vis}", True, color_etq)
        ex         = x_pan + ANCHO_VIS_PERSONAJE // 2 - etq.get_width() // 2
        ey         = y_pan - 18
        fondo      = pygame.Surface((etq.get_width() + 8, etq.get_height() + 4),
                                    pygame.SRCALPHA)
        fondo.fill((0, 0, 0, 145))
        pantalla.blit(fondo, (ex - 4, ey - 2))
        pantalla.blit(etq, (ex, ey))
        self.sospecha.dibujar_sobre_npc(pantalla,
                                        x_pan + ANCHO_VIS_PERSONAJE // 2, y_pan)


# =============================================================================
# SECCIÓN 11 — SARGENTO QUIROGA
# =============================================================================

class SargentoQuiroga:
    """
    Antagonista del Capítulo 2.
    Necesita SALUD_QUIROGA_MAX impactos de boleadora para caer.
    La animación de caída se CONGELA en el frame 3 (no vuelve al 0).
    """

    ANCHO_CAJA = int(ANCHO_VIS_PERSONAJE * 0.55)
    ALTO_CAJA  = ALTO_VIS_PERSONAJE

    def __init__(self, x_mundo: float):
        self.x_mundo     = float(x_mundo)
        self.nombre      = "Sgto. Quiroga"
        self.activo      = True
        self.caido       = False
        self.salud       = SALUD_QUIROGA_MAX
        self._cuadro     = 0
        self._timer_anim = 0.0
        self._vel_anim   = 0.18
        self._fuente     = pygame.font.SysFont("Arial", 13)

        ruta = (RUTA_QUIROGA if RUTA_QUIROGA and os.path.exists(RUTA_QUIROGA)
                else RUTA_SOLDADO_AVANCE)
        self._hoja_avance = HojaSprites(ruta, ANCHO_CUADRO_PERSONAJE,
                                        ALTO_CUADRO_PERSONAJE, ESCALA_GAMEPLAY)
        self._hoja_caido  = HojaSprites(RUTA_SOLDADO_CAIDO, ANCHO_CUADRO_PERSONAJE,
                                        ALTO_CUADRO_PERSONAJE, ESCALA_GAMEPLAY)

        self.rect = pygame.Rect(
            int(self.x_mundo) + (ANCHO_VIS_PERSONAJE - self.ANCHO_CAJA) // 2,
            SUELO - self.ALTO_CAJA,
            self.ANCHO_CAJA, self.ALTO_CAJA,
        )

    def recibir_impacto(self) -> bool:
        """Descuenta 1 de salud. Devuelve True si acaba de caer."""
        if self.caido:
            return False
        self.salud -= 1
        if self.salud <= 0:
            self.caido   = True
            self._cuadro = 0
        return self.caido

    def actualizar(self, dt: float, pos_jugador_x: float) -> None:
        if self.caido:
            # Avanzar hasta el frame 3 y QUEDARSE AHÍ (no usar %)
            self._timer_anim += dt
            if self._timer_anim >= self._vel_anim and self._cuadro < 3:
                self._timer_anim = 0.0
                self._cuadro    += 1
            return

        # Avanzar hacia el jugador
        if self.x_mundo > pos_jugador_x + ANCHO_VIS_PERSONAJE:
            self.x_mundo -= VELOCIDAD_QUIROGA
        elif self.x_mundo < pos_jugador_x - ANCHO_VIS_PERSONAJE:
            self.x_mundo += VELOCIDAD_QUIROGA

        self.rect.x      = int(self.x_mundo) + (ANCHO_VIS_PERSONAJE - self.ANCHO_CAJA) // 2
        self.rect.bottom = SUELO

        self._timer_anim += dt
        if self._timer_anim >= self._vel_anim:
            self._timer_anim = 0.0
            self._cuadro     = (self._cuadro + 1) % FRAMES_SPRITESHEET_4

    def toca_al_jugador(self, rect_j: pygame.Rect) -> bool:
        return not self.caido and self.rect.colliderect(rect_j)

    def colisiona_con_boleadora(self, rect_b: pygame.Rect) -> bool:
        return not self.caido and self.rect.colliderect(rect_b)

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
        fondo = pygame.Surface((etq.get_width() + 8, etq.get_height() + 4), pygame.SRCALPHA)
        fondo.fill((0, 0, 0, 145))
        pantalla.blit(fondo, (ex - 4, ey - 2))
        pantalla.blit(etq, (ex, ey))
        if not self.caido:
            self._dibujar_resistencia(pantalla, x_pan, y_pan)

    def _dibujar_resistencia(self, pantalla, xp, yp):
        R, G = 6, 16
        xb   = xp + ANCHO_VIS_PERSONAJE // 2 - (SALUD_QUIROGA_MAX * G) // 2
        yb   = yp - 22
        for i in range(SALUD_QUIROGA_MAX):
            c = COLOR_ROJO_DANIO if i < self.salud else (60, 60, 60)
            pygame.draw.circle(pantalla, c, (xb + i * G, yb), R)
            pygame.draw.circle(pantalla, COLOR_BLANCO, (xb + i * G, yb), R, 1)


# =============================================================================
# SECCIÓN 12 — PLANTA EN EL MUNDO (Cap.2)
# =============================================================================

class PlantaMundoC2:
    """Planta coleccionable con imagen real o placeholder animado."""

    RADIO = 13

    def __init__(self, datos: dict, x_mundo: float, ruta_imagen: str = ""):
        self.datos    = datos
        self.nombre   = datos["nombre"]
        self.recogida = False
        self._x       = float(x_mundo)
        self._tick    = 0
        self._fuente  = pygame.font.SysFont("Arial", 11)
        self._imagen  = None

        if ruta_imagen and os.path.exists(ruta_imagen):
            img = pygame.image.load(ruta_imagen).convert_alpha()
            img.set_colorkey(COLOR_LLAVE)
            self._imagen = pygame.transform.scale(img, (40, 40))

        self.rect = pygame.Rect(
            int(x_mundo) - self.RADIO,
            SUELO - self.RADIO * 2 - 4,
            self.RADIO * 2, self.RADIO * 2,
        )

    def actualizar(self, dt: float) -> None:
        self._tick += 1

    def puede_recoger(self, rect_j: pygame.Rect) -> bool:
        return not self.recogida and self.rect.colliderect(rect_j.inflate(55, 55))

    def dibujar(self, pantalla: pygame.Surface, camara: Camara) -> None:
        if self.recogida:
            return
        radio = self.RADIO + int(math.sin(self._tick * 0.08) * 2)
        cx    = camara.aplicar_x(int(self._x))
        cy    = SUELO - self.RADIO * 2 - 4

        if self._imagen:
            pantalla.blit(self._imagen, (cx - 20, cy - 20))
        else:
            cp = (60, 160, 120)
            for r, a in [(radio + 7, 30), (radio + 3, 70)]:
                h = pygame.Surface((r * 2, r * 2), pygame.SRCALPHA)
                pygame.draw.circle(h, (*cp, a), (r, r), r)
                pantalla.blit(h, (cx - r, cy - r))
            pygame.draw.circle(pantalla, cp, (cx, cy), radio)
            pygame.draw.circle(pantalla, COLOR_BLANCO, (cx, cy), radio, 2)
            ltr = self._fuente.render(self.nombre[0], True, COLOR_BLANCO)
            pantalla.blit(ltr, (cx - ltr.get_width() // 2, cy - ltr.get_height() // 2))

        etq = self._fuente.render(self.nombre, True, COLOR_BLANCO)
        pantalla.blit(etq, (cx - etq.get_width() // 2, cy - radio - 15))


# =============================================================================
# SECCIÓN 13 — CINEMÁTICA DE INTRODUCCIÓN DEL CAPÍTULO 2
# =============================================================================

class CinematicaIntroduccionCap2:
    """
    Cinemática breve de apertura: fondo de las sierras con Chicha rengueando
    y el título del capítulo apareciendo progresivamente.
    """

    DUR_TOTAL      = 6.0
    VEL_PANORAMICA = 80.0

    def __init__(self, pantalla: pygame.Surface, fondo: pygame.Surface):
        self._pantalla   = pantalla
        self._fondo      = fondo
        self._timer      = 0.0
        self.terminada   = False
        self._scroll_x   = 0.0
        self._chicha_x   = float(-ANCHO_VIS_PERSONAJE)
        self._cuadro     = 0
        self._timer_anim = 0.0

        self._hoja = HojaSprites(RUTA_CHICHA_RENGUEANDO,
                                 ANCHO_CUADRO_PERSONAJE,
                                 ALTO_CUADRO_PERSONAJE,
                                 ESCALA_GAMEPLAY)
        self._f_tit = pygame.font.SysFont("Georgia", 42, bold=True)
        self._f_sub = pygame.font.SysFont("Georgia", 26, italic=True)

    def actualizar(self, dt: float) -> None:
        if self.terminada:
            return
        self._timer    += dt
        self._scroll_x += self.VEL_PANORAMICA * dt
        self._chicha_x += VELOCIDAD_HERIDO

        self._timer_anim += dt
        if self._timer_anim >= 0.15:
            self._timer_anim = 0.0
            self._cuadro     = (self._cuadro % 3) + 1

        if self._timer >= self.DUR_TOTAL:
            self.terminada = True

    def dibujar(self) -> None:
        scroll = min(int(self._scroll_x), ANCHO_MUNDO - ANCHO_PANTALLA)
        self._pantalla.blit(self._fondo, (-scroll, 0))

        frame    = self._hoja.obtener_frame(self._cuadro)
        x_chicha = int(self._chicha_x)
        y_chicha = SUELO - frame.get_height()
        self._pantalla.blit(frame, (x_chicha, y_chicha))

        progreso = self._timer / self.DUR_TOTAL
        if progreso > 0.2:
            alpha = min(255, int(255 * (progreso - 0.2) / 0.3))
            t1 = self._f_tit.render("Capítulo 2", True, COLOR_HONOR_ORO)
            t2 = self._f_sub.render("Las Sierras Bonaerenses", True, COLOR_BLANCO)
            t1.set_alpha(alpha)
            t2.set_alpha(alpha)
            self._pantalla.blit(t1, (ANCHO_PANTALLA // 2 - t1.get_width() // 2,
                                     ALTO_PANTALLA  // 2 - 60))
            self._pantalla.blit(t2, (ANCHO_PANTALLA // 2 - t2.get_width() // 2,
                                     ALTO_PANTALLA  // 2 + 10))

        if progreso < 0.15:
            alpha_ov = int(255 * (1.0 - progreso / 0.15))
            ov = pygame.Surface((ANCHO_PANTALLA, ALTO_PANTALLA))
            ov.set_alpha(alpha_ov)
            ov.fill(COLOR_NEGRO)
            self._pantalla.blit(ov, (0, 0))


# =============================================================================
# SECCIÓN 14 — ESCENA PRINCIPAL: CapituloSierras
# =============================================================================

class CapituloSierras(EscenaBase):
    """
    Capítulo 2 completo.

    ╔══════════════════════════════════════════════════════════════╗
    ║  CORRECCIÓN DEL BUG DE ESPACIO                              ║
    ║                                                              ║
    ║  manejar_evento() diferencia EXPLÍCITAMENTE:                ║
    ║    A) cinemática en curso  → ESPACIO/ENTER/ESC la saltan    ║
    ║    B) cinemática terminada → ESPACIO/ENTER avanzan página   ║
    ║                                                              ║
    ║  Los dos sub-casos tienen su propio `return`.               ║
    ║  NO existe un `return` compartido que tape al caso B.       ║
    ╚══════════════════════════════════════════════════════════════╝
    """

    TITULO = "Capítulo 2 — Las Sierras Bonaerenses"
    REGION = "Sierras Bonaerenses, Buenos Aires · 1870"
    NOMBRE = "capitulo_2"
    POS_INICIAL_JUGADOR = 150.0

    def __init__(self, gestor: GestorEscenas, jugador_x: float = None):
        super().__init__(gestor)

        # ── Tres fondos independientes ────────────────────────────────────────
        # Cada tramo de sierras cubre ANCHO_MUNDO // 2 = 1920 px.
        # El fondo del pueblo se superpone cuando la cámara supera UMBRAL_FONDO_PUEBLO.
        ANCHO_TRAMO = ANCHO_MUNDO // 2
        self._fondo_sierras_1 = cargar_imagen(RUTA_FONDO_SIERRAS_1,
                                              (ANCHO_TRAMO, ALTO_PANTALLA))
        self._fondo_sierras_2 = cargar_imagen(RUTA_FONDO_SIERRAS_2,
                                              (ANCHO_TRAMO, ALTO_PANTALLA))
        self._fondo_pueblo    = cargar_imagen(RUTA_FONDO_PUEBLO,
                                              (ANCHO_PANTALLA, ALTO_PANTALLA))

        self._camara = Camara()

        # ── Jugador ───────────────────────────────────────────────────────────
        x_inicial = jugador_x if jugador_x is not None else self.POS_INICIAL_JUGADOR
        self._jugador = Jugador(x_inicial,
                                gestor.partida["salud"],
                                gestor.partida["honor"])

        # Estado de sigilo
        self._jugador_oculto = False
        self._arbusto_activo = None

        # ── NPCs ──────────────────────────────────────────────────────────────
        self._yanis       = Caballo(POS_YANIS)
        self._toro_grande = ToroGrande(POS_TORO_GRANDE)
        self._espia       = EspiaCoronel(POS_ESPIA)
        self._quiroga     = SargentoQuiroga(POS_QUIROGA)
        self._quiroga.activo = False

        # Cruz (solo si fue liberado en el Cap.1)
        self._cruz = None
        if gestor.partida.get("cruz_aliado"):
            self._cruz = Cruz(max(0.0, x_inicial - 150))

        # ── Inventario y plantas ──────────────────────────────────────────────
        self._inventario = Inventario(gestor.partida["inventario"])
        self._plantas_mundo = [
            PlantaMundoC2(DATOS_TOLA_SERRANA, POS_PLANTA_TOLA, RUTA_TOLA_SERRANA_IMG),
        ]

        # ── Arbustos ──────────────────────────────────────────────────────────
        self._hoja_arbustos = HojaSprites(RUTA_SPRITESHEET_ARBUSTOS,
                                          ANCHO_CUADRO_ARBUSTO,
                                          ALTO_CUADRO_ARBUSTO,
                                          ESCALA_ARBUSTO)
        self._arbustos = [
            ArbustoEscondite(POS_ARBUSTO_1, self._hoja_arbustos, 0),
            ArbustoEscondite(POS_ARBUSTO_2, self._hoja_arbustos, 1),
            ArbustoEscondite(POS_ARBUSTO_3, self._hoja_arbustos, 0),
        ]

        # ── Combate ───────────────────────────────────────────────────────────
        self._boleadoras           = []
        self._cooldown_lanzamiento = 0.0

        # ── Sistemas UI ───────────────────────────────────────────────────────
        self._dialogo       = SistemaDialogo()
        self._hud           = HUD()
        self._menu_curacion = MenuCuracion()
        self._diario        = Diario()
        for nombre in gestor.partida.get("plantas_conocidas", []):
            self._diario.descubrir_planta(nombre)

        # ── Minijuego ─────────────────────────────────────────────────────────
        self._minijuego_caballo = MinijuegoCaballo(gestor.pantalla, self._yanis)
        self._yanis_conseguido  = gestor.partida.get("caballo_conseguido", False)

        # ── Máquina de estados ────────────────────────────────────────────────
        self._fase              = _FASE_INTRO_C2
        self._pagina_intro      = 0
        self._toro_hablo        = False
        self._musica_espia_ok   = False
        self._demora_quiroga    = DEMORA_QUIROGA
        self._quiroga_en_camino = False
        self._timer_trans       = 3.5

        # ── Cinemática ────────────────────────────────────────────────────────
        self._cinematica = CinematicaIntroduccionCap2(
            gestor.pantalla, self._fondo_sierras_1)

        # ── Fuentes ───────────────────────────────────────────────────────────
        self._f_tit  = pygame.font.SysFont("Georgia", 28, bold=True)
        self._f_ital = pygame.font.SysFont("Georgia", 20, italic=True)
        self._f_ctrl = pygame.font.SysFont("Arial",   15)
        self._f_etq  = pygame.font.SysFont("Arial",   13)
        self._f_fund = pygame.font.SysFont("Georgia", 22, italic=True)
        self._f_aviso= pygame.font.SysFont("Arial",   14)

        reproducir_musica(RUTA_MUSICA_SIERRAS or RUTA_MUSICA_COMBATE, 0.45)

    # =========================================================================
    # MANEJO DE EVENTOS — CORRECCIÓN CENTRAL DEL BUG
    # =========================================================================

    def manejar_evento(self, evento: pygame.event.Event) -> None:
        """
        Estructura de prioridades de eventos:

        1. Diario (consume cualquier evento si está abierto)
        2. Tecla J → abrir/cerrar diario
        3. F5 → guardar rápido
        4. Fase INTRO:
               4a. cinemática EN CURSO  → ESPACIO/ENTER/ESC la saltan → return
               4b. cinemática TERMINADA → ESPACIO/ENTER avanzan página → return
           IMPORTANTE: estos son dos bloques if SEPARADOS, no anidados.
           Así se garantiza que nunca se mezclen los dos casos.
        5. Minijuego activo
        6. Diálogo activo
        7. Menú de curación activo
        8. Solo KEYDOWN a partir de aquí
        9. Exploración / combate
        """

        # ── 1. Diario ─────────────────────────────────────────────────────────
        if self._diario.manejar_evento(evento):
            return
        if evento.type == pygame.KEYDOWN and evento.key == TECLA_DIARIO:
            self._diario.alternar()
            return

        # ── 2. Guardado rápido ────────────────────────────────────────────────
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_F5:
            self._guardar_rapido()
            return

        # ── 3. Fase de introducción ───────────────────────────────────────────
        if self._fase == _FASE_INTRO_C2:

            # CASO A: cinemática todavía en curso
            # ESPACIO / ENTER / ESC la saltan inmediatamente
            if not self._cinematica.terminada:
                if (evento.type == pygame.KEYDOWN and
                        evento.key in (pygame.K_SPACE, pygame.K_RETURN, pygame.K_ESCAPE)):
                    self._cinematica.terminada = True
                return   # consumir TODOS los eventos durante la cinemática

            # CASO B: cinemática YA terminada — avanzar páginas narrativas
            # Llega aquí solo si self._cinematica.terminada == True
            if evento.type == pygame.KEYDOWN:
                if evento.key in (pygame.K_SPACE, pygame.K_RETURN):
                    self._pagina_intro += 1
                    if self._pagina_intro >= len(PAGINAS_INTRO_CAP2):
                        # Todas las páginas vistas → iniciar exploración
                        self._fase = _FASE_EXPLORA_C2
                        self._hud.mostrar_mensaje(
                            "A / D  mover   E  hablar / esconderse   Q  curar   J  diario")
            return   # consumir todos los eventos durante las páginas narrativas

        # ── 4. Minijuego del caballo ──────────────────────────────────────────
        if self._fase == _FASE_MINIJUEGO_C2:
            self._minijuego_caballo.manejar_evento(evento)
            # Si fracasó y ya mostró el mensaje, cualquier tecla reinicia
            if (self._minijuego_caballo.estado == ESTADO_MJ_FRACASO
                    and self._minijuego_caballo.terminado
                    and evento.type == pygame.KEYDOWN):
                self._minijuego_caballo.reiniciar()
            return

        # ── 5. Diálogo activo ─────────────────────────────────────────────────
        if self._dialogo.activo:
            resultado = self._dialogo.procesar_evento(evento)
            if resultado:
                self._resolver_decision(resultado)
            return

        # ── 6. Menú de curación ───────────────────────────────────────────────
        if self._menu_curacion.activo:
            self._menu_curacion.manejar_evento(
                evento, self._inventario, self._jugador, self._hud)
            return

        # ── Solo procesar KEYDOWN a partir de aquí ────────────────────────────
        if evento.type != pygame.KEYDOWN:
            return

        # ── 7. Exploración general ────────────────────────────────────────────
        if self._fase in (_FASE_EXPLORA_C2, _FASE_EXPLORA_ESPIA, _FASE_PUEBLO_C2):
            if evento.key == pygame.K_e:
                self._intentar_interaccion()
            elif evento.key == pygame.K_q:
                self._usar_planta()

        # ── 8. Zona del espía ─────────────────────────────────────────────────
        elif self._fase == _FASE_CERCA_ESPIA:
            if evento.key == pygame.K_e:
                if self._jugador_oculto:
                    self._salir_de_arbusto()
                else:
                    self._intentar_interaccion()
            elif evento.key == pygame.K_q:
                self._usar_planta()

        # ── 9. Combate ────────────────────────────────────────────────────────
        elif self._fase == _FASE_COMBATE_C2:
            if evento.key in (pygame.K_SPACE, pygame.K_z):
                self._lanzar_boleadora()
            elif evento.key == pygame.K_q:
                self._usar_planta()

    # =========================================================================
    # ACTUALIZACIÓN
    # =========================================================================

    def actualizar(self, dt: float) -> None:
        self._hud.actualizar(dt)
        self._diario.actualizar(dt)

        # Menú de curación pausa el mundo
        if self._menu_curacion.activo:
            return

        # ── Cinemática de intro ───────────────────────────────────────────────
        if self._fase == _FASE_INTRO_C2:
            self._cinematica.actualizar(dt)
            return   # nada más se actualiza durante la intro

        # ── Minijuego del caballo ─────────────────────────────────────────────
        if self._fase == _FASE_MINIJUEGO_C2:
            self._minijuego_caballo.actualizar(dt)
            if self._minijuego_caballo.terminado:
                if self._minijuego_caballo.estado == ESTADO_MJ_EXITO:
                    self._finalizar_minijuego_exito()
            return

        # ── Diálogos activos ──────────────────────────────────────────────────
        if self._dialogo.activo:
            self._dialogo.actualizar(dt)

        # ── Fases de exploración ──────────────────────────────────────────────
        if self._fase in (_FASE_EXPLORA_C2, _FASE_EXPLORA_ESPIA,
                          _FASE_CERCA_ESPIA, _FASE_PUEBLO_C2):

            if not self._jugador_oculto:
                teclas = pygame.key.get_pressed()
                self._jugador.procesar_entrada(teclas)
            self._jugador.actualizar(dt)
            self._camara.actualizar(self._jugador.x)

            self._toro_grande.actualizar(dt)
            self._yanis.actualizar(dt)
            for a in self._arbustos:
                a.actualizar(dt)
            if self._cruz:
                self._cruz.actualizar(dt, self._jugador.x)

            self._espia.actualizar(dt, self._jugador.x,
                                   self._jugador_oculto, self._arbustos)

            for p in self._plantas_mundo:
                p.actualizar(dt)
            self._recoger_plantas()

            # Trigger: Yanis
            if (not self._yanis_conseguido
                    and self._yanis.cerca_de(self._jugador.rect, DISTANCIA_TRIGGER_YANIS)
                    and self._fase == _FASE_EXPLORA_C2):
                self._iniciar_dialogo_yanis()

            # Trigger: Toro Grande
            if (not self._toro_hablo
                    and self._toro_grande.cerca_de(self._jugador.rect)):
                self._iniciar_dialogo_toro()

            # Trigger: zona del espía → cambiar música
            if (self._fase == _FASE_EXPLORA_C2
                    and not self._musica_espia_ok
                    and self._espia.cerca_de(self._jugador.rect, DISTANCIA_MUSICA_ESPIA)):
                self._musica_espia_ok = True
                self._fase = _FASE_EXPLORA_ESPIA
                reproducir_musica(RUTA_MUSICA_ESPIA or RUTA_MUSICA_DECISION, 0.5)
                self._hud.mostrar_mensaje(
                    "Hay alguien mirándote raro...  Usá los arbustos para esconderte.")

            # Trigger: zona inmediata del espía
            if (self._fase == _FASE_EXPLORA_ESPIA
                    and self._espia.cerca_de(self._jugador.rect, 90)):
                self._fase = _FASE_CERCA_ESPIA

            # Si el espía descubre a Chicha automáticamente
            if (self._espia.sospecha.descubierto
                    and self._fase in (_FASE_EXPLORA_ESPIA, _FASE_CERCA_ESPIA)
                    and not self._dialogo.activo):
                self._hud.mostrar_mensaje("¡Te han descubierto!")
                self._iniciar_decision_espia()

        # ── Combate ───────────────────────────────────────────────────────────
        elif self._fase == _FASE_COMBATE_C2:
            self._actualizar_combate(dt)

        # ── Transición ────────────────────────────────────────────────────────
        elif self._fase == _FASE_TRANS_C2:
            self._timer_trans -= dt
            if self._timer_trans <= 0:
                self._guardar_y_avanzar()

    def _actualizar_combate(self, dt: float) -> None:
        """Lógica del combate defensivo contra Quiroga."""
        teclas = pygame.key.get_pressed()
        self._jugador.procesar_entrada(teclas)
        self._jugador.actualizar(dt)
        self._camara.actualizar(self._jugador.x)
        if self._cruz:
            self._cruz.actualizar(dt, self._jugador.x)

        if self._cooldown_lanzamiento > 0:
            self._cooldown_lanzamiento -= dt

        if self._quiroga_en_camino:
            self._demora_quiroga -= dt
            if self._demora_quiroga <= 0:
                self._quiroga.activo    = True
                self._quiroga_en_camino = False

        if self._quiroga.activo:
            self._quiroga.actualizar(dt, self._jugador.x)
            if self._quiroga.toca_al_jugador(self._jugador.rect):
                self._jugador.recibir_danio(DANIO_SOLDADO)
            if self._cruz and not self._cruz.atado:
                if self._quiroga.rect.colliderect(self._cruz.rect):
                    self._cruz.recibir_danio(DAÑO_SOLDADO_A_CRUZ)

        for bol in self._boleadoras:
            bol.actualizar(dt)
            if self._quiroga.activo and self._quiroga.colisiona_con_boleadora(bol.rect):
                bol.activo = False
                if self._quiroga.recibir_impacto():
                    self._hud.mostrar_mensaje("¡Quiroga cayó! La sierra es tuya.")

        self._boleadoras = [b for b in self._boleadoras if b.activo]
        self._recoger_plantas()

        if self._quiroga.activo and self._quiroga.caido:
            self._fase = _FASE_TRANS_C2

    # =========================================================================
    # DIBUJO
    # =========================================================================

    def dibujar(self, pantalla: pygame.Surface) -> None:

        # ── Cinemática ────────────────────────────────────────────────────────
        if self._fase == _FASE_INTRO_C2 and not self._cinematica.terminada:
            self._cinematica.dibujar()
            return

        # ── Fondos (tres imágenes independientes) ────────────────────────────
        self._dibujar_fondos(pantalla)

        # ── Páginas narrativas post-cinemática ────────────────────────────────
        if self._fase == _FASE_INTRO_C2 and self._cinematica.terminada:
            _dibujar_intro_textual(pantalla, self.TITULO, PAGINAS_INTRO_CAP2,
                                   self._pagina_intro,
                                   self._f_tit, self._f_ital, self._f_ctrl)
            return

        # ── Minijuego ─────────────────────────────────────────────────────────
        if self._fase == _FASE_MINIJUEGO_C2:
            self._yanis.dibujar(pantalla, self._camara)
            self._minijuego_caballo.dibujar()
            return

        # ── Elementos del mundo ───────────────────────────────────────────────
        for p in self._plantas_mundo:
            p.dibujar(pantalla, self._camara)
        for a in self._arbustos:
            a.dibujar(pantalla, self._camara, self._jugador_oculto)

        self._yanis.dibujar(pantalla, self._camara)
        self._toro_grande.dibujar(pantalla, self._camara)
        self._espia.dibujar(pantalla, self._camara)
        if self._quiroga.activo:
            self._quiroga.dibujar(pantalla, self._camara)
        if self._cruz:
            self._cruz.dibujar(pantalla, self._camara)
        for bol in self._boleadoras:
            bol.dibujar(pantalla, self._camara)

        # ── Jugador (semitransparente si está oculto) ─────────────────────────
        if self._jugador_oculto:
            frame = self._jugador.hoja_activa.obtener_frame(self._jugador._cuadro)
            frame = frame.copy()
            frame.set_alpha(ALPHA_OCULTO)
            pantalla.blit(frame, (self._camara.aplicar_x(self._jugador.x),
                                  SUELO - ALTO_VIS_PERSONAJE))
        else:
            self._jugador.dibujar(pantalla, self._camara)

        # ── HUD ───────────────────────────────────────────────────────────────
        self._hud.dibujar(pantalla, self._jugador.salud,
                          self._jugador.honor, self._inventario)
        if self._menu_curacion.activo:
            self._menu_curacion.dibujar(pantalla, self._inventario, self._jugador)
        if self._dialogo.activo:
            self._dialogo.dibujar(pantalla)
        self._diario.dibujar(pantalla)

        if self._fase == _FASE_COMBATE_C2:
            self._dibujar_hud_combate(pantalla)
        if self._espia.sospecha.descubierto:
            self._dibujar_aviso_descubierto(pantalla)
        if self._fase == _FASE_TRANS_C2:
            _dibujar_fundido(pantalla, self._timer_trans, 3.5,
                             "Rumbo al litoral...", self._f_fund)

        _dibujar_etiqueta_capitulo(pantalla, self._f_etq, self.TITULO, self.REGION)

    def _dibujar_fondos(self, pantalla: pygame.Surface) -> None:
        """
        Dibuja los tres fondos según la posición de la cámara.

        Fondos 1 y 2 (sierras): cada uno cubre ANCHO_MUNDO//2 = 1920 px.
        Fondo del pueblo: se superpone cuando la cámara supera UMBRAL_FONDO_PUEBLO.
        """
        ANCHO_TRAMO = ANCHO_MUNDO // 2

        # Fondo 1: posición mundo 0
        x1_pan = self._camara.aplicar_x(0.0)
        if -ANCHO_TRAMO < x1_pan < ANCHO_PANTALLA:
            pantalla.blit(self._fondo_sierras_1, (x1_pan, 0))

        # Fondo 2: posición mundo 1920
        x2_pan = self._camara.aplicar_x(float(ANCHO_TRAMO))
        if -ANCHO_TRAMO < x2_pan < ANCHO_PANTALLA:
            pantalla.blit(self._fondo_sierras_2, (x2_pan, 0))

        # Fondo del pueblo: se muestra cuando el jugador llega a la zona del pueblo.
        # Se dibuja por encima de las sierras con una transición de alpha.
        if self._jugador.x >= UMBRAL_FONDO_PUEBLO:
            distancia    = self._jugador.x - UMBRAL_FONDO_PUEBLO
            alpha_pueblo = min(255, int(255 * distancia / 300))
            sup_pueblo   = self._fondo_pueblo.copy()
            sup_pueblo.set_alpha(alpha_pueblo)
            pantalla.blit(sup_pueblo, (0, 0))

    def _dibujar_hud_combate(self, pantalla: pygame.Surface) -> None:
        cd  = max(0.0, self._cooldown_lanzamiento)
        txt = (self._f_aviso.render(f"Boleadora: {cd:.1f}s", True, COLOR_HONOR_ORO)
               if cd > 0 else
               self._f_aviso.render("Boleadora: lista  [Espacio / Z]", True, COLOR_HONOR_ORO))
        pantalla.blit(txt, (ANCHO_PANTALLA // 2 - txt.get_width() // 2,
                            ALTO_PANTALLA - SistemaDialogo.ALTO_CAJA - 55))

    def _dibujar_aviso_descubierto(self, pantalla: pygame.Surface) -> None:
        if (pygame.time.get_ticks() // 400) % 2 == 0:
            aviso = self._f_aviso.render("¡Te han descubierto!", True, COLOR_ROJO_DANIO)
            pantalla.blit(aviso, (ANCHO_PANTALLA // 2 - aviso.get_width() // 2, 80))

    # =========================================================================
    # SIGILO — ARBUSTOS
    # =========================================================================

    def _intentar_esconderse(self) -> bool:
        """Intenta ocultar al jugador en el arbusto más cercano libre."""
        for arbusto in self._arbustos:
            if arbusto.puede_ocultar(self._jugador.rect) and not arbusto.ocupado:
                arbusto.ocupado      = True
                self._jugador_oculto = True
                self._arbusto_activo = arbusto
                if self._espia.cerca_de(self._jugador.rect, DIST_DETECCION):
                    self._espia.sospecha.aumentar(SOSPECHA_ARBUSTO)
                self._hud.mostrar_mensaje("Te escondiste.  [E] para salir")
                return True
        return False

    def _salir_de_arbusto(self) -> None:
        """El jugador sale del arbusto."""
        if self._arbusto_activo:
            self._arbusto_activo.ocupado = False
            self._arbusto_activo         = None
        self._jugador_oculto = False
        if self._espia.cerca_de(self._jugador.rect, DIST_DETECCION):
            self._espia.sospecha.aumentar(SOSPECHA_ARBUSTO)
        self._hud.mostrar_mensaje("Saliste del escondite.")

    # =========================================================================
    # INTERACCIÓN — tecla E
    # =========================================================================

    def _intentar_interaccion(self) -> None:
        """Determina qué acción ejecutar al presionar E."""
        if self._jugador_oculto:
            self._salir_de_arbusto()
            return
        if self._intentar_esconderse():
            return
        if (not self._yanis_conseguido
                and self._yanis.cerca_de(self._jugador.rect, DISTANCIA_TRIGGER_YANIS)):
            self._iniciar_dialogo_yanis()
            return
        if not self._toro_hablo and self._toro_grande.cerca_de(self._jugador.rect):
            self._iniciar_dialogo_toro()
            return
        if (self._fase in (_FASE_EXPLORA_ESPIA, _FASE_CERCA_ESPIA)
                and self._espia.cerca_de(self._jugador.rect, 90)):
            self._iniciar_decision_espia()

    # =========================================================================
    # PLANTAS
    # =========================================================================

    def _recoger_plantas(self) -> None:
        for planta in self._plantas_mundo:
            if planta.puede_recoger(self._jugador.rect):
                self._inventario.agregar(planta.datos)
                planta.recogida = True
                nombre = planta.datos["nombre"]
                self._diario.descubrir_planta(nombre)
                if nombre not in self.gestor.partida["plantas_conocidas"]:
                    self.gestor.partida["plantas_conocidas"].append(nombre)
                self._hud.mostrar_mensaje(f"Recogiste: {nombre}  [Q] curar  [J] diario")

    def _usar_planta(self) -> None:
        if not len(self._inventario):
            self._hud.mostrar_mensaje("No tenés plantas en el inventario.")
            return
        self._menu_curacion.abrir()

    # =========================================================================
    # BOLEADORA
    # =========================================================================

    def _lanzar_boleadora(self) -> None:
        if self._cooldown_lanzamiento > 0:
            return
        dir_x    = 1 if self._jugador.mirando_der else -1
        x_inicio = self._jugador.x + (ANCHO_VIS_PERSONAJE if dir_x > 0 else 0)
        self._boleadoras.append(Boleadora(x_inicio, dir_x))
        self._cooldown_lanzamiento = COOLDOWN_LANZAMIENTO
        self._jugador.iniciar_animacion_ataque()

    # =========================================================================
    # DIÁLOGOS Y NARRATIVA
    # =========================================================================

    def _iniciar_dialogo_yanis(self) -> None:
        lineas = [
            LineaDialogo("Chicha",
                "Ahí hay un caballo. Solo, atado. Parece que alguien lo dejó."),
            LineaDialogo("Chicha",
                "Si puedo calmarle los nervios, puede ser mi compañero de ruta."),
        ]
        if self._cruz and not self._cruz.atado:
            lineas.append(LineaDialogo("Cruz",
                "Los caballos se ganan con paciencia, Chicha."))
        self._dialogo.iniciar(lineas, callback_cerrar=self._abrir_minijuego_caballo)

    def _abrir_minijuego_caballo(self) -> None:
        self._fase = _FASE_MINIJUEGO_C2
        self._minijuego_caballo.reiniciar()
        reproducir_musica(RUTA_MUSICA_MINIJUEGO_CABALLO or RUTA_MUSICA_DECISION, 0.5)

    def _finalizar_minijuego_exito(self) -> None:
        self._yanis_conseguido = True
        self._yanis.ganar_confianza(100)
        self.gestor.partida["caballo_conseguido"] = True
        self._fase = _FASE_EXPLORA_C2
        reproducir_musica(RUTA_MUSICA_SIERRAS or RUTA_MUSICA_COMBATE, 0.45)
        self._hud.mostrar_mensaje("Yanis confía en vos. Ahora buscá a Toro Grande.")
        self._dialogo.iniciar([LineaDialogo("Chicha", "Bien, Yanis. Vamos juntos.")])

    def _iniciar_dialogo_toro(self) -> None:
        self._fase       = _FASE_DLG_TORO
        self._toro_hablo = True

        lineas = [
            LineaDialogo("Toro Grande",
                "No muchos llegan hasta acá sin saber dónde pisan."),
            LineaDialogo("Chicha",
                "Busco una ruta al sur. Y un caballo."),
            LineaDialogo("Toro Grande",
                "Las sierras tienen caminos que no aparecen en los mapas."),
            LineaDialogo("Toro Grande", DIALOGO_HISTORIA_QUERANDI),
            LineaDialogo("Toro Grande",
                "Pero acá estoy yo todavía. Y las sierras también. "
                "Algunas cosas no se pueden borrar del todo."),
            LineaDialogo("Chicha",
                "No sabía que su pueblo había resistido tanto."),
            LineaDialogo("Toro Grande",
                "Pocos lo saben. Los libros que escriben los vencedores "
                "no suelen hablar de los que les hicieron frente."),
            LineaDialogo("Toro Grande",
                "Venís cansado. Hay algo que te puede ayudar."),
            LineaDialogo("Toro Grande",
                f"{DATOS_TOLA_SERRANA['nombre']} "
                f"({DATOS_TOLA_SERRANA['nombre_cient']}). "
                f"{DATOS_TOLA_SERRANA['descripcion']}"),
            LineaDialogo("Toro Grande",
                f"Propiedad: {DATOS_TOLA_SERRANA['propiedad']}. "
                f"Cura {DATOS_TOLA_SERRANA['curacion']} puntos de vida. "
                "La encontrás entre las rocas de por acá."),
            LineaDialogo("Toro Grande",
                "Una cosa más. Hay un hombre en el pueblo que no es del lugar. "
                "Lo vi hablando con un mensajero. Cuidate."),
            LineaDialogo("Chicha", "¿Un espía del Coronel?"),
            LineaDialogo("Toro Grande",
                "No lo sé con certeza. Pero huelo cuando algo no cierra. "
                "Y ese hombre no cierra."),
        ]

        if self._cruz and not self._cruz.atado:
            lineas.insert(1, LineaDialogo("Toro Grande", "Veo que no viajás solo."))
            lineas.insert(2, LineaDialogo("Cruz",
                "El camino se hace distinto cuando uno no lo enfrenta solo."))

        self._diario.desbloquear_reflexion(REFLEXION_TORO_GRANDE["clave"])
        self._dialogo.iniciar(lineas, callback_cerrar=self._finalizar_dialogo_toro)

    def _finalizar_dialogo_toro(self) -> None:
        self._fase = _FASE_EXPLORA_C2
        self._hud.mostrar_mensaje(
            "Buscá la Tola Serrana entre las rocas. Cuidado con el hombre de la plaza.")

    def _iniciar_decision_espia(self) -> None:
        self._fase = _FASE_DECISION_ESPIA
        reproducir_musica(RUTA_MUSICA_DECISION, 0.55)

        lineas = [
            LineaDialogo("Chicha",
                "Ese hombre lleva un rato mirándome. "
                "Toro Grande me avisó de alguien sospechoso..."),
            LineaDialogo("Chicha",
                "Si es un espía del Coronel, ya sabe que estoy acá. "
                "¿Lo enfrento o me hago el desentendido?"),
        ]
        if self._cruz and not self._cruz.atado:
            lineas.append(LineaDialogo("Cruz",
                "Si lo confrontás va a alertar a Quiroga. "
                "Pero si te callás, tampoco sabés cuánto sabe."))

        opciones = [
            Opcion("Confrontarlo. Quiero saber qué sabe.",
                   efecto_honor=+15, resultado="confrontar"),
            Opcion("Irme en silencio. No vale la pena el riesgo.",
                   efecto_honor=-5,  resultado="huir"),
        ]
        self._dialogo.iniciar(lineas, opciones)

    def _resolver_decision(self, opcion: Opcion) -> None:
        self.gestor.sumar_honor(opcion.efecto_honor)
        self._jugador.honor = self.gestor.partida["honor"]

        if opcion.resultado == "confrontar":
            self.gestor.partida["decisiones"]["confronto_espia"] = True
            self._espia.descubierto  = True
            self._fase               = _FASE_COMBATE_C2
            self._quiroga_en_camino  = True
            self._hud.mostrar_mensaje(
                "¡El espía alertó a Quiroga! Usá las boleadoras. [Espacio / Z]")
            reproducir_musica(RUTA_MUSICA_COMBATE, 0.6)

        elif opcion.resultado == "huir":
            self.gestor.partida["decisiones"]["confronto_espia"] = False
            self._hud.mostrar_mensaje("Pasaste desapercibido. Seguís tu camino.")
            self._fase = _FASE_TRANS_C2
            reproducir_musica(RUTA_MUSICA_SIERRAS or RUTA_MUSICA_COMBATE, 0.4)

    # =========================================================================
    # GUARDADO Y TRANSICIÓN
    # =========================================================================

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
        # Intentar pasar al Cap.3; si no existe, usar fin_demo como seguro
        destino = "capitulo_3"
        try:
            self.gestor.cambiar(destino)
        except KeyError:
            self.gestor.cambiar("fin_demo")


# =============================================================================
# SECCIÓN 15 — INSTRUCCIONES DE INTEGRACIÓN
# =============================================================================
#
# 1. En main.py (o en la función main() de los_hijos_de_nadie.py):
#
#       from capitulo2_corregido import CapituloSierras
#       gestor.registrar("capitulo_2", CapituloSierras)
#
# 2. En CapituloPampa._guardar_y_avanzar() (Capítulo 1):
#       self.gestor.cambiar("capitulo_2")
#
# 3. Para probar el Cap.2 directamente:
#       gestor.cambiar("capitulo_2")
#
# 4. Assets nuevos necesarios (ponés las rutas en la Sección 1):
#       RUTA_FONDO_SIERRAS_1  — imagen panorámica primera mitad (1920×720 recomendado)
#       RUTA_FONDO_SIERRAS_2  — imagen panorámica segunda mitad (1920×720 recomendado)
#       RUTA_FONDO_PUEBLO     — imagen del pueblo Tres Lagunas (1280×720)
#       RUTA_SPRITESHEET_CABALLO  — spritesheet de Yanis
#       RUTA_SPRITESHEET_ARBUSTOS — spritesheet de arbustos
#       (las rutas de Tola Serrana y músicas ya estaban)
# =============================================================================