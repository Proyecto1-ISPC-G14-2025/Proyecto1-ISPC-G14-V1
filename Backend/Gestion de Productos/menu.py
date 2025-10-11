# menu.py
from producto import Producto

def input_entero(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"Debe ingresar un número mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número entero.")

def input_decimal(mensaje, minimo=None):
    while True:
        try:
            valor = float(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"Debe ingresar un número mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número válido.")

def mostrar_menu():
    print("\n--- Menú Productos ---")
    print("1. Listar productos")
    print("2. Listar productos con detalles (JOIN)")
    print("3. Agregar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("0. Salir")

def ejecutar_opcion():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            productos = Producto().listar()
            if productos:
                for p in productos:
                    print(f"ID: {p.id_producto} | Nombre: {p.nombre} | Precio: {p.precio} | Stock: {p.stock}")
            else:
                print("No hay productos para mostrar.")
        elif opcion == '2':
            productos = Producto.listar_con_detalles()
            if productos:
                for p in productos:
                    print(f"ID: {p[0]} | Nombre: {p[1]} | Categoría: {p[5]} | Proveedor: {p[6]} | Precio: {p[3]} | Stock: {p[4]}")
            else:
                print("No hay productos con detalles para mostrar.")
        elif opcion == '3':
            nombre = input("Nombre: ").strip()
            descripcion = input("Descripción: ").strip()
            precio = input_decimal("Precio: ", minimo=0)
            stock = input_entero("Stock: ", minimo=0)
            id_tipo_producto = input_entero("ID Categoría: ", minimo=1)
            id_tipo_producto = input_entero("ID Tipo Producto: ", minimo=1)
            id_proveedor = input_entero("ID Proveedor: ", minimo=1)
            producto = Producto(nombre=nombre, descripcion=descripcion, precio=precio, stock=stock, id_tipo_producto=id_tipo_producto, id_proveedor=id_proveedor)
            producto.agregar()
        elif opcion == '4':
            id_producto = input_entero("ID producto a actualizar: ", minimo=1)
            nombre = input("Nuevo nombre: ").strip()
            descripcion = input("Nueva descripción: ").strip()
            precio = input_decimal("Nuevo precio: ", minimo=0)
            stock = input_entero("Nuevo stock: ", minimo=0)
            id_tipo_producto = input_entero("Nuevo ID Categoría: ", minimo=1)
            id_proveedor = input_entero("Nuevo ID Proveedor: ", minimo=1)
            producto = Producto(id_producto=id_producto, nombre=nombre, descripcion=descripcion,
                                precio=precio, stock=stock, id_tipo_producto=id_tipo_producto, id_proveedor=id_proveedor)
            producto.actualizar()
        elif opcion == '5':
            id_producto = input_entero("ID producto a eliminar: ", minimo=1)
            producto = Producto(id_producto=id_producto)
            producto.eliminar()
        elif opcion == '0':
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
