from models import Client, Recipe, Order, Ingredient, OrderDetail
from OrderModel import *
from repository import *

def HandleOrderRequest(order):
    if order == {}:
        raise Exception("Invalid order data")
    orderModel = OrderModel(order)
                  



def ValidateOrderRequest(order):
	json_to_return = "{nit:c/f,"
	if order == {}:
		raise Exception("Invalid order data")
	#print order
	for i,elem in order.items():
		total = 0.0
		if((i == "token" or i == "user") or (i == "order" or i == "orderid")):
			json_to_return = json_to_return + i + ":" + elem + ","
		if (i == "products"):
			#validacion de que la orden tenga al menos un ingrediente
			allprods = elem
			if(len(elem) > 0):
				print i,elem
				for j in elem:
					id_ing = j["product_guid"]
					cant = j["quantity"]
					precio = FindPriceInRecipe(id_ing)
					total = total + (precio*cant)
					#update cantidad de acuerdo al ID del ingrediente
					qty_by_ing = FindQtyOfIngredientByRecipeGui(id_ing)
					print qty_by_ing,cant
					if(qty_by_ing >= cant):
						#si hay suficientes ingredientes
						UpdateQtyOfIngredientByRecipeGui(qty_by_ing - cant) #update de cantidad de ingredientes.
					else:
						print "No hay suficientes ingredientes para preparar la orden."

			else:
				raise Exception("Products in order has no ingredients")
	json_to_return = json_to_return + "amount:"+total + "," + "products:" + allprods + "}"
	if (cant >= 1):
		# order = '{"nit":"5464646-3","token" : "df6d11e18af84c7eb3bbcc8b7d7a9e47","orderid" : "lfakjsdlfkajsdf","amount":100.52}'
		return json_to_return
