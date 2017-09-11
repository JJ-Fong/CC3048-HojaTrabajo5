from models import Client, Order, Recipe, OrderDetail, Ingredient

def CreateNewClient(client):
	try:
		client_model = Client.objects.create_new_client(client)
		return client_model
	except IntegrityError as e:
		err = e.message.encode('utf-8')
		raise Exception(err)


def FindQtyOfIngredientByRecipeGui(guid,cant):
    try:
        ing = Ingredient.objects.get_ingredient_qty(guid)
        return ing
    except:
		raise Exception("Invalid ingredient, there is no ingredient with dat recipe guid.. biatch.")

def UpdateQtyOfIngredientByRecipeGui(guid,cant):
    try:
        ing = Ingredient.objects.update_ingredient_qty(guid,cant)
        # return ing
    except:
		raise Exception("Guess what? Error! Can't you even make an update? u suck..")

def FindPriceInRecipe(guid):
	try:
		precio = Recipe.objects.find_price_in_recipe_by_guid(guid)
		return precio
	except:
		raise Exception("There is no price for this product.")