# soil info

class Soil:
	'soil values, in mm. The soil correspond to a crop'
	
	def __init__(self, stock, stock_max ):
		self.stock = stock
		self.stock_max = stock_max
	
	def take_from_soil(self, water):
		if self.stock >= water:
			self.stock -=water
			return water
		else:
			raise NameError('water stock went negative')
			
		
		
	def add_to_soil(self, water):
		self.stock += water
		if (self.stock > self.stock_max):
			self.stock = self.stock_max
		
		
		
	
		
	
	
