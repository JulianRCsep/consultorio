from flask import Flask, render_template
from flask_migrate import Migrate
from config import Config
from modelos import db
from vistas.medicos import obtener_medicos, agregar_medico  # Importamos las vistas desde medicos.py

# Creación de la aplicación Flask
app = Flask(__name__)
app.config.from_object(Config)

# Inicializar la base de datos y migraciones
db.init_app(app)
migrate = Migrate(app, db)

# Rutas directamente aquí
app.add_url_rule('/medicos', 'obtener_medicos', obtener_medicos, methods=['GET'])
app.add_url_rule('/medicos', 'agregar_medico', agregar_medico, methods=['POST'])

# Ruta para servir el archivo HTML
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Asegúrate de que las tablas existen en la base de datos
    app.run(debug=True)
