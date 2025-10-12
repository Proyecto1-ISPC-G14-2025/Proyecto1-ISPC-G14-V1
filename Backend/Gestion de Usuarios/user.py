# user.py
# Clase Usuario con registro, login, edición datos personales
#usuarios de prueba admin /admin123 y hellraiser/hell22


from db import Database
import hashlib

class Usuario:
    def __init__(self, username, password, nombre="", email="", role="user"):
        self.username = username
        self.password = password  # plain text, se almacenará hash
        self.nombre = nombre
        self.email = email
        self.role = role  # 'user' o 'admin'
    
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def save(self):
        db = Database()
        try:
            db.connect()
            hashed = self.hash_password(self.password)
            query = ("INSERT INTO usuarios (username, password, nombre, email, role) "
                     "VALUES (%s, %s, %s, %s, %s)")
            params = (self.username, hashed, self.nombre, self.email, self.role)
            db.execute(query, params)
            db.conn.commit()  # confirmar cambios en la base
        except Exception as e:
            print(f"Error en save(): {e}")
            raise e
        finally:
            db.close()
        
        
    @staticmethod
    def login(username, password):
        db = Database()
        db.connect()
        hashed = hashlib.sha256(password.encode()).hexdigest()
        query = "SELECT * FROM usuarios WHERE username=%s AND password=%s"
        db.execute(query, (username, hashed))
        user_data = db.fetchone()
        db.close()
        if user_data:
            return Usuario(
                username=user_data['username'],
                password="",  # no se guarda plano
                nombre=user_data['nombre'],
                email=user_data['email'],
                role=user_data['role']
            )
        else:
            return None
    
    def update_personal_info(self, nombre, email):
        db = Database()
        db.connect()
        query = "UPDATE usuarios SET nombre=%s, email=%s WHERE username=%s"
        db.execute(query, (nombre, email, self.username))
        db.close()
        self.nombre = nombre
        self.email = email
