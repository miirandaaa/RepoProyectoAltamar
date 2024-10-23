\
from flask import Blueprint, jsonify
from src.models.huesped import Huesped
from src.database.db_supabase import db

from src.controllers.gestion_reserva_controller import GestionReservaController


# Crear el Blueprint
api = Blueprint("api", __name__)

gestion_reserva_controller = GestionReservaController()

# Ruta simple de prueba
@api.route('/')
def hello_world():
    return jsonify({"message": "Hello, World!"})

# Ruta para obtener los huéspedes
@api.route("/gestion_reserva/get_huesped", methods=["GET"])
def get_huesped():
    try:
        huespedes = Huesped.query.all()  # Consulta todas las entradas en la tabla Huesped
        huesped_list = [
            {
                'cedula': huesped.cedula,
                'nombre': huesped.nombre,
                'email': huesped.email,
                'telefono': huesped.telefono
            }
            for huesped in huespedes
        ]
        return jsonify(huesped_list), 200  # Retorna como JSON con estado 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Retorna un mensaje de error si algo falla

# Ruta para agregar un huésped
@api.route("/gestion_reserva/add_huesped", methods=["POST"])
def add_huesped_endpoint():
    return gestion_reserva_controller.add_huesped()
