from . import plan_bp

@plan_bp.route("/test/insert/categoria", methods=["GET"])
def insertCategoria():
	categoria = Categoria(name="Desayuno", state=1)
	db.session.add(categoria)
	db.session.commit()
	return "<h1>Registro creado</h1>"

