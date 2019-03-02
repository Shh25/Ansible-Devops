#!/usr/bin/python

import sys
import os, fnmatch
itrustPath = sys.argv[1]

def getFilesByPattern(pattern, directoryPath) :
    result = []
    for root, dirs, files in os.walk(directoryPath):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result
    
def addFuzzer(pattern, directoryPath) :
    javaFiles = getFilesByPattern(pattern, directoryPath)
    for filename in javaFiles:
        with open(filename, 'r') as inputfile:
            newText = inputfile.read().replace('<', '>').replace('==', '!=').replace('0', '1')

        with open(filename, 'w') as outputfile:
            outputfile.write(newText)


addFuzzer('*.java', itrustPath)
