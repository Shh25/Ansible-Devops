#!/usr/bin/python

import sys
import os, glob
itrustPath = sys.argv[1]
os.chdir(itrustPath)

# print('1st Argument: ', sys.argv[1])
def addFuzzer(itrustPath) :
    for f in glob.iglob("*.java"):
        print(f)
        with open(f, "r") as inputfile:
            newText = inputfile.read().replace('<', '>')

        with open(f, "w") as outputfile:
            outputfile.write(newText)
    
addFuzzer(itrustPath)