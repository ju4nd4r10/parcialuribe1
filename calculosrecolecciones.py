def calcular_promedios(recolecciones):

    promedios = {}
    suma_global = 0
    total_mediciones = 0

    for material in recolecciones:
        suma = sum(recolecciones[material])
        promedio = suma / len(recolecciones[material])

        promedios[material] = promedio

        suma_global += suma
        total_mediciones += len(recolecciones[material])

    promedio_global = suma_global / total_mediciones

    return promedios, promedio_global
