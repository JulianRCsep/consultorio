from flask import jsonify, request
from modelos import db, Medico

# Función para obtener los médicos
def obtener_medicos():
    medicos = Medico.query.all()
    medicos_serializados = [
        {'id': medico.id, 'nombre': medico.nombre, 'especialidad': medico.especialidad, 'email': medico.email}
        for medico in medicos
    ]
    return jsonify(medicos_serializados), 200

# Función para agregar un nuevo médico
def agregar_medico():
    datos = request.json
    nombre = datos.get('nombre')
    especialidad = datos.get('especialidad')
    email = datos.get('email')

    if not nombre or not especialidad or not email:
        return jsonify({'error': 'Todos los campos son obligatorios'}), 400

    if Medico.query.filter_by(email=email).first():
        return jsonify({'error': 'El médico con este email ya existe'}), 400

    nuevo_medico = Medico(nombre=nombre, especialidad=especialidad, email=email)
    db.session.add(nuevo_medico)
    db.session.commit()

    return jsonify({'mensaje': 'Médico agregado exitosamente'}), 201


