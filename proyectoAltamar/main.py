from flask import Flask, jsonify, g, request
from src.database.db_supabase import db
from src.models.huesped import Huesped
from src.routes.__init__ import api


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.cqejclaqspbhestfhlmy:proyectoaltamar@aws-0-us-west-1.pooler.supabase.com:6543/postgres'
    db.init_app(app)

    app.register_blueprint(api)


    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5050)

