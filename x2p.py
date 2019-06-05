
# User Inputs #
xyzFN = "movie.xyz"
numImages = 9


# Logic #
with open(xyzFN, 'r') as f:
    file1 = f.readlines()

numAtoms = int(file1[0])

for i in range(2,numAtoms+2):
    line = file1[i].split("   ")
    print(line)
    x = line[1]
    y = line[2]
    z = line[3]

    with open("POSCAR", 'a') as f:
        wline = ' ' + x + ' ' + y + ' ' + z
        f.write(wline)

startIndex = 65
running = True
index = startIndex
filenum = 1
while running:
    with open("POSCAR" + str(filenum), 'a') as f:
        for i in range(0,numAtoms):
            line = file1[index+i]
            linesp = line.split("   ")
            f.write(' ' + linesp[1] + ' ' + linesp[2] + ' ' + linesp[3])
    print("New File\n\n")
    if filenum == numImages - 1:
        running = False
    filenum = filenum + 1
    index = index + numAtoms + 2
