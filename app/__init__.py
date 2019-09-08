# PlanificacionCompras/app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_wtf import CsrfProtect

db = SQLAlchemy()
api = Api()
csrf = CsrfProtect()

def create_app(settings_env="config.DevelopmentConfig"):
	app = Flask(__name__, template_folder='templates')
	# Cargamos la configuracion DevelopmentConfig por defecto
	app.config.from_object(settings_env)
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