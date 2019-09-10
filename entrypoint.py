from app import create_app, setup_database
import os
# Obtenemos la varaible de entorno APP_SETTING_ENV
setting_env = os.getenv("APP_SETTING_ENV")
# Este módulo es el encargado de crear la aplicación Flask
app = create_app(setting_env)
setup_database(app)
app.run()