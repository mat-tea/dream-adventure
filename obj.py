import pygame  # borrar al compilar


pygame.font.init()  # borrar al compilar
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


class Texto:  # texto general
    def __init__(self, string, font, color):
        self.string = str(string)
        self.font = font
        self.color = color
        self.texto = font.render(self.string, True, color)
        self.width = self.texto.get_width()
        self.height = self.texto.get_height()

    def update(self, string):
        self.string = str(string)
        self.texto = self.font.render(self.string, True, self.color)


class Boton:  # FALTA OPTIMIZAR CON MASK PARA BOTONES NO RECTANGULARES Y CUSTOMIZADOS
    def __init__(self, color1, color2, x, y, width, height, accion, texto=""):
        if texto != "":  # se revisa si el boton tiene texto
            self.id = 1
            self.texto = Texto(str(texto), freesans, black)
        else:
            self.id = 0
        self.color = color1
        self.color1 = color1
        self.color2 = color2
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.accion = accion
        self.superficie = (x, x + width), (y, y + height)

    def mostrar_texto(self, display):  # muestra el texto del boton
        display.blit(self.texto.texto, (self.x + self.width // 4, self.y + self.height // 4))

    def hover(self, posicion):  # revisa si el mouse esta sobre el boton
        hover = False
        if self.superficie[0][0] <= posicion[0] <= self.superficie[0][1]:
            if self.superficie[1][0] <= posicion[1] <= self.superficie[1][1]:
                hover = True
        return hover

    def dibujar(self, display, hover=None):  # dibuja el boton sobre el display
        if hover is not None:
            self.color = self.color2
        else:
            self.color = self.color1
        pygame.draw.rect(display, self.color, [self.x, self.y, self.width, self.height])

    def ejecutar(self):  # para hacer funcionar al boton
        return self.accion()


class Cuadro:
    def __init__(self, titulo, screen_size, color):
        self.guion = 0  # contador para ver en que linea del guion va, cada vez que se actualiza el texto, se le suma 1
        self.color = color  # cont^: cada vez que el texto es actualizado
        self.width = screen_size[0] * 11 // 12
        self.height = screen_size[1] // 3.2
        self.superficie = self.x, self.y = 0, screen_size[1] - self.height
        self.texto = Texto("", freesans, black)
        self.titulo = Texto(titulo[0], freesans, titulo[1])

    def actualizar_texto(self, archivo="guion.txt"):  # cambia el texto del cuadro al siguiente
        with open(archivo, "r") as guion:
            for i, linea in enumerate(guion):
                if i == self.guion:
                    string = linea.rstrip()
                    try:
                        titulo_dialogo, linea_dialogo = string.split(": ", 1)
                    except ValueError as error:
                        print(error, ": No hay titulo de dialogo.")
                        titulo_dialogo, linea_dialogo = "", string
                    break
        try:
            self.texto.update(linea_dialogo)
            self.titulo.update(titulo_dialogo)
            self.guion += 1
        except UnboundLocalError as error:
            print(error, ": Se ha llegado a la ultima linea de", archivo + ": ", str(self.guion))

    def dibujar(self, display):  # dibuja el cuadro sobre el display
        pygame.draw.rect(display, self.color, [self.x, self.y, self.width, self.height])
        display.blit(self.titulo.texto, (self.x + self.width // 48, self.y + self.height // 8))
        display.blit(self.texto.texto, (self.x + self.width // 48, self.y + 2 * self.height // 8))
