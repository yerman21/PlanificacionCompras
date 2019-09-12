# config.py
import os
"""cargando configuraciones de config.py"""

class Config(object):
	ENV = "Development"
	SECRET_KEY = "my_secret_is_you"
	#SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
	ENV = "Development"
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/db_pc"

class TestingConfig(Config):
    ENV = "Test"
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_pass@test_host:port/db_name'

class ProductConfig(Config):
	ENV = "Production"
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/planificacionCompras"
