cur = None

def update_crop_water_consumption(crop_id, amount):
	"updates water consumed by a crop on nth day, no control on tick "
	cur.execute("""update crop 
				set consumption = array_append(consumption, cast (%s as double precision))
				where crop_id = %s;""",(amount, crop_id));
	
def crop_harvest(crop_id, growth, biomass):
	"update harvest information into db"
	
	cur.execute("""insert into harvest
				values (%s,%s,%s)""",(crop_id, growth, biomass));
				
def water_source_info(tick, stock, water_released):
	"update water source info"
	
	cur.execute("""insert into water_source values(%s,%s,%s);""",
				(tick, stock, water_released));
				
def supply_equation(tick, water_available, demand):
	"updated once everyday"
	cur.execute("""insert into supply values(%s,%s,%s);""",
				(tick, water_available, demand));
				
				
def supply_details(tick, crop_id, crop_db_id, demand, supply):
	"supply details, updated n times everyday"
	cur.execute("""insert into supply_details values (1, 1, 1, 12, 11 );""",
				(tick, crop_id, crop_db_id, demand, supply));
				


