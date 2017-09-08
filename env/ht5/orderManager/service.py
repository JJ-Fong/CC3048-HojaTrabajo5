from models import Client, Recipe, Order, Ingredient, OrderDetail
from OrderModel import *
from repository import *

def HandleOrderRequest(order):
    if order == {}:
        raise Exception("Invalid order data")
    orderModel = OrderModel(order)
                  



def ValidateOrderRequest(order):
	if order == {}:
		raise Exception("Invalid order data")
	print order
	#order