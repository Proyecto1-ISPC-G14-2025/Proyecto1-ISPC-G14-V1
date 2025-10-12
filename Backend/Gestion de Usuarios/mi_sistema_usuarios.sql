--
-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS `mi_sistema_usuarios` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- Seleccionar la base de datos
USE `mi_sistema_usuarios`;

-- Crear la tabla usuarios (asumiendo las columnas y tipos)
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(50) NOT NULL,
  `password` CHAR(64) NOT NULL,
  `nombre` VARCHAR(100) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `role` ENUM('admin', 'user') NOT NULL DEFAULT 'user',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username_UNIQUE` (`username`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Insertar datos en la tabla usuarios
INSERT INTO `usuarios` (`username`, `password`, `nombre`, `email`, `role`) VALUES
('admin', '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9', 'Administrador', 'admin@example.com', 'admin'),
('Fabio', 'd01167afa273b0424e4471bdeffc0dc95b7f0ad831aa1dd0f6b1bc627f5b3cee', 'Fabio D', 'fabiod@example.com', 'user'),
('Juanito', 'cb54f49a4ad4135c3272479b147b4786a873a5a436912714370b6a1941514315', 'Juanito Perez', 'jperez@example.com', 'user');
