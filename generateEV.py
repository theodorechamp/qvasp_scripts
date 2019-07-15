import os
import subprocess

parent = os.getcwd()

# User Inputs #
NUMPOINTS = 11

# Constants #
volsubstr = "volume of cell :"
enesubstr = "energy  without entropy="

# Logic #
with open("e-v.dat", 'w') as f_obj:
	for i in range(0,11):
		os.chdir(parent+"/"+str(i)+"/")
#get volume of cell
		output = str(subprocess.run("grep volume OUTCAR", stdout=subprocess.PIPE, shell=True))
		print("here")
		startindex = output.find(volsubstr) + len(volsubstr) + 6
		volume = float(output[startindex:startindex+6])

#get energy of cell
		output = str(subprocess.run("ene", stdout=subprocess.PIPE, shell = True))
		startindex = output.find(enesubstr) + len(enesubstr) + 5
		energy = float(output[startindex:startindex+13])
		f_obj.write("\t" + str(volume) + "\t" + str(energy) + "\n")
		os.chdir(parent)



