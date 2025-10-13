-- Usar base de datos farmastock (crearla antes si no existe)
CREATE DATABASE IF NOT EXISTS farmastock CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE farmastock;

-- Crear tabla medicamentos con campo precio y proveedor
CREATE TABLE IF NOT EXISTS medicamentos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  lote VARCHAR(50) NOT NULL,
  cantidad INT UNSIGNED NOT NULL,
  fecha_expiracion DATE NOT NULL,
  descripcion TEXT,
  precio DECIMAL(10,2) NOT NULL DEFAULT 0.00,
  proveedor VARCHAR(100) NOT NULL,
  creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar 20 registros de ejemplo
INSERT INTO medicamentos (nombre, lote, cantidad, fecha_expiracion, descripcion, precio, proveedor) VALUES
('Paracetamol', 'A1234', 50, '2025-12-31', 'Analgésico y antipirético común', 200.50, 'Proveedor A'),
('Ibuprofeno', 'B5678', 30, '2024-10-20', 'Antiinflamatorio no esteroideo', 150.75, 'Proveedor B'),
('Amoxicilina', 'C9012', 100, '2026-05-15', 'Antibiótico de amplio espectro', 350.00, 'Proveedor C'),
('Loratadina', 'D3456', 75, '2025-08-10', 'Antihistamínico para alergias', 180.25, 'Proveedor D'),
('Omeprazol', 'E7890', 40, '2024-12-05', 'Inhibidor de bomba de protones', 220.00, 'Proveedor E'),
('Metformina', 'F2345', 120, '2026-03-25', 'Tratamiento para diabetes tipo 2', 360.40, 'Proveedor F'),
('Simvastatina', 'G6789', 60, '2025-07-20', 'Reductor de colesterol', 275.60, 'Proveedor G'),
('Aspirina', 'H0123', 80, '2025-09-30', 'Analgésico y antiinflamatorio', 130.00, 'Proveedor H'),
('Clorfenamina', 'I4567', 35, '2024-11-22', 'Medicamento para alergias', 120.50, 'Proveedor I'),
('Dextrometorfano', 'J8910', 55, '2025-04-01', 'Supresor de la tos', 160.75, 'Proveedor J'),
('Fenitoína', 'K1357', 28, '2025-06-18', 'Tratamiento para epilepsia', 400.00, 'Proveedor K'),
('Prednisona', 'L2468', 90, '2026-01-30', 'Corticosteroide antiinflamatorio', 310.00, 'Proveedor L'),
('Cephalexina', 'M3579', 110, '2025-10-11', 'Antibiótico para infecciones bacterianas', 350.50, 'Proveedor M'),
('Clonazepam', 'N4680', 25, '2025-05-05', 'Ansiolítico anticonvulsivante', 290.30, 'Proveedor N'),
('Diclofenaco', 'O5791', 70, '2025-03-27', 'Antiinflamatorio no esteroideo', 180.00, 'Proveedor O'),
('Levotiroxina', 'P6802', 95, '2026-08-15', 'Tratamiento para hipotiroidismo', 425.00, 'Proveedor P'),
('Salbutamol', 'Q7913', 50, '2025-02-14', 'Broncodilatador para asma', 260.00, 'Proveedor Q'),
('Naproxeno', 'R8024', 45, '2025-06-23', 'Antiinflamatorio no esteroideo', 175.00, 'Proveedor R'),
('Cetirizina', 'S9135', 65, '2026-04-29', 'Antihistamínico', 140.00, 'Proveedor S'),
('Ranitidina', 'T0246', 33, '2024-09-19', 'Tratamiento para úlceras gástricas', 230.00, 'Proveedor T');
