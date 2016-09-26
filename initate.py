import random

import Model
import config

from objects import Water_source
from objects import Supply
from objects import Crop_db
from objects import Crop
from objects import Soil

import connect_db
from database import update_database
from database import read_db


def connection():
	cur = connect_db.connect()
	update_database.cur = cur
	read_db.cur = cur

def sow_crop():
	r= random.random()
	crop_db_index = config.select_crop(r)
	
	return Crop.create_random_crop(Model.crop_db_list[crop_db_index -1])



connection()

# create supply object 
Model.supply = Supply.create_supply(config.strategy)

# import water source
Model.water_source_list.append(Water_source.create_random_water_source(config.dam_stock))

# import crop database
a = read_db.read_crop_db()
for i in a:
	Model.crop_db_list.append(Crop_db.create_random_crop_db(*i))


# import crop sown
for i in range(config.farms):
	Model.crop_list.append(sow_crop())

# append crops based on crop mix defined in config file.
# other way would be to import it from database as real world crop mix





