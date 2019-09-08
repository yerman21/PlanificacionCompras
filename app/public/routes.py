from flask import render_template
from . import public_bp

@public_bp.route("/", methods=["GET"])
def inicio():
	return render_template("index.html")