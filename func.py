from decimal import Decimal


def res_scaling(screen_res, object_position, object_area):  # falta ajustar esta funcion a imagenes
    target_width, target_height = screen_res[0], screen_res[1]
    object_x, object_y = object_position[0], object_position[1]
    object_width, object_height = object_area[0], object_area[1]
    base_width, base_height = 3840, 2160
    x_ratio, y_ratio = round(Decimal(target_width / base_width), 2), round(Decimal(target_height / base_height), 2)
    new_x, new_y = int(object_x * x_ratio), int(object_y * y_ratio)
    new_width, new_height = int(object_width * x_ratio), int(object_height * y_ratio)
    return new_x, new_y, new_width, new_height


def change_res(width, height):
    global screen_sz
    screen_sz = width, height


def boton_comenzar():
    return 2


def boton_pausa():
    return 1


def boton_despausa():
    return 2


def boton_menu():
    return 0


def boton_43():
    return 0


def boton_169():
    return 1


def boton_1610():
    return 2


def cambio_de_resolucion():
    return "end"
