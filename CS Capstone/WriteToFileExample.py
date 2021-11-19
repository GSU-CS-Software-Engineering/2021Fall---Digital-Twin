import os
import sys
import json
import subprocess

if (len(sys.argv) > 1):
    #Number of batches will be equal to the number of unique settings files
    numBatches = int(sys.argv[1]);
    numJobs = int(sys.argv[2]);
    numFiles = int(sys.argv[3]);

    print("Printing test files to Pre-processed directory.")
    for j in range(int(sys.argv[2])*int(sys.argv[3])):
        fileName = "DTPipeline/Pre-processed/test.CATPart"
        fileExists = os.path.exists(fileName)
        if (fileExists):
            i = 0
            #Split filename and extension
            temp = fileName.split('.')
            while (fileExists):
                i += 1
                fileExists = os.path.exists(temp[0]+"("+str(i)+")."+temp[1])
            file = open(temp[0]+"("+str(i)+")."+temp[1], 'x')
        else:
            file = open(fileName, 'x')
        file.close()

    print("Printing test files to Recipes directory.")
    for j in range(int(sys.argv[1])):
        settingsFileName = "DTPipeline/Recipes/test.Recipe"
        settingsFileExists = os.path.exists(settingsFileName)
        if (settingsFileExists):
            i = 0
            #Split filename and extension
            temp = settingsFileName.split('.')
            while (settingsFileExists):
                i += 1
                settingsFileExists = os.path.exists(temp[0]+"("+str(i)+")."+temp[1])
            file = open(temp[0]+"("+str(i)+")."+temp[1], 'x')
        else:
            file = open(settingsFileName, 'x')
        file.close()
else:
    print("Please use the following argument input format: "
    +"int(number of batches) "
    +"int(number of jobs per batch) "
    +"int(number of files per job)")
