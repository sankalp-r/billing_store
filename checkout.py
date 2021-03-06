
# CheckOut class for buying and billing items
class CheckOut:
	

	# a contrucor for CheckOut class
	def __init__(self,pricing_rules):
		self.pricing_rules = pricing_rules # pricing_rules for price and discount of items
		self.total=0  # total bill amount
		self.items=[] # item-list to store items in the order of scanning
		self.billed_item_quantity={} # Bought items and their quantities

	# function to scan items for billing
	def scan(self,item):
		if(item in self.pricing_rules):
			self.total+=self.pricing_rules[item]['price']
			self.items.append(item)
			if(item in self.billed_item_quantity):
				self.billed_item_quantity[item]+=1
			else:
				self.billed_item_quantity[item]=1

	# Function to generate total bill after discounts
	def generateBill(self):
		for key,value in self.billed_item_quantity.items():
			if(self.pricing_rules[key]['discount'] !=''):
				discount_type, x, y  = self.__discountParser(self.pricing_rules[key]['discount'])
				if(value>=x):
					try:
						if(discount_type=="type1"): # type1 denotes 2-for-1 type of discount
							self.total-=(int(value/x)*self.pricing_rules[key]['price']*(x-y))
						elif(discount_type=="type2"): #type2 denotes buy x or more type of discount
							self.total-=(value*(self.pricing_rules[key]['price']-y))
					except ArithmeticError:
						print('Arithmetic exception occured')
						raise
		return self.items,self.total

	# A private function to parse discount rules
	# Categorised the discount in two type:
	# 1. type1 for 2-for-1
	# 2. type2 for 3-or-more-19
	# This parser can be externlized for more discount rules and it can be improved to raise errors if discount is invalid
	def __discountParser(self,discount):
		discount = discount.split('-')
		if(len(discount)==3):
			return "type1",int(discount[0]),int(discount[2]) 
		else:
			return "type2",int(discount[0]),int(discount[3])







