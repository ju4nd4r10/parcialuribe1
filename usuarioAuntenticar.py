def login(usuarios):
    intentos = 0

    while intentos < 3:
        correo = input("\nIngrese correo: ")
        password = input("Ingrese password: ")

        for usuario in usuarios:
            if usuario["correo"] == correo and usuario["password"] == password:
                print("✅ Bienvenido", usuario["nombre"])
                return True

        intentos += 1
        print("❌ Datos incorrectos. Intento", intentos)

    print("⛔ Acceso bloqueado")
    return False
