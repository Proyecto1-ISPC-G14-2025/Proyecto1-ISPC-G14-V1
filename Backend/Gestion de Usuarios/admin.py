# admin.py
from db import Database
#definicion de clase Admin para acciones de gestion de usuarios

class Admin:
    def __init__(self, username):
        self.username = username

    def listar_usuarios(self):
        db = Database()
        db.connect()
        query = "SELECT username, nombre, email, role FROM usuarios"
        db.execute(query)
        usuarios = db.fetchall()
        db.close()
        return usuarios

    def cambiar_rol(self, username, nuevo_rol):
        db = Database()
        db.connect()
        query = "UPDATE usuarios SET role=%s WHERE username=%s"
        db.execute(query, (nuevo_rol, username))
        db.commit()
        db.close()

    def eliminar_usuario(self, username):
        db = Database()
        db.connect()
        query = "DELETE FROM usuarios WHERE username=%s"
        db.execute(query, (username,))
        db.commit()
        db.close()
