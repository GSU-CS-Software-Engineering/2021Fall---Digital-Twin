import os
import json
import sys
#import time

from pathlib import Path

print("Processing file: "+str(sys.argv[1])
+"\nWith input location: "+str(sys.argv[2]+"/"+sys.argv[1])
+"\nWith output location: "+str(sys.argv[3]+"/"+sys.argv[1])
+"\nWith settings location: "+str(sys.argv[4]+"/"))

testFile = os.path.exists(sys.argv[2]+"/"+sys.argv[1])
if (testFile):
    print("Input file found.")
testFile = os.path.exists(sys.argv[3])
if (testFile):
    print("Output directory found.")
testFile = os.path.exists(sys.argv[4])
if (testFile):
    print("Settings file found.")

#Wait 2 seconds to simulate job time.
#time.sleep(2)

#Check if the file exists before writing
#If it exists, loop (#) until filename(#) does not already exist
fileExists = os.path.exists(sys.argv[3]+"/"+sys.argv[1])
if (fileExists):
    i = 0
    while (fileExists):
        i += 1
        fileExists = os.path.exists(sys.argv[3]+"/"+sys.argv[1]+"("+str(i)+")")
    file = open(sys.argv[3]+"/"+sys.argv[1]+"("+str(i)+")", 'x')
else:
    file = open(sys.argv[3]+"/"+sys.argv[1], 'x')
file.close()

print("Job: "+str(sys.argv[5])+" completed")
