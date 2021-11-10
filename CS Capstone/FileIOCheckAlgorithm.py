#!/usr/bin/python

import os, sys, json
from csv import DictReader
#import PipelineController

# This is the collection of known file extensions that should be processed
def acceptable_ext():
    fileName = open('KnownExt.csv', 'r')
    try:
        if DEBUG:
            print("ITERATING THESE FILES TO COMPARE TO KNOWN EXTENSIONS FROM CSV FILE")
        with fileName as read_obj:
            try:
                csv_dict_reader = DictReader(read_obj)
                for each in list_Entry:
                    if DEBUG:
                        print(each)
                    for row in csv_dict_reader:
                        if DEBUG:
                            print("CAD: ", row['CAD'], " IMAGE: ", row['IMAGE'])
                        if each.endswith(row['CAD']):
                            list_Unsorted.append(each)
                        if each.endswith(row['IMAGE']):
                            list_Unsorted.append(each)
            finally:
                fileName.close()
            
    except TypeError:
        print("No valid extension type files found")
        
        
# This will collect files within the current directory    
def files_only(): 
    try:
        if DEBUG:
            print("THESE ARE ALL THE FILES WITHIN THE PATH DIRECTORY: ")
        files = [entry for entry in os.listdir(os.curdir)]
        for entry in files:
            if os.path.isfile(entry):
                list_Entry.append(entry)
                if DEBUG:
                    print(entry)
    except OSError:
        print("No files found in this directory")
        
        
# This will create and write acceptable-known-extension files to "FileListUnsorted.json"
def writeToJson(list_Unsorted):
    try:
        jsonList = json.dumps(list_Unsorted)
        jsonFile = open("FileListUnsorted.json", "w")
        jsonFile.write(jsonList)
        jsonFile.close()
        return jsonList

    except:
        print("Some error occurred")
    
        
# This is set to 'True' for debug of output data
DEBUG = True

list_Entry=[]
list_Unsorted=[]

# Change the working directory to find import and setting files
path = "DTPipeline\Settings\Batch Settings\\"
try:
    os.chdir(path)
except NotADirectoryError:
    print("[{0} is not a directory".format(path))

files_only()
acceptable_ext()    
finalList = writeToJson(list_Unsorted)

if DEBUG:
    print("THESE ARE ACCEPTABLE CASES: ", list_Unsorted)
    print("FINAL FILTERED FILES: ", finalList)
#PipelineController.setProcessState(1)
exit()
