import Model
import config
from database import model_processing
import to_database

def simulate_one():
	for crop in Model.crop_list:
		crop.go_crop()

	for crop in Model.ready_for_harvest:
		Model.crop_list.remove(crop)
		growth = crop.crop_db.calculate_production(crop.consumption)
		try:
			Model.production[crop.crop_db] += crop.area*crop.crop_db.yieldd*growth
		except:
			Model.production[crop.crop_db] = crop.area*crop.crop_db.yieldd*growth
	Model.ready_for_harvest =[]
	
	for water_source in Model.water_source_list:
		water_source.go_water_source()

	Model.supply.go_supply()
	model_processing.process(to_database)




while config.tick<150:
	simulate_one()
	config.tick = config.tick +1
	print(config.tick)
	connect_db.commit_db()


connect_db.commit_db()

