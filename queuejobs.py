##################################
# Created by Theodore Champ      #
# Team Weimer                    #
# Last Updated: July 31, 2018    #
# 				 #
# For use with the Summit        #
# Computing System at CU Boulder #
#				 # 
# This program serves to queue   #
# all the jobs necessary for     #
# either an ENCUT or KPT study   #
##################################

#### Imports ####
import subprocess
import time
#################

# User Entry Values #
LowFolder = 255   #Only change if KPoint is False
UpperFolder = 300 #Only change if KPoint is False
Increment = 5
Material = "V"
KPoint = False
#####################

# Logic #
Tag = 'ENCUTStudy'
if KPoint:
	LowFolder = 2
	UpperFolder = 9
	Increment = 1
	Tag = 'KPTStudy'

Folder = LowFolder

while Folder <= UpperFolder:
	subprocess.Popen('qvasp_kpts_mail 4 24 5 ' + Material + Tag + str(Folder) + '.log',cwd='./' + str(Folder) + '/', shell=True)
	Folder = Folder + Increment
######################################################################################################################################
