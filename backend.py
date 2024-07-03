# Importando la libreria de Flask con diferentes modulos para
# el renderizado de los templates "HTML"
from flask import Flask, redirect, render_template, request, url_for

# Importa la conexion de la base de datos del archivo database.py
import database as db

# Creacion de un objeto que usa Flask
backend = Flask(__name__)

# Definicion de rutas de Flask:

# Ruta Raiz


@backend.route("/")
def index():
    return render_template("index.html")


# Ruta para renderizar el apartado de noticias
# La plantilla de momento esta vacia solo contiene el navbar
# ToDo: poblar de contenido esta vista


@backend.route("/news")
def news():
    return render_template("news.html")


# Ruta para renderizar el apartado del catalogo
# La plantilla esta vacia solo contiene el navbar
# Todo: poblar el contenido de esta vista


@backend.route("/catalog")
def catalog():
    return render_template("catalog.html")


# Ruta para acceder a la tabla de estudiantes del apartado
# Academy, se rederiza la plantilla base con el navbar mas una tabla
# que muestra el registro de los estudiantes


@backend.route("/academy", methods=["GET", "POST"])
# La funcion academy renderiza una tabla usando clases de boostrap
# y la rellena usando la conexion SQL mediante un cursor definido
# se hace un llamado a los datos desde la plantilla html VER academy.html
def academy():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM v27225952")
    result = cursor.fetchall()
    # Convertir data en diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in result:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    # Devuelve la plantilla y le envia los regisros de los usuarios
    return render_template("academy.html", data=insertObject)


# Ruta para añadir estudiantes


@backend.route("/add_student", methods=["POST"])
# La funcion add_student realiza el query para añadir estudiantes a la tabla
# por medio del modulo request form de flask el cual se trae los valores
# insertados en el formulario, estos los ordenamos y los pasamos al query mediante
# la funcion cursor del modulo database, regresa la pagina refrescada con el nuevo
# Registro añadido
def add_student():
    cedula = request.form["cedula"]
    lastname = request.form["lastname"]
    name = request.form["name"]
    email = request.form["email"]
    course = request.form["course"]
    section = request.form["section"]

    if cedula and lastname and name and email and course and section:
        cursor = db.database.cursor()
        sql = "INSERT INTO v27225952 (CEDULA, APELLIDO, NOMBRE, EMAIL, CURSO, SECCION) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (cedula, lastname, name, email, course, section)
        cursor.execute(sql, data)
        db.database.commit()

    return redirect(url_for("academy"))


# Ruta para editar los datos de un estudiantes
# Funcion similar a la anterior pero con query UDATE


@backend.route("/edit_student/<string:id>", methods=["POST"])
def edit_student(id):
    cedula = request.form["cedula"]
    lastname = request.form["lastname"]
    name = request.form["name"]
    email = request.form["email"]
    course = request.form["course"]
    section = request.form["section"]

    if cedula and lastname and name and email and course and section:
        cursor = db.database.cursor()
        sql = "UPDATE v27225952 SET CEDULA = %s, APELLIDO = %s, NOMBRE = %s, EMAIL = %s, CURSO = %s, SECCION = %s WHERE ID = %s"
        data = (cedula, lastname, name, email, course, section, id)
        cursor.execute(sql, data)
        db.database.commit()

    return redirect(url_for("academy"))


# Ruta para eliminar unestudiante


@backend.route("/del_student/<string:id>")
def del_student(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM v27225952 WHERE ID=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for("academy"))


if __name__ == "__main__":
    backend.run(debug=True, host="0.0.0.0")
