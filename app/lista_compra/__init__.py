from flask import Blueprint

lista_compra_bp = Blueprint("lista_compra", __name__, template_folder="templates")
from . import routes