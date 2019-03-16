#!/usr/bin/python

import readline
import re
import sys

filteredTests = []
dataset = []
classnamedataset = set()


tempdirlocation = sys.argv[1]
loglocation = tempdirlocation + sys.argv[2]
testcaselocation = tempdirlocation + sys.argv[3]

def readLogs(filename) :
    with open(filename, 'r') as fp:
        line = fp.readline()
        for cnt, line in enumerate(fp):

            #TODO: Remove/refactor this crap
            z = re.findall("INFO|DEBUG|ERROR", line)
            if z:
                y = re.findall("Time", line)
                if y:
                    x = re.findall("run|driver|ShutdownMonitor|ITRunner|DateTimeParse", line)
                    if not x:
                        if line not in filteredTests:
                            filteredTests.append(line)

            #To capture failure cases, directly append all failures to the file.
            z = re.findall("FAILURE!|ERROR!", line)
            if z:
                y = re.findall("run|driver|ITRunner", line)
                if not y:
                    if line not in filteredTests:
                        filteredTests.append(line)



        # print(type(testsWithTime))
    with open(tempdirlocation + 'logs_filtered', 'w') as outputfile:
        outputfile.write(''.join(str(e) for e in filteredTests))

def createTestDataSet(filename, filetosave):
    with open(filename, 'r') as fp:
        for cnt, line in enumerate(fp):
            if "[INFO]" in line:
                line = line.split("[INFO]")[1]
                status = "Passed"
            elif "[ERROR]" in line:
                line = line.split("[ERROR]")[1]
                status = "Failed"
            testname = line.split("(")[0]
            line = line.split("(")[1]
            classname = line.split(")")[0]
            line = line.split(")")[1]
            time = line.split(":")[1].split("\n")[0].split("s")[0]
            item = classname.strip() + "." + testname.strip() + "," + time.strip() + "," + status.strip() + "\n"
            if item not in dataset:
                dataset.append(item)
                classnamedataset.add(classname.strip() + "." + testname.strip())

    with open(filetosave, 'a+') as outputfile:
        outputfile.write(''.join(str(e) for e in dataset))

def addMissingTests(sourcefile, testcorpus):
    tests = set()
    missingTests = []
    origtests = []
    with open(testcorpus, 'r') as fp:
        for cnt, line in enumerate(fp):
            tests.add(line.strip())

        i = 0
        for test in tests:
            if test not in classnamedataset:
                missingTests.append(test.strip() + "," + "N.A." + "," + "Passed\n")
            else:
                missingTests.append(dataset[i])
                i += 1

    with open(sourcefile, 'a+') as outputfile:
        outputfile.write(''.join(str(e) for e in missingTests))


import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
print('dir path: ', dir_path)

readLogs(loglocation)
createTestDataSet(tempdirlocation + '/logs_filtered', tempdirlocation + '/logs_filtered_dataset')
#addMissingTests(tempdirlocation + '/logs_filtered_dataset', testcaselocation)