from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo'


def inicializar_app():
    return app
