import os
import json

# Utility class to fetch pricing rules
class pricingRules:
	itemStore="itemStore.json" # json input-file
	metadata=None # Metadata to store modified-date of the json-file
	priceCache={} # Cache to store the contents of the json-file(persisting data in-memory to avoid reading file multiple times)

	# Function to fetch pricing_rules
	@staticmethod
	def fetchPrices():
		try:
			if(pricingRules.metadata==None):
			# First time cache-creation
				pricingRules.metadata = os.stat(pricingRules.itemStore).st_mtime
				pricingRules.__createCache()
			else:
				modified_date = os.stat(pricingRules.itemStore).st_mtime

				# Updating cache if the content is modified
				if(pricingRules.metadata<modified_date):
					pricingRules.metadata = modified_date
					pricingRules.__createCache()
		
		except (OSError,FileNotFoundError):
			print('Error reading json-file')
			raise

		
		return pricingRules.priceCache


	# Function to create priceCache of pricing_rules
	@staticmethod
	def __createCache():

		try:
			# reading pricing_rules from json-file
			with open(pricingRules.itemStore) as json_file:
				pricingRules.priceCache = json.load(json_file)
		
		except OSError:
			print('Error reading json-file')
			raise
