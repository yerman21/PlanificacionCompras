# PlanificacionCompras/app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_wtf import CsrfProtect

db = SQLAlchemy()
api = Api()
csrf = CsrfProtect()

def create_app(settings_env="config.DevelopmentConfig"):
	import os
	TOP_LEVEL_DIR = os.path.abspath(os.curdir)
	PATH_INSTANCE = os.path.join(TOP_LEVEL_DIR, "instance")
	app = Flask(__name__, template_folder='templates', instance_path=PATH_INSTANCE, instance_relative_config=True)
	# print("imprimirendo -> {}".format(os.path.abspath(os.curdir)))
	# Cargamos la configuracion DevelopmentConfig por defecto
	app.config.from_object(settings_env)
	# Cargar la configuracion del folder instance
	app.config.from_pyfile("configLocal.py", silent=True)
	# Iniciamos el token de nuestra configuracion cargado en app
	# para evitar el CSRF
	csrf.init_app(app)
	# Iniciamos las configuracion de db cargadas en app
	db.init_app(app)
	# Iniciamos la api rest
	api.init_app(app)
	# Añadimos los blueprint a nuestra app
	from .public import public_bp
	app.register_blueprint(public_bp)
	from .lista_compra import lista_compra_bp
	app.register_blueprint(lista_compra_bp)
	from .plan import plan_bp
	app.register_blueprint(plan_bp)	

	return app

def init_database(app):
    with app.app_context(): # Para que es esta cosa?????????
        db.create_all()