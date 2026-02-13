from usuarioRegistro import registrar_usuarios
from usuarioAuntenticar import login
from registrorecolecciones import registrar_recolecciones
from calculosrecolecciones import calcular_promedios
from clacificacion import clasificar_material, clasificar_global

print("=== SISTEMA MEDELLIN RECICLA ===")

# Registrar usuarios
usuarios = registrar_usuarios()

# Login
if login(usuarios):

    recolecciones = registrar_recolecciones()

    promedios, promedio_global = calcular_promedios(recolecciones)

    print("\n----- RESULTADOS -----")

    for material in promedios:
        print("\nMaterial:", material)
        print("Promedio:", round(promedios[material], 2), "kg")
        print("Clasificacion:", clasificar_material(promedios[material]))

    print("\nPromedio Global:", round(promedio_global, 2), "kg")
    print("Clasificacion Global:", clasificar_global(promedio_global))
