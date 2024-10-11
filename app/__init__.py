from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_wtf.csrf import CSRFProtect
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_mail import Mail

from .models.ModeloLibro import ModeloLibro
from .models.ModeloUsuario import ModeloUsuario
from .models.ModeloCompra import ModeloCompra
from .models.entities.Usuario import Usuario
from .models.entities.Libro import Libro
from .models.entities.Compra import Compra

from .const import *
from .email import confirmacion_compra

app = Flask(__name__)

csrf = CSRFProtect()

db = MySQL(app)

login_manager_app = LoginManager(app)

mail = Mail()


@login_manager_app.user_loader
def load_user(id):
    return ModeloUsuario.obtener_por_id(db, id)


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        usuario = Usuario(
            None, request.form['usuario'], request.form['password'], None)
        usuario_logeado = ModeloUsuario.login(db, usuario)

        if usuario_logeado != None:
            login_user(usuario_logeado)
            flash(MENSAJE_BIENVENIDA, 'success')
            return redirect(url_for('index'))

        else:
            flash(LOGIN_CREDENCIALES_INVALIDAS, 'warning')
            return render_template('auth/login.html')

    else:
        return render_template('auth/login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash(LOGOUT, 'success')
    return redirect(url_for('login'))


@app.route('/')
@login_required
def index():
    if current_user.is_authenticated:
        if current_user.tipousuario.id == 1:
            try:
                libros_vendidos: list = ModeloLibro.listar_libros_vendidos(db)
                data: dict = {
                    'titulo': 'Libros vendidos',
                    'libros_vendidos': libros_vendidos
                }
                return render_template('index.html', data=data)
            except Exception as e:
                return render_template('errores/error.html', mensaje=format(e))
        else:
            try:
                compras: list = ModeloCompra.listar_compras_usuario(
                    db, current_user)
                data: dict = {
                    'titulo': 'Mis compras',
                    'compras': compras
                }
                return render_template('index.html', data=data)
            except Exception as e:
                return render_template('errores/error.html', mensaje=format(e))
    else:
        redirect(url_for('login'))


@app.route('/libros')
@login_required
def listado_libros():
    try:
        libros: list = ModeloLibro.listar_libros(db)
        data: dict = {
            'titulo': 'Listado de libros',
            'libros': libros,
        }
        return render_template('listado_libros.html', data=data)

    except Exception as e:
        return render_template('errores/error.html', mensaje=format(e))


@app.route('/comprarlibro', methods=['POST'])
@login_required
def comprar_libro():
    data_request = request.get_json()

    data = {}
    try:
        libro = ModeloLibro.leer_libro(db, data_request['isbn'])
        compra = Compra(None, libro, current_user)

        data['exito'] = ModeloCompra.registrar_compra(db, compra)
        confirmacion_compra(app, mail, current_user, libro)
    except Exception as e:
        data['exito'] = False
        data['mensaje'] = f'{e}'
    return jsonify(data)


def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404


def pagina_no_autorizada(error):
    flash(MENSAJE_USUARIO_NO_LOGEADO, 'warning')
    return redirect(url_for('login')), 401


def inicializar_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    mail.init_app(app)
    app.register_error_handler(404, pagina_no_encontrada)
    app.register_error_handler(401, pagina_no_autorizada)
    return app
