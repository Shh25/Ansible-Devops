#!/usr/bin/python
import sys

combinedLogLocation = sys.argv[1]

def combine_tests(combinedLogLocation):
    # Read file
    combinedLog = open(combinedLogLocation,'r')
    finalreport = ''
    testDict = {}
    for line in combinedLog:
        lineValues = line.split(' ')
        
        unitTest = lineValues[0]
        successCount = lineValues[1]
        failureCount = lineValues[2]
        timeToBuild = lineValues[3].split('\n')[0]
        if not unitTest in testDict:
            testDict[unitTest] = {}
            testDict[unitTest]['successCount'] = float(successCount)
            testDict[unitTest]['failureCount'] = float(failureCount)
            testDict[unitTest]['timeToBuild'] = float(timeToBuild)
            testDict[unitTest]['successToFailureDiff'] = float(successCount)-float(failureCount)
        else:
            testDict[unitTest]['successCount'] += float(successCount)
            testDict[unitTest]['failureCount'] += float(failureCount)
            testDict[unitTest]['timeToBuild'] = float(timeToBuild)
            testDict[unitTest]['successToFailureDiff'] += float(successCount)-float(failureCount)
    
    sortedTuple = sorted(testDict.items(), key=lambda x: ((-x[1]['successToFailureDiff']), x[1]['timeToBuild']))
    finalString = ''
    for test, val in sortedTuple:
        finalString += '| ' + test + ': | successCount - ' + str(val['successCount']) + ' | failureCount - ' + str(val['failureCount']) + ' | timeToBuild - ' + str(val['timeToBuild']) + ' | \n'
    
    # Write file
    outputfile = open(combinedLogLocation, 'w')
    x = outputfile.write(finalString)
    print(x)

combine_tests(combinedLogLocation)