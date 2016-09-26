# supply function
import to_database

class Supply():
	'supply function of water source'
	
	def __init__(self, water_available, demand,strategy):
		self.water_available = water_available
		self.demand = demand    # {crop: demand}
		self.strategy = strategy
		
	def go_supply(self):
		allocation = self.allocate_water()
		self.distribute_water(allocation)
		
	def update_demand(self, crop, water):
		self.demand[crop]=water

	def update_water_available(self, water):
		self.water_available += water

	def allocate_water(self):
		total_demand = sum(self.demand.values())
		
		allocation = {}
		## checking extreme cases
		if (total_demand == 0 or self.water_available == 0):
			for crop in self.demand:
				allocation[crop] = 0
		elif(total_demand <= self.water_available):
			for crop in self.demand:
				allocation[crop] = self.demand[crop]
		else:
			eval('_'+self.strategy+'_water_allocation')(self.water_available, self.demand, allocation)
		return allocation
		
	
	def distribute_water(self, allocation):
		for crop in allocation:
			crop.soil.add_to_soil(allocation[crop])
			
		to_database.water_available = self.water_available
		to_database.demand = sum(self.demand.values())
		to_database.tick +=1
		self.water_available = 0
		self.demand.clear()
		


		
	
def _proportional_water_allocation(supply, demand, allocation):
	ratio = supply/sum(demand.values())
	for crop in demand:
			allocation[crop] = ratio*demand[crop]
	
def _preferred_water_allocation(supply, demand, allocation):

	for crop in demand:
		if(supply > 0 and supply >=demand[crop]  ):
			allocation[crop] = demand[crop]
			supply -= demand[crop]
		else:
			allocation[crop] = supply
			supply  = 0	



def create_supply(strategy):
	return Supply(0, {}, strategy)
