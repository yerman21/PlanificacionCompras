import os

class Config(object):
	SECRET_KEY = "my_secret_is_you"
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
	ENV = "Development"
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/planificacionCompras"

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_pass@test_host:port/db_name'

class ProductConfig(Config):
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/planificacionCompras"
