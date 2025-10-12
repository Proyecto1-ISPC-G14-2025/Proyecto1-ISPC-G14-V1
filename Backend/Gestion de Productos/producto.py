from db import conectar, desconectar

class Producto:
    def __init__(self, id_producto=None, nombre=None, descripcion=None, precio=None, stock=None, id_tipo_producto=None, id_proveedor=None):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.id_tipo_producto = id_tipo_producto
        self.id_proveedor = id_proveedor

    def validar_datos(self):
        errores = []
        if not self.nombre or not self.nombre.strip():
            errores.append("El nombre no puede estar vacío.")
        if self.precio is None or self.precio < 0:
            errores.append("El precio debe ser mayor o igual a 0.")
        if self.stock is None or self.stock < 0:
            errores.append("El stock debe ser mayor o igual a 0.")
        if self.id_tipo_producto is None or self.id_tipo_producto <= 0:
            errores.append("La categoría debe ser un número entero positivo.")
        if self.id_proveedor is None or self.id_proveedor <= 0:
            errores.append("El proveedor debe ser un número entero positivo.")
        return errores

    def agregar(self):
        errores = self.validar_datos()
        if errores:
            print("Errores en los datos:")
            for e in errores:
                print(f"- {e}")
            return
        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                sql = ("INSERT INTO productos (nombre, descripcion, precio, stock, id_tipo_producto, id_proveedor) "
                        "VALUES (%s, %s, %s, %s, %s, %s)")
                datos = (
                    self.nombre.strip(),
                    self.descripcion.strip() if self.descripcion else '',
                    self.precio,
                    self.stock,
                    self.id_tipo_producto,
                    self.id_proveedor
                )
                cursor.execute(sql, datos)
                conexion.commit()
                print(f"Producto '{self.nombre}' agregado correctamente.")
            except Exception as e:
                print(f"Error al agregar producto: {e}")
            finally:
                cursor.close()
                desconectar(conexion)

    def listar(self):
        conexion = conectar()
        productos = []
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT id_producto, nombre, descripcion, precio, stock, id_tipo_producto, id_proveedor FROM productos")
                filas = cursor.fetchall()
                for fila in filas:
                    p = Producto(*fila)
                    productos.append(p)
            except Exception as e:
                print(f"Error al listar productos: {e}")
            finally:
                cursor.close()
                desconectar(conexion)
        return productos

    def actualizar(self):
        if self.id_producto is None or not isinstance(self.id_producto, int) or self.id_producto <= 0:
            print("Error: El ID del producto debe ser un entero positivo para actualizar.")
            return
        errores = self.validar_datos()
        if errores:
            print("Errores en los datos:")
            for e in errores:
                print(f"- {e}")
            return
        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                sql = ("UPDATE productos SET nombre=%s, descripcion=%s, precio=%s, stock=%s, id_tipo_producto=%s, id_proveedor=%s "
                        "WHERE id_producto=%s")
                datos = (
                    self.nombre.strip(),
                    self.descripcion.strip() if self.descripcion else '',
                    self.precio,
                    self.stock,
                    self.id_tipo_producto,
                    self.id_proveedor,
                    self.id_producto
                )
                cursor.execute(sql, datos)
                conexion.commit()
                if cursor.rowcount == 0:
                    print(f"No se encontró producto con ID {self.id_producto}.")
                else:
                    print(f"Producto ID {self.id_producto} actualizado correctamente.")
            except Exception as e:
                print(f"Error al actualizar producto: {e}")
            finally:
                cursor.close()
                desconectar(conexion)

    def eliminar(self):
        if self.id_producto is None or not isinstance(self.id_producto, int) or self.id_producto <= 0:
            print("Error: El ID del producto debe ser un entero positivo para eliminar.")
            return
        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                sql = "DELETE FROM productos WHERE id_producto=%s"
                cursor.execute(sql, (self.id_producto,))
                conexion.commit()
                if cursor.rowcount == 0:
                    print(f"No se encontró producto con ID {self.id_producto}.")
                else:
                    print(f"Producto ID {self.id_producto} eliminado correctamente.")
            except Exception as e:
                print(f"Error al eliminar producto: {e}")
            finally:
                cursor.close()
                desconectar(conexion)

    @staticmethod
    def listar_con_detalles():
        conexion = conectar()
        productos = []
        if conexion:
            try:
                cursor = conexion.cursor()
                sql = """
                    SELECT p.id_producto, p.nombre, p.descripcion, p.precio, p.stock,
                            c.nombre AS categoria, pr.nombre AS proveedor
                    FROM productos p
                    LEFT JOIN categorias c ON p.id_tipo_producto = c.id_categoria
                    LEFT JOIN proveedores pr ON p.id_proveedor = pr.id_proveedor
                """
                cursor.execute(sql)
                productos = cursor.fetchall()
            except Exception as e:
                print(f"Error en la consulta con JOIN: {e}")
            finally:
                cursor.close()
                desconectar(conexion)
        return productos
