from models import Client, Recipe, Order, Ingredient, OrderDetail
from OrderModel import *
from repository import *

def HandleOrderRequest(order):
    if order == {}:
        raise Exception("Invalid order data")
    orderModel = OrderModel(order)
    order_model = CreateNewOrder(orderModel)
    for det in orderModel.detail:
    	detail_model = CreateNewDetail(det)
