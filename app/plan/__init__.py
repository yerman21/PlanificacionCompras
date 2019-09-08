from flask import Blueprint

plan_bp = Blueprint("plan", __name__, template_folder="templates")
from . import routes