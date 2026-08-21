import pygame
import sys


from los_hijos_de_nadie import (
    ANCHO_PANTALLA,
    ALTO_PANTALLA,
    FPS,

    GestorEscenas,

    MenuPrincipal,
    EscenaCinematica,
    CapituloPampa,
    FinDemo,

    cargar_partida,
)


from los_hijos_de_nadieCap2 import CapituloSierras


def main():


    pygame.init()

    if not pygame.mixer.get_init():
        pygame.mixer.init()


    pantalla = pygame.display.set_mode(
        (ANCHO_PANTALLA, ALTO_PANTALLA)
    )

    pygame.display.set_caption(
        "Los Hijos de Nadie"
    )

    reloj = pygame.time.Clock()

    gestor = GestorEscenas(pantalla)

    # Menú principal
    gestor.registrar(
        "menu",
        MenuPrincipal
    )

    # Cinemática introductoria
    gestor.registrar(
        "cinematica",
        EscenaCinematica
    )

#Cap 1

    gestor.registrar(
        "capitulo_1",
        CapituloPampa
    )

#Cap 2

    gestor.registrar(
        "capitulo_2",
        CapituloSierras
    )



    gestor.registrar(
        "fin_demo",
        FinDemo
    )


    gestor.cambiar("menu")


    ejecutando = True

    while ejecutando:

        for evento in pygame.event.get():

            # Cerrar ventana
            if evento.type == pygame.QUIT:

                ejecutando = False

                continue

            if (
                evento.type == pygame.KEYDOWN
                and evento.key == pygame.K_F9
            ):

                datos = cargar_partida()

                if datos:

                    gestor.aplicar_guardado(datos)

                    capitulo_guardado = datos.get(
                        "capitulo",
                        "capitulo_1"
                    )

                    jugador_x = datos.get(
                        "jugador_x",
                        200.0
                    )


                    if capitulo_guardado == "capitulo_2":

                        gestor.cambiar(
                            "capitulo_2",
                            jugador_x=jugador_x
                        )

                    else:

                        gestor.cambiar(
                            "capitulo_1",
                            jugador_x=jugador_x
                        )

                continue

            if gestor.escena_actual is not None:

                gestor.escena_actual.manejar_evento(
                    evento
                )


        dt = reloj.tick(FPS) / 1000.0

        if gestor.escena_actual is not None:

            gestor.escena_actual.actualizar(dt)

            gestor.escena_actual.dibujar(
                pantalla
            )
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()