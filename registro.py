from flask import Flask, request, jsonify
from modelos import db, Usuario, UsuarioSchema

app = Flask(__name__)

@app.route('/registro', methods=['POST'])
def registrar_usuario():
    datos = request.get_json()
    
    if not datos.get('nombre') or not datos.get('email') or not datos.get('contraseña'):
        return jsonify({'error': 'Faltan datos: nombre, email y contraseña'}), 400

    if Usuario.query.filter_by(email=datos['email']).first():
        return jsonify({'error': 'Email ya registrado'}), 400

    nuevo_usuario = Usuario(nombre=datos['nombre'], email=datos['email'], contraseña=datos['contraseña'])
    db.session.add(nuevo_usuario)
    db.session.commit()

    usuario_schema = UsuarioSchema()
    return jsonify({'mensaje': 'Usuario registrado', 'usuario': usuario_schema.dump(nuevo_usuario)}), 201
