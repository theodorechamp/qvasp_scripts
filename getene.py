#################################
# Created by Theodore Champ     #
# Weimer Group                  #
# Last Updated: July 31, 2018   #
# For use with Summit Computing #
# System at CU Boulder          #
#                               #
# Will run the 'ene' command    #
# all the folders specified,    #
# then save results to a        #
# space seperated file, which   #
# is easy to open in excel      #
#################################

# Imports #
import subprocess
import time
###########

# User Input #
KPOINT = True
LOWFOLDER = 400
UPPERFOLDER = 520
INCREMENT = 5
FILENAME = 'ENEResults.txt'
##############

# Logic #
if KPOINT:
	LOWFOLDER = 2
	UPPERFOLDER = 9
	INCREMENT = 1

FOLDER = LOWFOLDER

with open(FILENAME, 'w') as f_obj:
	while FOLDER <= UPPERFOLDER:
		OUTPUT = subprocess.run('ene',cwd='./'+str(FOLDER)+'/',shell=True,stdout=subprocess.PIPE)
		strOUTPUT = str(OUTPUT.stdout)
		energies = [strOUTPUT[103:116], strOUTPUT[141:154]]  	
		f_obj.write(str(FOLDER) + '\t' + energies[0] + '\t' + energies[1]+'\n')
		FOLDER = FOLDER + INCREMENT
		time.sleep(1)
#############################################################################################################
