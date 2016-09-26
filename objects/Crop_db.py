
class Crop_db :
	' theoretical information about crop'
	
	def __init__(self, crop_id, crop_name, market_value, yieldd, daysToHarvest, stages, crop_water_needs, total_water_required ):
		self.crop_id 		= crop_id
		self.crop_name 		= crop_name
		self.market_value 	= market_value
		self.yieldd		    = yieldd
		self.daysToHarvest = daysToHarvest
		self.stages = stages      # {20,40,60} # points of tranfromation from one stage to another
		self.crop_water_needs = crop_water_needs    #{2,3,4,5,0} # change in stage should increase index by 1
		self.total_water_required = total_water_required

	def calculate_production(self, consumption):
		'production at the harvest'
		
		
		#a= consumption
		#b = self.crop_water_needs
		#c = [float(ai)/bi for ai,bi in zip(a,b)]   # ratio_Water_taken
		c = consumption      # consumption is already ratio of water taken/demand
		sensitivity = 10
		growth = 1
		for i in range(len(c) - sensitivity):
			j = sum(c[i:i+sensitivity])/sensitivity
			if j < growth :
				growth = j
		return growth

def create_random_crop_db(crop_id, crop_name, market_value, yieldd, daysToHarvest, stages, crop_water_needs, total_water_required):
	return Crop_db(crop_id, crop_name, market_value, yieldd, daysToHarvest, stages, crop_water_needs, total_water_required)
	
