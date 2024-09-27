from flask_cli import FlaskCLI
import click
from app import inicializar_app

app = inicializar_app()

if __name__ == "__main__":
    app.run(debug=True)
