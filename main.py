import pygame
import obj
import func

pygame.init()  # se inicia pygame
clock = pygame.time.Clock()  # se establece un reloj para medir el tiempo
fullScreen_sz = width, height = pygame.display.Info().current_w - 100, pygame.display.Info().current_h - 100
# ^^^TUPLA CON LA RESOLUCION DE LA PANTALLA^^^

# COLORES
black = 0, 0, 0
white = 255, 255, 255
red = 179, 32, 36
bright_red = 233, 29, 41
cream = 255, 255, 204
green = 18, 230, 3
bright_green = 99, 255, 32
#############
# FUENTES
freesans = pygame.font.SysFont("freesans", 54)
#############
# BOTONES
cerrar = obj.Boton(red, bright_red, 860, 440, 200, 110, quit, "Exit")  # RECORDAR DEJAR RESOLUCION DE TODAS LAS
#                                                                        IMAGENES EN FUNCION DE LA RESOLUCION ACTUAL
comenzar = obj.Boton(green, bright_green, 400, 440, 200, 110, func.boton_comenzar, "Comenzar")
#############
# CUADROS
main_cuadro = obj.Cuadro(("Matias", black), fullScreen_sz, cream)
#############

screen = pygame.display.set_mode(fullScreen_sz, pygame.HWSURFACE | pygame.DOUBLEBUF)
fps_counter = obj.Texto(clock.get_fps(), freesans, black)
menus = [True, False, False]  # especifica el menu
#      0           1          2
# [main_menu, pause_menu, play_menu]

# MAIN LOOP
while True:
    clock.tick(60)  # 60 FPS
    screen.fill(white)
    fps_counter.update(str(int(clock.get_fps())))
    screen.blit(fps_counter.texto, (1, 1))  # contador de fps
    posicion_mouse = pygame.mouse.get_pos()
    for i in menus:  # botones cambian dependiendo en que pantalla esta el jugador.
        main_menu, pause_menu, play_menu = menus[0], menus[1], menus[2]
    if main_menu:
        botones = [cerrar, comenzar]
        cuadros = []
    elif pause_menu:
        botones = [cerrar]
        cuadros = []
    elif play_menu:
        botones = [cerrar]
        cuadros = [main_cuadro]
    for boton in botones:
        if boton.hover(posicion_mouse):
            boton.dibujar(screen, 0)
        else:
            boton.dibujar(screen)
        if boton.id == 1:
            boton.mostrar_texto(screen)
    for cuadro in cuadros:
        cuadro.dibujar(screen)
    for event in pygame.event.get():  # comienza deteccion de eventos
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] == 1:  # click izquierdo
                for boton in botones:
                    if boton.hover(posicion_mouse):
                        resultado = boton.ejecutar()
                        if resultado is not None:
                            menus = resultado
                        break
                else:  # si no se rompio el for con un break
                    if len(cuadros) == 1:  # si solo hay un cuadro en pantalla
                        cuadros[0].actualizar_texto()
    pygame.display.flip()  # actualiza la display
