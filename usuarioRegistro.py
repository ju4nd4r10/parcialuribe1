
usuarios = []

def registrar_usuarios():
    for i in range(5):
        print("\nRegistro Gestor Ambiental ", i+1)
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        password = input("Password: ")
        empresa = input("Empresa: ")
        rol = input("Rol: ")

        usuario = {
            "nombre": nombre,
            "correo": correo,
            "password": password,
            "empresa": empresa,
            "rol": rol
        }

        usuarios.append(usuario)

    return usuarios
