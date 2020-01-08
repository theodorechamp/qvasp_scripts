import sys
import math

poscarorder = []
distance = []

class ioninfo():
    def __init__(self, element, num):
        self.element = element
        self.num = num

class atom():

    def __init__(self, posfrac, basisi, basisj, basisk):
            self.posfrac = []
            for i in posfrac:
                self.posfrac.append(float(i))
            self.basisi = []
            for i in basisi:
                self.basisi.append(float(i))
            self.basisj = []
            for i in basisj:
                self.basisj.append(float(i))
            self.basisk = []
            for i in basisk:
                self.basisk.append(float(i))

            self.posabs = [0.0,0.0,0.0]
            self.calcabs()


    def switchcell(self, direction, switch):
        #print("Switching cell in " + str(direction) + " direction")
        self.posfrac[direction] = self.posfrac[direction] + switch * 1
        self.calcabs()

    def calcabs(self):
        self.posabs[0] = self.posfrac[0]*self.basisi[0]+self.posfrac[1]*self.basisj[0]+self.posfrac[2]*self.basisk[0]
        self.posabs[1] = self.posfrac[0]*self.basisi[1]+self.posfrac[1]*self.basisj[1]+self.posfrac[2]*self.basisk[1]
        self.posabs[2] = self.posfrac[0]*self.basisi[2]+self.posfrac[1]*self.basisj[2]+self.posfrac[2]*self.basisk[2]

def parseposcar(fn):

    with open(fn, 'r') as f_obj:
        lines = f_obj.readlines()
        basisi = lines[2].split()
        basisj = lines[3].split()
        basisk = lines[4].split()

        ions = lines[5].split()
        ionnum = lines[6].split()
        for i in range(0, len(ions)):
            tempion = ioninfo(ions[i], ionnum[i])
            poscarorder.append(tempion)

        ionlist = []

        for i in range(8,1000):
            posfrac = [0.0, 0.0, 0.0]
            try:
                posfrac = lines[i].split()
                if(len(posfrac) == 0):
                    break
            except IndexError:
                break
            ionlist.append(atom(posfrac, basisi, basisj, basisk))

        return ionlist

def getdistances(ionlist, ionnum):
    ioninterest = ionlist[ionnum-1]

    for ion in ionlist:
        for i in range(0,3):
            if ioninterest.posfrac[i] - ion.posfrac[i] > 0.5:
                ion.switchcell(i, 1)
            elif ioninterest.posfrac[i] - ion.posfrac[i] < -0.5:
                ion.switchcell(i, -1)

    for ion in ionlist:
        distance.append(math.sqrt( \
          (ioninterest.posabs[0] - ion.posabs[0])**2 \
        + (ioninterest.posabs[1] - ion.posabs[1])**2 \
        + (ioninterest.posabs[2] - ion.posabs[2])**2))
    distancesort = distance[:]
    distancesort.sort()
    return distancesort


def main():

    if('-f' in sys.argv):
        index = sys.argv.index('-f') + 1
        fn = sys.argv[index]
    else:
        fn = "POSCAR"
    if('-i' in sys.argv):
        index = sys.argv.index('-i') + 1
        iontype = sys.argv[index]
    else:
        iontype = 'no'
    if('-n' in sys.argv):
        index = sys.argv.index('-n') + 1
        numnear = int(sys.argv[index])
    else:
        numnear = 0
    if('-r' in sys.argv):
        index = sys.argv.index('-r') + 1
        radius = float(sys.argv[index])
    else:
        radius = 0.0
    ionnum = int(sys.argv[1])

    ionlist = parseposcar(fn)
    distancesorted = getdistances(ionlist,ionnum)

    ionnumbers = []
    if numnear > 0:
        for i in range(0, numnear):
            ionnumbers.append(distance.index(distancesorted[i])+1)
    elif radius > 0.0:
        i = 0
        while True:
            if distancesorted[i] > radius:
                break
            else:
                ionnumbers.append(distance.index(distancesorted[i]) + 1)
            i = i + 1
    else:
        print("Please specify either a radius or a number of atoms")
        sys.exit(0)

    for i in ionnumbers:
        index1 = 0
        index2 = 0
        ionname = ""
        while True:
            if i > int(poscarorder[index1].num) + index2:
                index2 = index2 + int(poscarorder[index1].num)
                index1 = index1 + 1
            else:
                ionname = poscarorder[index1].element
                break
        print(str(i) +  " " + ionname + " " +  "{0:.2f}".format(float(distance[i-1])) + "A")

if __name__ == "__main__":
    main()
