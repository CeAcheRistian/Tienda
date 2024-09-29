from app import inicializar_app
from config import config

configuracion = config['development']
app = inicializar_app(configuracion)

if __name__ == "__main__":
    app.run()
