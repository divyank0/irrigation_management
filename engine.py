import sys
import time
import copy

print(sys.version)



########################################################################3
#### begin logging
logs = False
if(logs):
	temp = sys.stdout
	fileName = 'logs/log_' + str(int(time.time())) + '.log'
	sys.stdout = open(fileName,'w')
###########################################################################

import initate
import simulate




connect_db.close_db()

























########################################################

if(logs):
	sys.stdout.close()
	sys.stdout = temp
	print(open(fileName).read())
##############################################################
