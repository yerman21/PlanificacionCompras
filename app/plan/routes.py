from . import plan_bp
from .models import Categoria, Dia, Plan, PlanDetalle
from app import db
import datetime

@plan_bp.route("/test/insert/categoria", methods=["GET"])
def insertCategoria():
	categoria = Categoria(name="Desayuno", state=1)
	db.session.add(categoria)
	db.session.commit()
	return "<h1>Registro creado</h1>"

@plan_bp.route("/test/insert/plan", methods=["GET"])
def insertPlan():	
	categoria = Categoria(name="Break", state=1)
	dia = Dia(name="Lunes", order=2)
	#planDetalle = PlanDetalle(state="sd", id_menu=13)
	planDetalle = PlanDetalle(13, "sfsdfsdf")
	planDetalle.id_categoria = categoria.id_categoria
	planDetalle.id_dia = dia.id_dia	
	plan = Plan(name=2343, description="algo de plan1",
		usu_crea=1, state=1, planDetalles=[planDetalle])
	db.session.add(categoria)
	db.session.add(dia)
	db.session.add(plan)
	db.session.commit()
	#plan.save()

	return "<h1>Registro creado</h1>"