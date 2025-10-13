-- Crear base de datos
CREATE DATABASE IF NOT EXISTS farmastock CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE farmastock;

-- Crear tabla usuarios
CREATE TABLE IF NOT EXISTS usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  rol ENUM('admin','user') NOT NULL DEFAULT 'user',
  creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar 20 registros de usuarios de ejemplo
INSERT INTO usuarios (nombre, email, password, rol) VALUES
('Admin Principal', 'admin1@farmastock.com', 'admin123', 'admin'),
('Usuario Normal 1', 'user1@farmastock.com', 'user123', 'user'),
('Usuario Normal 2', 'user2@farmastock.com', 'user123', 'user'),
('Usuario Normal 3', 'user3@farmastock.com', 'user123', 'user'),
('Usuario Normal 4', 'user4@farmastock.com', 'user123', 'user'),
('Usuario Normal 5', 'user5@farmastock.com', 'user123', 'user'),
('Usuario Normal 6', 'user6@farmastock.com', 'user123', 'user'),
('Usuario Normal 7', 'user7@farmastock.com', 'user123', 'user'),
('Usuario Normal 8', 'user8@farmastock.com', 'user123', 'user'),
('Usuario Normal 9', 'user9@farmastock.com', 'user123', 'user'),
('Admin Secundario', 'admin2@farmastock.com', 'admin123', 'admin'),
('Usuario Normal 10', 'user10@farmastock.com', 'user123', 'user'),
('Usuario Normal 11', 'user11@farmastock.com', 'user123', 'user'),
('Usuario Normal 12', 'user12@farmastock.com', 'user123', 'user'),
('Usuario Normal 13', 'user13@farmastock.com', 'user123', 'user'),
('Usuario Normal 14', 'user14@farmastock.com', 'user123', 'user'),
('Usuario Normal 15', 'user15@farmastock.com', 'user123', 'user'),
('Usuario Normal 16', 'user16@farmastock.com', 'user123', 'user'),
('Usuario Normal 17', 'user17@farmastock.com', 'user123', 'user'),
('Usuario Normal 18', 'user18@farmastock.com', 'user123', 'user');
