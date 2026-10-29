SET NAMES utf8mb4;

USE colegio;
CREATE TABLE IF NOT EXISTS estudiantes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  correo VARCHAR(150) NOT NULL,
  carrera VARCHAR(100) NOT NULL
);
INSERT INTO estudiantes (nombre, correo, carrera) VALUES
('Ana Pérez', 'ana@ejemplo.cl', 'Ingeniería'),
('Luis Soto', 'luis@ejemplo.cl', 'Informática'),
('María Díaz', 'maria@ejemplo.cl', 'Administración');
