from app import db
import datetime

class ListaCompra(db.Model):
	__tablename__ = "lista_compra"
	id_lista_compra = db.Column(db.Integer, primary_key=True)
	id_plan = db.Column(db.Integer, db.ForeignKey("plan.id_plan"))
	id_ingrediente = db.Column(db.Integer, nullable=False)
	cantidad_total = db.Column(db.Float, nullable=False)
	# atributos de auditoria
	usu_crea = db.Column(db.Integer, nullable=False)
	usu_mod = db.Column(db.Integer)
	usu_eli = db.Column(db.Integer)
	date_crea = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)
	date_mod = db.Column(db.DateTime)
	date_eli = db.Column(db.DateTime)
	state = db.Column(db.Integer)

	def save(self):
		if not self.id_lista_compra:
			db.session.add(self)
		db.session.commit()