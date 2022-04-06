import os
from sqlite3 import Cursor
from flask import Flask, jsonify, render_template, request
from flask_mysqldb import MySQL

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates')
app = Flask(__name__, template_folder=template_path)
# app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')

conexion = MySQL(app)

#FUNCION LISTA DE CURSOS
@app.route('/cursos') #Ruta de la funcion
def listar():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT codigo, nombre, creditos FROM cursos"
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursor.close()
        cursos = []
        for fila in datos:
            curso = {'codigo': fila[0], 'nombre': fila[1], 'creditos': fila[2]}
            cursos.append(curso)
        return jsonify({'cursos': cursos, 'mensaje': "Estos son los cursos listados."})
    except Exception as e:
        return jsonify({'mensaje': "Error al listar."})


#FUNCION ACCEDER A PANTALLA DE AGREGAR CURSO
@app.route('/pantallaAgregarCurso') #Ruta de la funcion
def pantallaAgregarCurso():
    return render_template("agregarCurso.html")


#FUNCION AGREGAR CURSO
@app.route('/agregar', methods=['GET']) #Ruta de la funcion
def agregar():
    try:
        codigo = request.args.get('codigoCurso')
        nombre = request.args.get('nombreCurso')
        creditos = request.args.get('creditosCurso')

        cursor = conexion.connection.cursor()
        sql = f"INSERT INTO cursos (codigo, nombre, creditos) VALUES ({codigo}, '{nombre}', {creditos})"
        cursor.execute(sql)
        conexion.connection.commit()
        return "<b>Insertado con extio.</b><br><br><br>" + render_template("agregarCurso.html")
    except Exception as e:
        return "<b>Error al insertar.</b>"


#FUNCION ACCEDER A PANTALLA DE ELIMINAR CURSO
@app.route('/pantallaEliminarCurso') #Ruta de la funcion
def pantallaEliminarCurso():
    return render_template("eliminarCurso.html")


#FUNCION PARA ELIMINAR CURSO
@app.route('/eliminar') #Ruta de la funcion
def eliminar():
    try:
        codigo = request.args.get('codigoCurso')

        cursor = conexion.connection.cursor()
        sql = f"DELETE FROM cursos WHERE codigo = {codigo}"
        cursor.execute(sql)
        conexion.connection.commit()
        return "<b>Eliminado con extio.</b><br><br><br>" + render_template("eliminarCurso.html")
    except Exception as e:
        return "<b>Error al eliminar.</b>"


#FUNCION ACCEDER A PANTALLA DE ACTUALIZAR CURSO
@app.route('/pantallaActualizarCurso') #Ruta de la funcion
def pantallaActualizarCurso():
    return render_template("actualizarCurso.html")


#FUNCION ACTUALIZAR CURSO
@app.route('/actualizar', methods=['GET']) #Ruta de la funcion
def actualizar():
    try:
        codigo = request.args.get('codigoCurso')
        nombre = request.args.get('nombreCurso')
        creditos = request.args.get('creditosCurso')

        cursor = conexion.connection.cursor()
        sql = f"UPDATE cursos SET nombre = '{nombre}', creditos = {creditos} WHERE codigo = {codigo}"
        cursor.execute(sql)
        conexion.connection.commit()
        return "<b>Actualizado con extio.</b><br><br><br>" + render_template("actualizarCurso.html")
    except Exception as e:
        return "<b>Error al actualizar.</b>"


if __name__ == '__main__':
    app.run()
    