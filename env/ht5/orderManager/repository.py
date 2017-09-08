from models import Client, Order, Recipe, OrderDetail, Ingredient

def CreateNewClient(client):
	try:
		client_model = Client.objects.create_new_client(client)
		return client_model
	except IntegrityError as e:
		err = e.message.encode('utf-8')
		raise Exception(err)