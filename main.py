import pygame
import os
import obj
import func

pygame.init()  # se inicia pygame
clock = pygame.time.Clock()  # se establece un reloj para medir el tiempo
screenInfo = pygame.display.Info()  # info de la resolucion de la pantalla
screen_res = screen_w, screen_h = screenInfo.current_w, screenInfo.current_h
res_screen_resolution = res_w, res_h = int(screen_w * 0.25), int(screen_h * 0.5)
win_pos_left = 1 + ((screen_w - res_w) // 2)
win_pos_top = 1 + ((screen_h - res_h) // 2)
os.environ['SDL_VIDEO_WINDOW_POS'] = '{},{}'.format(win_pos_left, win_pos_top)  # centra la display
res_screen = pygame.display.set_mode((res_w, res_h), pygame.HWSURFACE | pygame.DOUBLEBUF)

print('res_screen resolution: ' + str(res_screen_resolution))
print('win_pos_left: ' + str(win_pos_left) + '  win_pos_top: ' + str(win_pos_top))

screen_sz = width, height = screenInfo.current_w, screenInfo.current_h

# COLORES
black = 0, 0, 0
white = 255, 255, 255
red = 179, 32, 36
bright_red = 233, 29, 41
cream = 255, 255, 204
green = 18, 230, 3
bright_green = 99, 255, 32
orange = 253, 94, 83
bright_orange = 255, 117, 56
HTML_Gray = 128, 128, 128
HTML_DarkGray = 169, 169, 169
X11_Gray = 190, 190, 190
#############
# FUENTES
freesans = pygame.font.SysFont("freesans", 54)
#############
# BOTONES RESOLUCION
cuatrotres = obj.Boton(HTML_DarkGray, HTML_Gray, 14, 14, res_w // 3.2, res_h // 10.2, func.boton_43, "4:3", True)
dieciseisnueve = obj.Boton(HTML_DarkGray, HTML_Gray, res_w // 3.2 + 16, 14, res_w // 3.2 + 1, res_h // 10.2,
                           func.boton_169, "16:9", True)
dieciseisdiez = obj.Boton(HTML_DarkGray, HTML_Gray, res_w - res_w // 3.2 - 14, 14, res_w // 3.2, res_h // 10.2,
                          func.boton_1610, "16:10", True)
res43_1 = obj.Boton(HTML_DarkGray, HTML_Gray, 14, res_h // 10.2 + 16, res_w - 28,
                    (res_h - res_h // 10.2 - 20) // 11, func.cambio_de_resolucion, "640x480", True, (640, 480),
                    func.change_res)
res43_2 = obj.Boton(HTML_DarkGray, HTML_Gray, 14, res_h // 10.2 * 2 + 8, res_w - 28,
                    (res_h - res_h // 10.2 - 20) // 11, func.cambio_de_resolucion, "800x600", True, (800, 600),
                    func.change_res)
res43_3 = obj.Boton(HTML_DarkGray, HTML_Gray, 14, res_h // 10.2 * 3, res_w - 28,
                    (res_h - res_h // 10.2 - 20) // 11, func.cambio_de_resolucion, "960x720", True, (960, 720),
                    func.change_res)
res43_4 = obj.Boton(HTML_DarkGray, HTML_Gray, 14, res_h // 10.2 * 4 - 8, res_w - 28,
                    (res_h - res_h // 10.2 - 20) // 11, func.cambio_de_resolucion, "1024x768", True, (1024, 768),
                    func.change_res)
res43_5 = obj.Boton(HTML_DarkGray, HTML_Gray, 14, res_h // 10.2 * 5 - 16, res_w - 28,
                    (res_h - res_h // 10.2 - 20) // 11, func.cambio_de_resolucion, "1280x960", True, (1280, 960),
                    func.change_res)
res43_6 = obj.Boton(HTML_DarkGray, HTML_Gray, 14, res_h // 10.2 * 6 - 24, res_w - 28,
                    (res_h - res_h // 10.2 - 20) // 11, func.cambio_de_resolucion, "1400x1050", True, (1400, 1050),
                    func.change_res)
res43_7 = obj.Boton(HTML_DarkGray, HTML_Gray, 14, res_h // 10.2 * 7 - 32, res_w - 28,
                    (res_h - res_h // 10.2 - 20) // 11, func.cambio_de_resolucion, "1440x1080", True, (1440, 1080),
                    func.change_res)
res43_8 = obj.Boton(HTML_DarkGray, HTML_Gray, 14, res_h // 10.2 * 8 - 40, res_w - 28,
                    (res_h - res_h // 10.2 - 20) // 11, func.cambio_de_resolucion, "1600x1200", True, (1600, 1200),
                    func.change_res)
res43_9 = obj.Boton(HTML_DarkGray, HTML_Gray, 14, res_h // 10.2 * 9 - 48, res_w - 28,
                    (res_h - res_h // 10.2 - 20) // 11, func.cambio_de_resolucion, "1856x1392", True, (1856, 1392),
                    func.change_res)
res43_10 = obj.Boton(HTML_DarkGray, HTML_Gray, 14, res_h // 10.2 * 10 - 56, res_w - 28,
                     (res_h - res_h // 10.2 - 20) // 11, func.cambio_de_resolucion, "1920x1440", True, (1920, 1440),
                     func.change_res)
res43_11 = obj.Boton(HTML_DarkGray, HTML_Gray, 14, res_h // 10.2 * 11 - 64, res_w - 28,
                     (res_h - res_h // 10.2 - 20) // 11, func.cambio_de_resolucion, "2048x1536", True, (2048, 1536),
                     func.change_res)
res169_1 = obj.Boton(HTML_DarkGray, HTML_Gray, 14, res_h // 10.2 + 16, res_w - 28,
                     (res_h - res_h // 10.2 - 20) // 11, func.cambio_de_resolucion, "1024x576", True, (1024, 576),
                     func.change_res)
res169_2 = obj.Boton(HTML_DarkGray, HTML_Gray, 14, res_h // 10.2 * 2 + 8, res_w - 28,
                     (res_h - res_h // 10.2 - 20) // 11, func.cambio_de_resolucion, "1152x648", True, (1152, 648),
                     func.change_res)
res169_3 = obj.Boton(HTML_DarkGray, HTML_Gray, 14, res_h // 10.2 * 3, res_w - 28,
                     (res_h - res_h // 10.2 - 20) // 11, func.cambio_de_resolucion, "1280x720", True, (1280, 720),
                     func.change_res)
res169_4 = obj.Boton(HTML_DarkGray, HTML_Gray, 14, res_h // 10.2 * 4 - 8, res_w - 28,
                     (res_h - res_h // 10.2 - 20) // 11, func.cambio_de_resolucion, "1366x768", True, (1366, 768),
                     func.change_res)
res169_5 = obj.Boton(HTML_DarkGray, HTML_Gray, 14, res_h // 10.2 * 5 - 16, res_w - 28,
                     (res_h - res_h // 10.2 - 20) // 11, func.cambio_de_resolucion, "1600x900", True, (1600, 900),
                     func.change_res)
res169_6 = obj.Boton(HTML_DarkGray, HTML_Gray, 14, res_h // 10.2 * 6 - 24, res_w - 28,
                     (res_h - res_h // 10.2 - 20) // 11, func.cambio_de_resolucion, "1920x1080", True, (1920, 1080),
                     func.change_res)
res169_7 = obj.Boton(HTML_DarkGray, HTML_Gray, 14, res_h // 10.2 * 7 - 32, res_w - 28,
                     (res_h - res_h // 10.2 - 20) // 11, func.cambio_de_resolucion, "2560x1440", True, (2560, 1440),
                     func.change_res)
res169_8 = obj.Boton(HTML_DarkGray, HTML_Gray, 14, res_h // 10.2 * 8 - 40, res_w - 28,
                     (res_h - res_h // 10.2 - 20) // 11, func.cambio_de_resolucion, "3840x2160", True, (3840, 2160),
                     func.change_res)
res1610_1 = obj.Boton(HTML_DarkGray, HTML_Gray, 14, res_h // 10.2 + 16, res_w - 28,
                      (res_h - res_h // 10.2 - 20) // 11, func.cambio_de_resolucion, "1280x800", True, (1280, 800),
                      func.change_res)
res1610_2 = obj.Boton(HTML_DarkGray, HTML_Gray, 14, res_h // 10.2 * 2 + 8, res_w - 28,
                      (res_h - res_h // 10.2 - 20) // 11, func.cambio_de_resolucion, "1440x900", True, (1440, 900),
                      func.change_res)
res1610_3 = obj.Boton(HTML_DarkGray, HTML_Gray, 14, res_h // 10.2 * 3, res_w - 28,
                      (res_h - res_h // 10.2 - 20) // 11, func.cambio_de_resolucion, "1680x1050", True, (1680, 1050),
                      func.change_res)
res1610_4 = obj.Boton(HTML_DarkGray, HTML_Gray, 14, res_h // 10.2 * 4 - 8, res_w - 28,
                      (res_h - res_h // 10.2 - 20) // 11, func.cambio_de_resolucion, "1920x1200", True, (1920, 1200),
                      func.change_res)
res1610_5 = obj.Boton(HTML_DarkGray, HTML_Gray, 14, res_h // 10.2 * 5 - 16, res_w - 28,
                      (res_h - res_h // 10.2 - 20) // 11, func.cambio_de_resolucion, "2560x1600", True, (2560, 1600),
                      func.change_res)
#############
# resolucion
menu_res = 0
while True:
    clock.tick(60)  # 60 FPS
    res_screen.fill(X11_Gray)
    posicion_mouse = pygame.mouse.get_pos()
    if menu_res == "end":  # cambia la resolucion y rompe el ciclo
        screen_sz = width, height = func.screen_sz
        break
    elif menu_res == 0:
        botones = [cuatrotres, dieciseisnueve, dieciseisdiez, res43_1, res43_2, res43_3, res43_4, res43_5, res43_6,
                   res43_7, res43_8, res43_9, res43_10, res43_11]
    elif menu_res == 1:
        botones = [cuatrotres, dieciseisnueve, dieciseisdiez, res169_1, res169_2, res169_3, res169_4, res169_5,
                   res169_6, res169_7, res169_8]
    elif menu_res == 2:
        botones = [cuatrotres, dieciseisnueve, dieciseisdiez, res1610_1, res1610_2, res1610_3, res1610_4, res1610_5]
    for boton in botones:
        if boton.hover(posicion_mouse):
            boton.dibujar(res_screen, 0)
        else:
            boton.dibujar(res_screen)
        if boton.id == 1:
            boton.mostrar_texto(res_screen)
    for event in pygame.event.get():  # comienza deteccion de eventos
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] == 1:  # click izquierdo
                for boton in botones:
                    if boton.hover(posicion_mouse):
                        resultado = boton.ejecutar()
                        if resultado is not None:
                            menu_res = resultado
                    else:
                        boton.reset_color()
    pygame.display.flip()
#############
# BOTONES JUEGO
cerrar = obj.Boton(red, bright_red, *func.res_scaling(screen_sz, (2400, 1080), (500, 140)), quit, "Exit")
comenzar = obj.Boton(green, bright_green, *func.res_scaling(screen_sz, (960, 1080), (500, 140)), func.boton_comenzar, "Comenzar")
pausar = obj.Boton(orange, bright_orange, *func.res_scaling(screen_sz, (2400, 260), (300, 140)), func.boton_pausa, "Pausa")
despausar = obj.Boton(orange, bright_orange, *func.res_scaling(screen_sz, (2400, 410), (300, 140)), func.boton_despausa, "Despausa")
boton_menu = obj.Boton(green, bright_green, *func.res_scaling(screen_sz, (2400, 260), (300, 140)), func.boton_menu, "Menu")
#############
# CUADROS
main_cuadro = obj.Cuadro(("Matias", black), *func.res_scaling(screen_sz, (480, 1800), (2880, 360)), cream)
#############
win_pos_left = 1 + ((screenInfo.current_w - width) // 2)
win_pos_top = 1 + ((screenInfo.current_h - height) // 2)
os.environ['SDL_VIDEO_WINDOW_POS'] = '{},{}'.format(win_pos_left, win_pos_top)  # centra el objeto screen
screen = pygame.display.set_mode(screen_sz, pygame.HWSURFACE | pygame.DOUBLEBUF)
fps_counter = obj.Texto(clock.get_fps(), freesans, black)
menus = 0  # especifica el menu
#      0           1          2
# [main_menu, pause_menu, play_menu]

# MAIN LOOP
while True:
    clock.tick(60)  # 60 FPS
    screen.fill(white)
    fps_counter.update(str(int(clock.get_fps())))
    screen.blit(fps_counter.texto, (1, 1))  # contador de fps
    posicion_mouse = pygame.mouse.get_pos()
    if menus == 0:
        botones = [cerrar, comenzar]
        cuadros = []
    elif menus == 1:
        botones = [cerrar, despausar, boton_menu]
        cuadros = []
    elif menus == 2:
        botones = [cerrar, pausar]
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
