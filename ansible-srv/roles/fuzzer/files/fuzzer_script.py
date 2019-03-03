#!/usr/bin/python

import sys
import os, fnmatch
import random

# random.seed(233)

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
        if random.random() < 0.25:
            with open(filename, 'r') as inputfile:
                newText = inputfile.read()
                if random.random() < 0.1:
                    newText = newText.replace('<', '>')
                if random.random() < 0.1:
                    newText = newText.replace('==', '!=')
                if random.random() < 0.1:
                    newText = newText.replace('0', '1')

            with open(filename, 'w') as outputfile:
                outputfile.write(newText)
        

addFuzzer('*.java', itrustPath)
