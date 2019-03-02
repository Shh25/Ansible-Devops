#!/usr/bin/python

import sys
import os, fnmatch
import codecs
itrustPath = sys.argv[1]

# print('1st Argument: ', sys.argv[1])
def getFilesByPattern(pattern, directoryPath) :
    result = []
    for root, dirs, files in os.walk(directoryPath):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    # print(result)
    return result
    
def addFuzzer(itrustPath) :
    javaFiles = getFilesByPattern('*.java', itrustPath)
    for filename in javaFiles:
        f = codecs.open(filename, encoding='utf-8')
        contents = f.read()

        newcontents = contents.replace('>','<').replace('==', '!=').replace('0', '1')
        f.close()

        f = codecs.open(filename,"w", encoding='utf-8')
        f.write(newcontents)
        print(f)
        # with open(f, "r") as inputfile:
        #     newText = inputfile.read().replace('<', '>')
        #     print(newText)

        # with open(f, "w") as outputfile:
        #     outputfile.write(newText)

addFuzzer(itrustPath)

