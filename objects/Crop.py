from objects import Soil

import config
import random
import Model

class Crop() :
	' information about crop that is sown on the ground'
	
	def __init__(self, crop_db, soil, area, sowing_day, stage, consumption  ):
		self.crop_db = crop_db
		self.soil = soil
		
		self.area = area
		self.stage = stage
		self.sowing_day = sowing_day
		self.consumption = consumption
		
	def go_crop(self):
		self.take_water()
		self.grow()
		age = config.tick - self.sowing_day
		if(age == self.crop_db.daysToHarvest ):
			Model.ready_for_harvest.append(self)
			print("y00")
		else:
			self.update_demand()
	
	
	def take_water(self):
		water_needed = self.crop_db.crop_water_needs[self.stage]
		water_taken  = self.soil.take_from_soil(water_needed)
		self.consumption.append(water_taken/water_needed)
		
	
	def grow(self):
		age = config.tick - self.sowing_day
		if (age in self.crop_db.stages):
			self.stage +=1 
		
		
	def update_demand(self):
		ratio = self.soil.stock/self.soil.stock_max
		if ratio< 0.5 :
			Model.supply.update_demand(self, (self.soil.stock_max - self.soil.stock)*self.area)
		
			
	
	
	
			

def create_random_crop(crop_db):
	soil = Soil.Soil(config.soil_capacity, config.soil_capacity)
	area = 2 + 2*random.random()  # in hectares
	stage = 0
	crop = Crop(crop_db, soil, area, 0, stage,[])
	return crop
	
			
