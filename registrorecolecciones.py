def registrar_recolecciones():

    recolecciones = {
        "PET": [],
        "CARTON": [],
        "VIDRIO": [],
        "METAL": []
    }

    for material in recolecciones:
        print("\nIngrese 20 mediciones para", material)

        contador = 0

        while contador < 20:

            dato = input("Medicion en kg: ")

            # Validar que no esté vacío
            if dato == "":
                print("❌ No puede dejar el campo vacío")
                continue

            # Validar que sea número
            if dato.replace(".", "").isdigit():
                kg = float(dato)
                recolecciones[material].append(kg)
                contador += 1
            else:
                print("❌ Solo se permiten números")

    return recolecciones
