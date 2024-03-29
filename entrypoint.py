from app import create_app, init_database
import os
# Obtenemos la varaible de entorno APP_SETTING_ENV
setting_env = os.getenv("APP_SETTING_ENV")
# Este módulo es el encargado de crear la aplicación Flask
app = create_app(setting_env)
init_database(app)
app.run() # port=5000, host="localhost"