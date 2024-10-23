# src/models/huesped.py
from src.database.db_supabase import db

class Huesped(db.Model):
    """
    create table
    HUESPED (
        cedula text primary key,
        email text not null,
        telefono text,
        nombre text not null
    );
    """

    __tablename__ = 'huesped'  # This should match the table name in Supabase

    cedula = db.Column(db.String(256), primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefono = db.Column(db.String(120), nullable=False)

    
    def __init__(self, cedula, nombre, email, telefono):
        self.cedula = cedula
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    
    @classmethod
    def get_by_cedula(cls, cedula):
        return db.session.query(cls).filter(cls.cedula == cedula).first()