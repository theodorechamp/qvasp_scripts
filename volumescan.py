#Create Volume scan folders.
import os
import subprocess
import time

cwd = os.getcwd()
#############
#User inputs#
#############
POSCARFN = "SPOSCAR" #this could be a relative directory
VOLUMEVARIANCE = .25
NUMPOINTS = 11
SUBMIT = False
ELEMENTS = "BN"

#Logic
#read in POSCAR
initVolPara = 0.0
minVolPara = 0.0
volParaIncrement = (VOLUMEVARIANCE * 2) / NUMPOINTS
posHeader = []
posFooter = []

with open(POSCARFN, "r") as f:
    posLines = f.readlines()
    #print(posLines)
    foo = posLines[2].strip("     ").strip('\n').split()
    initVolPara = float(foo[0])
    minVolPara = initVolPara - VOLUMEVARIANCE
    posHeader.append(posLines[0])
    posHeader.append(posLines[1])

    for i in range(5,len(posLines)):
        posFooter.append(posLines[i])


#Create NUMPOINTS folders
currentVolPara = minVolPara
for i in range(0,NUMPOINTS):
    cmd = "mkdir " + cwd + "/" + str(i) + "/"
    print(str(i))
    subprocess.run(cmd, shell=True)
    time.sleep(1)

    with open(cwd + "/" + str(i) + "/POSCAR", 'w') as f_POS:
        f_POS.write(posHeader[0])
        f_POS.write(posHeader[1])
        line1 = "     " + str(currentVolPara) + "    " + "0.0000000000000000" + "    " + "0.0000000000000000\n"
        line2 = "     " + "0.0000000000000000" + "    " + str(currentVolPara) + "    " + "0.0000000000000000\n"
        line3 = "     " + "0.0000000000000000" + "    " + "0.0000000000000000" + "    " + str(currentVolPara) + "\n"
        f_POS.write(line1)
        f_POS.write(line2)
        f_POS.write(line3)
        for j in range(0,len(posFooter)):
            f_POS.write(posFooter[j])
        subprocess.run("cp " + cwd + "/POTCAR " + cwd + "/" + str(i) + "/", shell = True)
        subprocess.run("cp " + cwd + "/INCAR " + cwd + "/" + str(i) + "/", shell = True)
        subprocess.run("cp " + cwd + "/KPOINTS " + cwd + "/" + str(i) + "/", shell = True)
        currentVolPara = currentVolPara + volParaIncrement
        print("qvasp_kpts_mail 4 24 12 " + ELEMENTS + "TE_0" + str(i) + "_1.log")
        os.chdir(cwd + "/" + str(i))
        if SUBMIT:
            subprocess.run("qvasp_kpts_mail 4 24 12 " + ELEMENTS + "TE_0" + str(i) + "_1.log", shell=True)
        else:
            print("CWD: " + os.getcwd())
            print("qvasp_kpts_mail 4 24 12 " + ELEMENTS + "TE_0" + str(i) + "_1.log")
        os.chdir(cwd)
