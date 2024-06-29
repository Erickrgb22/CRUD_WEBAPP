from flask import Flask, redirect, render_template, request, url_for
import database as db

backend = Flask(__name__)


@backend.route("/")
def index():
    return render_template("index.html")


@backend.route("/news")
def news():
    return render_template("news.html")


@backend.route("/catalog")
def catalog():
    return render_template("catalog.html")


@backend.route("/academy", methods=["GET", "POST"])
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

    return render_template("academy.html", data=insertObject)


@backend.route("/add_student", methods=["POST"])
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
