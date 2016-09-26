
cur = None


def read_crop_db():
	cur.execute('select * from crop_db');
	crop_db = cur.fetchall()
	
	return crop_db
	
