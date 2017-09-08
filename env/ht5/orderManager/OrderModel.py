import uuid

class OrderModel:
	order_guid = str(uuid.uuid4())
	address = ""
	status = "" 
	store = ""

	def __init__(self, order):
		self.products = []
		self.qty = []
		for k, v in order.items():
			if k == 'order': 	
				for key, value in v.items():
					key = key.encode('utf-8')
					if (key == 'address'):
						self.address = value
					if (key == 'products'):
						for product in value:
							for pkey, pvalue in product.items():
								if (pkey == 'qty'):
									self.qty.append(pvalue)
								if (pkey == 'product'):
									print pvalue
									self.products.append(pvalue)
						print self.qty, self.products
					if (key == 'store'):
						self.store = value
					if (key == 'status'):
						self.status = value
					
	def ValidateOrder(self, order):
		if order.client == None or order.client == "":
			raise Exception("Order CLIENT is invalid")
		if order.products == None or order.products == "":
			raise Exception("Order PRODUCTS is invalid")
		if order.status == None or order.status == "":
			raise Exception("Order STATUS is invalid")	
		return True 
	

