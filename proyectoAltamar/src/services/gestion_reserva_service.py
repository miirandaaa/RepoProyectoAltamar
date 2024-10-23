from datetime import datetime, time
from src.exceptions import BusinessLogicException
from src.models.huesped import Huesped
from config import AuxiliarMixin

class GestionReservaService:
    def __init__(self):
        pass

    def add_huesped(self, cedula, nombre, email, telefono):

        # Check if the huesped already exists
        if Huesped.get_by_cedula(cedula):
            raise BusinessLogicException("Huesped already exists")

        # Create the huesped
        new_huesped = Huesped(cedula, nombre, email, telefono)
        AuxiliarMixin.save(new_huesped)
        

        return new_huesped


