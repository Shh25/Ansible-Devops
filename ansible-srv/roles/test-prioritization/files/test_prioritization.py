#!/usr/bin/python3
import sys
from prettytable import PrettyTable

tab = PrettyTable()
tab.field_names = ['Test Name', 'Total Passed', 'Total Failed', 'Average Build Time']
combinedLogLocation = sys.argv[1]
saveInLocation = sys.argv[2]

def combine_tests(combinedLogLocation):
    # Read file
    combinedLog = open(combinedLogLocation,'r')
    finalreport = ''
    testDict = {}
    for line in combinedLog:
        lineValues = line.split(',')
        
        timeToBuildNotApplicable = 0
        timeToBuild = 0
        unitTest = lineValues[0]
        timeToBuildString = lineValues[1]
        testResult = lineValues[2].split('\n')[0]
        if testResult == 'Passed':
            successCount = 1
            failureCount = 0
        else:
            successCount = 0
            failureCount = 1

        try: 
            timeToBuild = float(timeToBuildString)
        except:
            timeToBuild = 0
            timeToBuildNotApplicable = 1

        if not unitTest in testDict:
            testDict[unitTest] = {}
            testDict[unitTest]['successCount'] = int(successCount)
            testDict[unitTest]['failureCount'] = int(failureCount)
            testDict[unitTest]['timeToBuild'] = timeToBuild
            testDict[unitTest]['timeToBuildNotApplicable'] = timeToBuildNotApplicable
            testDict[unitTest]['successToFailureDiff'] = int(successCount) - int(failureCount)
        else:
            testDict[unitTest]['successCount'] += int(successCount)
            testDict[unitTest]['failureCount'] += int(failureCount)
            testDict[unitTest]['timeToBuild'] += float(timeToBuild)
            testDict[unitTest]['timeToBuildNotApplicable'] += timeToBuildNotApplicable
            testDict[unitTest]['successToFailureDiff'] += int(successCount) - int(failureCount)

        for key in testDict:
            testCount = testDict[key]['successCount'] + testDict[key]['failureCount'] - testDict[key]['timeToBuildNotApplicable']
            if testCount == 0:
                testCount = 1
            testDict[key]['averageTimeToBuild'] = testDict[key]['timeToBuild']/testCount
    
    # finalString = ''
    sortedTuple = sorted(testDict.items(), key=lambda x: ((x[1]['successToFailureDiff']), x[1]['timeToBuild']))
    for test, val in sortedTuple:
        tab.add_row([test, str(val['successCount']), str(val['failureCount']), str(val['averageTimeToBuild'])])
        # finalString += '| ' + test + ' | successCount - ' + str(val['successCount']) + ' | failureCount - ' + str(val['failureCount']) + ' | averageTimeToBuild - ' + str(val['averageTimeToBuild']) + ' | \n'
    
    # Write file
    outputfile = open(saveInLocation, 'w')
    x = outputfile.write(str(tab))
    # print(tab)

combine_tests(combinedLogLocation)