#surface water source
import random
import Model
import config
from objects import Supply

class Water_source():
	'water source likes dams'
	
	def __init__(self, stock, water_released):
		self.stock = stock
		self.water_released = water_released

	def go_water_source(self):
		# allocate water for day
		self.allocate_water()
		
		# release water to supply function
		self.release_water()
	
	def allocate_water(self):
		#predict demand for rest of days
		# predict demand for tomorrow
		# see how much water you can supply tomorrow
		# suppply that water
		# 
		self.water_released =  config.dam_stock/150
	
	def release_water(self):
		Model.supply.update_water_available(self.water_released )
		self.stock -= self.water_released
		


def create_random_water_source(stock):
	water_source = Water_source(stock, 0)
	return water_source
	


