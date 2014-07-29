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
        
def readPDB(argv):
    prot = Protein(argv[1])
    file = open(argv[1], 'r')
    
    for line in file:
        tokens = line.split()
        if tokens[0] == 'ATOM':
            atm = Atom(tokens[2], tokens[6], tokens[7], tokens[8])
            prot.addAtom(atm)
    
    prot.printAtoms()
    
readPDB(sys.argv)
