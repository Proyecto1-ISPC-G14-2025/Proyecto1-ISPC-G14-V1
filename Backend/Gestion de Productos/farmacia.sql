CREATE DATABASE IF NOT EXISTS farmacia;
USE farmacia;

CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE proveedores (
    id_proveedor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(100)
);

CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    id_tipo_producto INT,
    id_proveedor INT,
    stock INT DEFAULT 0,
    FOREIGN KEY (id_tipo_producto) REFERENCES categorias(id_categoria) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (id_proveedor) REFERENCES proveedores(id_proveedor) ON DELETE SET NULL ON UPDATE CASCADE
);

INSERT INTO categorias (nombre) VALUES ('Medicamentos'), ('Cuidado Personal'), ('Vitaminas'), ('Equipamiento Médico');

INSERT INTO proveedores (nombre, telefono, email) VALUES 
('Proveedor A', '1234567890', 'contacto@proveedora.com'),
('Proveedor B', '0987654321', 'ventas@proveedorb.com');

INSERT INTO productos (nombre, descripcion, precio, id_tipo_producto, id_proveedor, stock) VALUES
('Paracetamol', 'Analgésico y antipirético', 150.00, 1, 1, 50),
('Ibuprofeno', 'Analgésico antiinflamatorio', 200.00, 1, 1, 30),
('Crema Antiséptica', 'Cuidado de heridas', 80.00, 2, 2, 40),
('Multivitaminas', 'Suplemento vitamínico', 350.00, 3, 1, 20),
('Termómetro Digital', 'Medición de temperatura', 1200.00, 4, 2, 10);
