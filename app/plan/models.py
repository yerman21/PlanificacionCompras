from app import db
import datetime

class Categoria(db.Model):
	__tablename__ = "categoria"
	id_categoria = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=False)
	state = db.Column(db.Integer, nullable=False)
	planDetalles = db.relationship("PlanDetalle")

class Dia(db.Model):
	__tablename__ = "dia"
	id_dia = db.Column(db.Integer, primary_key=True)
	order = db.Column(db.Integer, nullable=False)
	name = db.Column(db.String(10), nullable=False)
	planDetalles = db.relationship("PlanDetalle")

class Plan(db.Model):
	__tablename__ = "plan"
	id_plan = db.Column(db.Integer, primary_key=True)	
	name = db.Column(db.String(200), nullable=False)
	description = db.Column(db.String(300))
	start_date = db.Column(db.DateTime)
	end_date = db.Column(db.DateTime)
	usu_crea = db.Column(db.Integer, nullable=False)
	usu_mod = db.Column(db.Integer)
	usu_eli = db.Column(db.Integer)
	date_crea = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)
	date_mod = db.Column(db.DateTime)
	date_eli = db.Column(db.DateTime)
	state = db.Column(db.Integer, nullable=False)
	# este campo no se va a crear, solo es para que nos devuelva datos
	# al momento de hacer join (ojo: se pone el nombre de la clase "PlanDetalle")
	planDetalles = db.relationship("PlanDetalle")
	listaCompras = db.relationship("ListaCompra")

	def save(self):
		if not self.id_plan:
			db.session.add(self)
		db.session.commit()

class PlanDetalle(db.Model):
	__tablename__ = "plan_detalle"
	id_plan_detalle = db.Column(db.Integer, primary_key=True)
	# Se referencia a la tabla y al atributo por el qeu se relacionara
	id_plan = db.Column(db.Integer, db.ForeignKey("plan.id_plan"))
	id_menu = db.Column(db.Integer, nullable=False)
	id_categoria = db.Column(db.Integer, db.ForeignKey("categoria.id_categoria"))
	id_dia = db.Column(db.Integer, db.ForeignKey("dia.id_dia"))
	state = db.Column(db.Integer)
	planProductos = db.relationship("PlanProducto")

	def __init__(self, id_menu, state):
		self.id_menu = id_menu
		self.state = state

	def save(self):
		if not self.id_plan_detalle:
			db.session.add(self)
		db.session.commit()

class PlanProducto(db.Model):
	__tablename__ = "plan_producto"
	id_plan_producto = db.Column(db.Integer, primary_key=True)
	id_plan_detalle = db.Column(db.Integer, db.ForeignKey("plan_detalle.id_plan_detalle"))
	id_ingrediente = db.Column(db.Integer, nullable=False)
	cantidad = db.Column(db.Float, nullable=False)