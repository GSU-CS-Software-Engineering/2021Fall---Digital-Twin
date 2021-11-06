#!/usr/bin/python

import os, sys, json

# This is set to 'True' for debug of output data
DEBUG = True

list_Unsorted=[]

# Open a file ********** WHAT SHOULD THE PATH BE? ***********
path = "c:"
dirs = os.listdir(path)

if DEBUG:
    print("THESE ARE ALL THE FILES WITHIN THE PATH DIRECTORY: ")
    
# This would check all the files within the "path" directory
for file in dirs:
    print(file)
    # This would import json files of "png"extension into "list_Unsorted"
#    for f in dirs:
    if(str(file))[-3:] == "png":
        list_Unsorted.append(file)
            
# This is the json list
jsonList=json.dumps(list_Unsorted)
if DEBUG:
    print("THESE ARE .png CASES: ", jsonList)

# This will create and write known extension files to "FileListUnsorted.json"
jsonFile = open("FileListUnsorted.json", "w")
jsonFile.write(jsonList)
jsonFile.close()