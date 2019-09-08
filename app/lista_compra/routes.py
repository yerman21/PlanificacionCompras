from . import lista_compra_bp
from .models import ListaCompra
from app.plan.models import Plan
import datetime

@lista_compra_bp.route("/test/insert/listacompras", methods=["GET"])
def insertListaCompras():
	plan = Plan(name="listaCompra1", description="blablalba"
		, start_date = datetime.datetime.now(), end_date = datetime.datetime.now()
		, usu_crea = 1, state=1)
	plan.save()

	lista_compra = ListaCompra(id_plan=plan.id_plan, id_ingrediente=4, cantidad_total=3.2
		, usu_crea=1, state=1)
	lista_compra.save()

	return "<h1>Registro creado</h1>"