#!/bin/env python
import sys

class Atom:
    def __init__(self, nameatm, xvalue, yvalue, zvalue):
        self.name = nameatm
        self.x = xvalue
        self.y = yvalue
        self.z = zvalue

class Protein:
    def __init__(self, pdb_name):
        self.atoms = []
        self.name = pdb_name.split()[0]
        
    def addAtom(self, atm):
        self.atoms.append(atm)
        
    def printAtoms(self):
        for atm in self.atoms:
            print (atm.name, atm.x, atm.y, atm.z)
            
class Ligand:
    def __init__(self, lig_name):
        self.atoms = []
        self.name = lig_name.split()[0]
        
    def addAtom(self, atm):
        self.atoms.append(atm)
        
    def printAtoms(self):
        for atm in self.atoms:
            print (atm.name, atm.x, atm.y, atm.z)
        
def readPDB(argv):
    prot = Protein(argv[1].trip('.pdb'))
    lig = Ligand(argv[1].trip('.pdb'))
    file = open(argv[1], 'r')
    
    for line in file:
        tokens = line.split()
        if tokens[0] == 'ATOM':
            atm = Atom(tokens[2], 
                       float(tokens[6]),
                       float(tokens[7]), 
                       float(tokens[8]))
            prot.addAtom(atm)
        
        elif tokens[0] == 'HETATM':
            atm2 = Atom(tokens[2], 
                        float(tokens[6]), 
                        float(tokens[7]), 
                        float(tokens[8]))
            lig.addAtom(atm2)

def distAtm(alfa, beta):
    from math import pow, sqrt
    return sqrt(pow(alfa.x - beta.x, 2)+
                pow(alfa.y - beta.y, 2)+
                pow(alfa.z - beta.z, 2))


def angleAtm(alfa, beta, gamma):
    from math import acos, pow, degrees
    a = distAtm(alfa, gamma)
    b = distAtm(beta, gamma)
    c = distAtm(alfa, beta)
    return degrees(acos((pow(a,2) + pow(b,2) - pow(c,2)) / (2*a*b)))

#readPDB(sys.argv)


A = Atom('A', 4, 5, 6)
B = Atom('B', 4, 5, 0)
C = Atom('C', 1, 1, 0)
print (distAtm(A, B)) #6
print (distAtm(B, C)) #5
print (distAtm(C, A))

print(angleAtm(A,C,B)+angleAtm(C,B,A)+angleAtm(B,A, C))

