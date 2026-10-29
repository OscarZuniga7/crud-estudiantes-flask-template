# CRUD estudiantes — GitHub Codespaces

Proyecto didáctico: MySQL 8.4 + phpMyAdmin + Flask + Bootstrap.

## Inicio rápido

1. Sube los archivos (incluida la carpeta `.devcontainer`) a un repositorio GitHub.
2. Abre **Code > Codespaces > Create codespace on main**.
3. En la terminal: `cp .env.example .env` y edita `.env` para sustituir las contraseñas.
4. Ejecuta `docker compose up --build -d`.
5. Abre la pestaña **Ports**: 8081 (Flask) y 8090 (phpMyAdmin). Conservar ambos en **Private**.
6. En phpMyAdmin usa `alumno` y la contraseña `MYSQL_PASSWORD` de `.env`.

## Conceptos SQL

- CREATE: `INSERT INTO estudiantes (nombre, correo, carrera) VALUES (...)`
- READ: `SELECT * FROM estudiantes`
- UPDATE: `UPDATE estudiantes SET ... WHERE id = ...`
- DELETE: `DELETE FROM estudiantes WHERE id = ...`

## Comandos

- Ver estado: `docker compose ps`
- Ver errores: `docker compose logs -f web`
- Detener: `docker compose down`
- **Borrar todos los datos y reinicializar:** `docker compose down -v` (destructivo).

## Seguridad

Esta es una aplicación didáctica. No dispone de login ni protección CSRF. Usa datos ficticios y no hagas públicos los puertos. Nunca subas `.env` al repositorio. El volumen MySQL conserva los datos: cambiar `.env` tras la primera inicialización no actualiza las contraseñas internas.
