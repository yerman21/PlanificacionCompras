# PlanificacionCompras
microservicio de planificacion de compras 

# Para instalar los requerimientos
Una vez activado su entorno virtual (si esta usando uno), ejecute el siguiente codigo
`pip install -r requirements.txt`

# Variables de entorno
Definir la variable de entorno APP_SETTING_ENV. O definirlo al final del archivo scripts/activate.bat o `source bin/activate`
## Para windows
`set "APP_SETTING_ENV=conf.DevelopmentConfig"`
## Para linux
`export APP_SETTING_ENV="conf.DevelopmentConfig"`

# Carpeta instance
La carpeta instance se usara para cargar las configuraciones del desarrollador en un entorno local. Esta carpeta no sera versionada, por lo que no hay miedo de hacer cambios en ella que afecten a los demas.

Solo basta con crear `instance/config.py` a la altura de `/app` y para modificar la url de conexion colocar el siguiente codigo. Remplazar los datos necesarios.

`SQLALCHEMY_DATABASE_URI = "mysql+pymysql://dbUser:dbPass@localhost/db_name"`