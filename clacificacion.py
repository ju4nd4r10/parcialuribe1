def clasificar_material(promedio):
    if promedio < 8:
        return "Bajo"
    elif promedio <= 15:
        return "Estable"
    else:
        return "Alto"


def clasificar_global(promedio):
    if promedio < 10:
        return "Alerta"
    elif promedio < 15:
        return "Operacion normal"
    else:
        return "Jornada sobresaliente"
