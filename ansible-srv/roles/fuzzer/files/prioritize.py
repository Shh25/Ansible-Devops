#!/usr/bin/python

import readline
import re
import sys

filteredTests = []
dataset = []

loglocation = sys.argv[1]
tempdirlocation = sys.argv[2]

def readLogs(filename) :
    with open(filename, 'r') as fp:
        line = fp.readline()
        for cnt, line in enumerate(fp):

            #TODO: Remove/refactor this crap
            z = re.findall("INFO|DEBUG|ERROR", line)
            if z:
                y = re.findall("Time", line)
                if y:
                    x = re.findall("run|driver|ShutdownMonitor|ITRunner", line)
                    if not x:
                        filteredTests.append(line)

            #To capture failure cases, directly append all failures to the file.
            z = re.findall("FAILURE!|ERROR!", line)
            if z:
                y = re.findall("run|driver|ITRunner", line)
                if not y:
                    filteredTests.append(line)



        # print(type(testsWithTime))
    with open(tempdirlocation + 'logs_filtered', 'w') as outputfile:
        outputfile.write(''.join(str(e) for e in filteredTests))

def createTestDataSet(filename):
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
            time = line.split(":")[1].split("\n")[0].split("s")[0] + "s"
            item = classname.strip() + "." + testname.strip() + ", " + time.strip() + ", " + status.strip() + "\n"
            if item not in dataset:
                dataset.append(item)

    with open(filename + '_dataset', 'w') as outputfile:
        outputfile.write(''.join(str(e) for e in dataset))

def addMissingTests(sourcefile, testcorpus):
    tests = []
    missingTests = []
    presentTests = []
    origtests = []
    with open(testcorpus, 'r') as fp:
        for cnt, line in enumerate(fp):
            tests.append(line.strip())

    with open(sourcefile, 'r') as fp:
        for cnt, line in enumerate(fp):
            presentTests.append(line.split(", ")[0].strip())
            origtests.append(line)

        i = 0
        for test in tests:
            if test not in presentTests:
                missingTests.append(test.strip() + ", " + "N.A." + ", " + "Passed\n")
            else:
                missingTests.append(origtests[i])
                i += 1

    with open(sourcefile, 'w') as outputfile:
        outputfile.write(''.join(str(e) for e in missingTests))


readLogs(loglocation)
createTestDataSet(tempdirlocation + '/logs_filtered')
addMissingTests(tempdirlocation + '/logs_filtered_dataset', '/vagrant/roles/fuzzer/templates/testcases')
