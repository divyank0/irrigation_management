

ticks = 150
tick = 0
sim_id = 1

mm_per_day 		= 4		# mm
crop_mix 		= {1:0.3, 2:0.7, 3:0.8, 4:1}
strategy 	= "preferred"   #"preferred" proportional"

farms = 100    # area  = 2 + 2*random.random() =  average area = 3 hectare
dam_stock = farms*3*100*mm_per_day    
soil_capacity = 100 # in mm = soil_depth * soil_capacity{"sand":25-100,"loam":100-175,"clay":175-200}

stages = {1:"initial", 2: "crop development", 3: "mid season", 4: "late season", 5:"ready to harvest"}



# generally water requirement  ~8mm/per day. 
# for 1 hectare = 8 mm * 10000 m^2 = 8 * .001 * 10000 m^3
#  				= 80 m^3 =  80 cum = cubic metre
#
# 
# 

def select_crop(r):
	for i in crop_mix:
		if r<= crop_mix[i]:
			return i;
			
