import checkout
import pricingRulesUtil


def test1():
	try:
		pricing_rules = pricingRulesUtil.pricingRules.fetchPrices()
	except Exception as e:
		print(e)
		return
	

	co = checkout.CheckOut(pricing_rules)
	co.scan("VOUCHER")
	co.scan("TSHIRT")
	co.scan("MUG")
	
	print("Items: ",end=" ")
	items,bill = co.generateBill()
	for i in range(len(items)):
		if(i<len(items)-1):
			print(items[i],end=", ")
		else:
			print(items[i])
	print("Price: "+str(bill))


def test2():
	try:
		pricing_rules = pricingRulesUtil.pricingRules.fetchPrices()
	except Exception as e:
		print(e)
		return
	co = checkout.CheckOut(pricing_rules)
	co.scan("VOUCHER")
	co.scan("TSHIRT")
	co.scan("VOUCHER")
	
	print("Items: ",end=" ")
	items,bill = co.generateBill()
	for i in range(len(items)):
		if(i<len(items)-1):
			print(items[i],end=", ")
		else:
			print(items[i])
	print("Price: "+str(bill))


def test3():
	try:
		pricing_rules = pricingRulesUtil.pricingRules.fetchPrices()
	except Exception as e:
		print(e)
		return
	co = checkout.CheckOut(pricing_rules)
	co.scan("TSHIRT")
	co.scan("TSHIRT")
	co.scan("TSHIRT")
	co.scan("VOUCHER")
	co.scan("TSHIRT")
	
	print("Items: ",end=" ")
	items,bill = co.generateBill()
	for i in range(len(items)):
		if(i<len(items)-1):
			print(items[i],end=", ")
		else:
			print(items[i])
	print("Price: "+str(bill))


def test4():
	try:
		pricing_rules = pricingRulesUtil.pricingRules.fetchPrices()
	except Exception as e:
		print(e)
		return
	co = checkout.CheckOut(pricing_rules)
	co.scan("VOUCHER")
	co.scan("TSHIRT")
	co.scan("VOUCHER")
	co.scan("VOUCHER")
	co.scan("MUG")
	co.scan("TSHIRT")
	co.scan("TSHIRT")
	
	print("Items: ",end=" ")
	items,bill = co.generateBill()
	for i in range(len(items)):
		if(i<len(items)-1):
			print(items[i],end=", ")
		else:
			print(items[i])
	print("Price: "+str(bill))



test1()
test2()
test3()
test4()
