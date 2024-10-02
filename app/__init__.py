from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from flask_mysqldb import MySQL

app = Flask(__name__)

csrf = CSRFProtect()

db = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # print(request.method)
        # print(request.form['usuario'])
        # print(request.form['password'])
        if request.form['usuario'] == 'admin' and request.form['password'] == '123456':
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/libros')
def listar_libros():
    try:
        cursor = db.connection.cursor()
        #sql = "SELECT isbn, titulo, anioedicion, autor_id FROM libro ORDER BY titulo ASC" Consulta a una sola tabla

        sql = "SELECT LIB.isbn, AUT.apellidos, AUT.nombres, LIB.titulo, LIB.anioedicion,  LIB.precio FROM libro LIB JOIN autor AUT ON LIB.autor_id = AUT.id ORDER BY AUT.apellidos ASC"

        cursor.execute(sql)
        data = cursor.fetchall()

        data = {
            'libros': data,
        }

        return render_template('listar_libros.html', data=data)

    except Exception as e:
        raise Exception(e)


def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404


def inicializar_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(404, pagina_no_encontrada)
    return app
