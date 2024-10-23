
from flask import make_response, request, jsonify, session

from src.services.gestion_reserva_service import GestionReservaService
from src.helpers.validate_input import validate_input
from src.utils.gestion_reserva_utils import HuespedAlreadyExists

class GestionReservaController:
    def __init__(self):
        self.gestion_reserva_service = GestionReservaService()

    def add_huesped(self):
        # Get the request data
        cedula = request.json.get("cedula")
        nombre = request.json.get("nombre")
        email = request.json.get("email")
        telefono = request.json.get("telefono")

        validate_input(cedula, str, error_message="Invalid cedula.")
        validate_input(nombre, str, error_message="Invalid nombre.")
        validate_input(email, str, error_message="Invalid email.")
        validate_input(telefono, str, error_message="Invalid telefono.")

        # Gestion Reserva Service
        try:
            self.gestion_reserva_service.add_huesped(cedula, nombre, email, telefono)
        except HuespedAlreadyExists:
            return jsonify({"msg": "Huesped already exists"}), 400
        except Exception as e:
            return jsonify({"msg": "Error al crear el huésped"}), 500

        return jsonify({"msg": "Huésped creado exitosamente"}), 200