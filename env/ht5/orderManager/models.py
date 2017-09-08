from __future__ import unicode_literals

from django.db import models
from django.conf import settings
import uuid
import datetime
# Create your models here.



class ClientManager(models.Manager):
	def create_new_client(self, client):
		try:
			client_model = self.create(client_guid=client.client_guid, name=client.name, address=client.address)
			return client_model
		except Exception, e:
			raise Exception("Invalid client data: " + str(e))

	def find_client_by_guid(self, guid):
		try:
			client_model = self.get(client_guid=guid)
			return client_model
		except Exception, e:
   			raise Exception("CLIENT GUID NOT FOUND: " + str(e))

class Client(models.Model):
	client_guid = models.CharField(max_length=250, primary_key=True, unique=True)
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	objects = ClientManager() 

class OrderManager(models.Manager):
	def create_new_order(self, order):
		try:
		    order_model = self.create(order_guid=order.order_guid, status=order.status, client=order.client)
		    return order_model
		except Exception, e:
   			raise Exception("Invalid order data: " + str(e))

	def find_order_by_guid(self, guid):
		try:
		    order_model = self.get(order_guid=guid)
		    return order_model
		except Exception, e:
		    raise Exception("ORDER GUID NOT FOUND: " + str(e))

class Order(models.Model):
	order_guid = models.CharField(max_length=250, primary_key=True, unique=True)
	status = models.CharField(max_length=100)
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	objects = OrderManager() 

class RecipeManager(models.Manager):
	def create_new_recipe(self, recipe):
	    try:
	        recipe_model = self.create(recipe_guid=recipe.recipe_guid, name=recipe.name, price=recipe.price)
	        return recipe_model
	    except Exception, e:
	        raise Exception("Invalid recipe data: " + str(e))

	def find_recipe_by_guid(self, guid):
	    try:
	        recipe_model = self.get(recipe_guid=guid)
	        return recipe_model
	    except Exception, e:
	        raise Exception("RECIPE GUID NOT FOUND: " + str(e))
    

class Recipe(models.Model):
	recipe_guid = models.CharField(max_length=250, primary_key=True, unique=True)
	name = models.CharField(max_length=100)
	price = models.FloatField()
	objects = RecipeManager() 

class OrderDetailManager(models.Manager):
	def create_new_order_detail(self, order):
	    try:
	        detail_model = self.create(order_guid=order.order_guid, product_guid=order.product_guid, qty=order.qty, value=order.value)
	        return detail_model
	    except Exception, e:
	        raise Exception("Invalid detail data: " + str(e))

	def find_detail_by_order_guid(self, guid):
	    try:
	        order_model = self.get(order_guid=guid)
	        return order_model
	    except Exception, e:
	        raise Exception("ORDER GUID NOT FOUND: " + str(e))

class OrderDetail(models.Model):
	order_guid = models.ForeignKey(Order, on_delete=models.CASCADE)
	product_guid = models.ForeignKey(Recipe)
	qty = models.FloatField()
	value = models.FloatField()
	objects = OrderManager() 


class IngredientManager(models.Manager):
	def create_new_ingredient(self, ingredient):
	    try:
	        ingredient_model = self.create(recipe_guid=ingredient.recipe_guid, name=ingredient.name, qty=ingredient.qty)
	        return ingredient_model
	    except Exception, e:
	        raise Exception("Ingredient order data: " + str(e))

	def find_ingredient_by_recipe_guid(self, guid):
	    try:
	        ingredient_model = self.get(recipe_guid=guid)
	        return ingredient_model
	    except Exception, e:
	        raise Exception("Recipe GUID NOT FOUND: " + str(e))

class Ingredient(models.Model):
	recipe_guid = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	qty = models.FloatField()
	objects = IngredientManager() 
