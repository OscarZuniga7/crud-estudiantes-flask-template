import os
from flask import Flask, flash, redirect, render_template, request, url_for
import pymysql

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]


def conectar():
    return pymysql.connect(
        host=os.environ.get("DB_HOST", "mysql"),
        user=os.environ.get("DB_USER", "alumno"),
        password=os.environ["DB_PASSWORD"],
        database=os.environ.get("DB_NAME", "colegio"),
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True,
    )


@app.get("/")
def inicio():
    with conectar() as db:
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM estudiantes ORDER BY id")
            estudiantes = cursor.fetchall()
    return render_template("index.html", estudiantes=estudiantes)


@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        correo = request.form.get("correo", "").strip()
        carrera = request.form.get("carrera", "").strip()
        if not all([nombre, correo, carrera]):
            flash("Completa los tres campos.", "warning")
        else:
            with conectar() as db:
                with db.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO estudiantes (nombre, correo, carrera) VALUES (%s, %s, %s)",
                        (nombre, correo, carrera),
                    )
            flash("Estudiante agregado correctamente.", "success")
            return redirect(url_for("inicio"))
    return render_template("formulario.html", estudiante=None, titulo="Nuevo estudiante")


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    with conectar() as db:
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM estudiantes WHERE id = %s", (id,))
            estudiante = cursor.fetchone()
    if estudiante is None:
        flash("Estudiante no encontrado.", "warning")
        return redirect(url_for("inicio"))
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        correo = request.form.get("correo", "").strip()
        carrera = request.form.get("carrera", "").strip()
        if not all([nombre, correo, carrera]):
            flash("Completa los tres campos.", "warning")
            estudiante = {"id": id, "nombre": nombre, "correo": correo, "carrera": carrera}
        else:
            with conectar() as db:
                with db.cursor() as cursor:
                    cursor.execute(
                        "UPDATE estudiantes SET nombre = %s, correo = %s, carrera = %s WHERE id = %s",
                        (nombre, correo, carrera, id),
                    )
            flash("Estudiante actualizado correctamente.", "success")
            return redirect(url_for("inicio"))
    return render_template("formulario.html", estudiante=estudiante, titulo="Editar estudiante")


@app.post("/eliminar/<int:id>")
def eliminar(id):
    with conectar() as db:
        with db.cursor() as cursor:
            cursor.execute("DELETE FROM estudiantes WHERE id = %s", (id,))
    flash("Estudiante eliminado.", "success")
    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
