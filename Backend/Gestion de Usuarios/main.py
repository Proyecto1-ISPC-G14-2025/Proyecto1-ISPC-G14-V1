# main.py
# Script principal para interacción en consola
# acciones principales

from user import Usuario
from admin import Admin


def menu_usuario(usuario):
    while True:
        print(f"\nBienvenido {usuario.nombre or usuario.username} - Rol: {usuario.role}")
        print("1. Ver y editar datos personales")
        print("2. Cerrar sesión")
        opcion = input("Elija una opción: ")
        if opcion == '1':
            print(f"Nombre actual: {usuario.nombre}")
            print(f"Email actual: {usuario.email}")
            nombre = input("Nuevo nombre (enter para no cambiar): ")
            email = input("Nuevo email (enter para no cambiar): ")
            if nombre.strip() == "":
                nombre = usuario.nombre
            if email.strip() == "":
                email = usuario.email
            usuario.update_personal_info(nombre, email)
            print("Datos actualizados.")
        elif opcion == '2':
            break
        else:
            print("Opción inválida.")

def menu_admin(admin):
    while True:
        print("\nPanel Admin")
        print("1. Listar usuarios")
        print("2. Cambiar rol usuario")
        print("3. Eliminar usuario")
        print("4. Cerrar sesión")
        opcion = input("Elija una opción: ")
        if opcion == '1':
            usuarios = admin.listar_usuarios()
            print("\nUsuarios registrados:")
            for u in usuarios:
                print(f"{u['username']} | {u['nombre']} | {u['email']} | {u['role']}")
        elif opcion == '2':
            user = input("Ingrese el username a cambiar rol: ")
            rol = input("Nuevo rol (user/admin): ")
            if rol not in ['user', 'admin']:
                print("Rol inválido.")
                continue
            admin.cambiar_rol(user, rol)
            print("Rol actualizado.")
        elif opcion == '3':
            user = input("Ingrese username a eliminar: ")
            admin.eliminar_usuario(user)
            print("Usuario eliminado.")
        elif opcion == '4':
            break
        else:
            print("Opción inválida.")

def registrar():
    print("\nRegistro de usuario")
    username = input("Username: ")
    password = input("Password: ")
    nombre = input("Nombre: ")
    email = input("Email: ")
    user = Usuario(username, password, nombre, email)
    try:
        user.save()
        print("Registro exitoso.")
    except Exception as e:
        print("Error al registrar, posible username repetido.")

def login():
    print("\nInicio de sesión")
    username = input("Username: ")
    password = input("Password: ")
    user = Usuario.login(username, password)
    if user:
        print("Login exitoso.")
        if user.role == 'admin':
            admin = Admin(user.username)
            menu_admin(admin)
        else:
            menu_usuario(user)
    else:
        print("Credenciales inválidas.")

def main():
    while True:
        print("\nSistema de Gestión de Usuarios")
        print("1. Registro")
        print("2. Login")
        print("3. Salir")
        opcion = input("Elija una opción: ")
        if opcion == '1':
            registrar()
        elif opcion == '2':
            login()
        elif opcion == '3':
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
