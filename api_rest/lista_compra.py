from flask_restful import Resource, request

class GetListaCompra(Resource):
	def post(self):
		return "<h1>aqui va el metodo POST</h1>", 200

	def get(self):
		return "<h1>aqui va el metodo GET</h1>", 200
		
