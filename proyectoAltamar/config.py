import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import URL
from configparser import ConfigParser
from pathlib import Path
from src.database.db_supabase import db

#--------------------------------------------------
# Class to use as base class for SQLAlchemy model classes
#--------------------------------------------------
class AuxiliarMixin:
    def to_json(self):
        result = {}
        for c in self.__table__.columns:
            value = getattr(self, c.key)
            if "time" in c.key or "date" in c.key:
                if isinstance(value, datetime.datetime):
                    result[c.key] = value.strftime('%Y-%m-%d %H:%M:%S')
                elif isinstance(value, datetime.date):
                    result[c.key] = value.strftime('%Y-%m-%d')
                elif isinstance(value, datetime.time):
                    result[c.key] = value.strftime('%H:%M:%S')
                else:
                    result[c.key] = value
            else:
                result[c.key] = value
        return result

    @classmethod
    def from_json(cls, json):
        instance = cls()
        for key, value in json.items():
            if hasattr(instance, key):
                setattr(instance, key, value)
        return instance

    @classmethod
    def validate_params(cls, json):
        for key, data_type in cls.attribute_types.items():
            if (key not in json) or not(isinstance(json[key], data_type)):
                raise TypeError(f"{key} must be of type {data_type.__name__} (desde mixin)")

    @classmethod
    def validate_selected_params(cls, json, **kwargs):
        for key, bool in kwargs.items():
            print(key, bool)
            if bool:
                data_type = cls.attribute_types[key]
                if (key not in json) or (not isinstance(json[key], data_type)):
                    raise TypeError(f"{key} must be of type {data_type.__name__} (desde mixin)")

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            raise Exception('ERROR: Could not save object {}!'.format(self.__class__.__name__))
        return self

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            raise Exception('ERROR: Could not delete object {}!'.format(self.__class__.__name__))
        return self

    def update(self):
        try:
            db.session.merge(self)  # Sincroniza el estado del objeto con la base de datos
            db.session.commit()     # Escribe los cambios en la base de datos
        except Exception as e:
            print(e)
            db.session.rollback()   # Revertir si hay un error
            raise Exception('ERROR: Could not update object {}!'.format(self.__class__.__name__))
        return self

class Base(DeclarativeBase, AuxiliarMixin):
    pass
