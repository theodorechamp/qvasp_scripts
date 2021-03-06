######################################################
# Created by Theodore Champ                          #
# Weimer Group                                       #
# Last Updated: July 31, 2018                        #
# For use with the Summit Computing System at CU     #
#                                                    #
#                                                    #
# This script prepares an ENCUT Analysis             #
# To Use: First, make sure the script is	     #
# placed in the folder where you want your           #
# ENCUT folders to be created. Next, ensure          #
# the INCAR, POTCAR, KPOINTS, and POSCAR files       #
# are in this same folder. Delete any ENCUT          #
# command in the INCAR, it will be automatically     #
# added to the end. Then, run the program with       # 
# $ python CreateENCUTFolder.py                      #
# and watch the magic happen! Note you still need    #
# to run the qvasp_kpts_mail command in each folder. #
######################################################

# Imports #
import subprocess
import time
###########

# User Inputs #
ENCUTLOWER = 255
ENCUTUPPER = 300
INCREMENT = 5
###############

# Logic #
ENCUT = ENCUTLOWER
while ENCUT <= ENCUTUPPER:
	subprocess.Popen('mkdir ./'+str(ENCUT)+'/',shell=True)
	time.sleep(1)
	subprocess.Popen('cp -r ./INCAR ./'+str(ENCUT)+'/',shell=True)
	subprocess.Popen('cp -r ./POTCAR ./'+str(ENCUT)+'/',shell=True)
	subprocess.Popen('cp -r ./KPOINTS ./'+str(ENCUT)+'/',shell=True)
	subprocess.Popen('cp -r ./POSCAR ./'+str(ENCUT)+'/',shell=True)
	time.sleep(1)
	out = open("./"+str(ENCUT)+"/INCAR","a")
	out.write("ENCUT = "+ str(ENCUT))
	out.close()

	ENCUT = ENCUT + INCREMENT
########################################################################
