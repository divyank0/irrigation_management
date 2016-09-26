import config
from database import update_database
# this file will recieve model as input
# will process it
# and create input variables for update_database
# update databases and commit



#commit_db()

def process(model):
	supply_equation(model.tick, model.water_available, model.demand)
	
def supply_equation(tick, water_available, demand):
	update_database.supply_equation(tick, water_available, demand)
