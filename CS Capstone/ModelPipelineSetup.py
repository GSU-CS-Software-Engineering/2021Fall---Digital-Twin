import os
import json
import sys

print("Running directory check...")
dirName = ["DTPipeline","DTPipeline/Pre-processed","DTPipeline/Processed","DTPipeline/Recipes","DTPipeline/Settings","DTPipeline/Settings/Batch Settings","DTPipeline/Settings/Temp","DTPipeline/BackupCopies"]
missingDir = []
for dir in dirName:
    if not os.path.exists(dir):
        missingDir.append(dir)
if (len(missingDir) > 0):
    print("The following directories could not be found: ")
    for dir in missingDir:
        print(dir)
    print("")
else:
    print("All directories were successfully validated.")

print("Running File check...")
fileName = ["DTPipeline/Settings/Batch Settings/Settings.txt","DTPipeline/Settings/Temp/fileExtensions.json","DTPipeline/Settings/Temp/ProcessingState.json"]
missingFile = []
for file in fileName:
    if not os.path.exists(file):
            missingFile.append(file)
if (len(missingFile) > 0):
    print("The following files could not be found: ")
    for file in missingFile:
        print(file)
    print("")
else:
    print("All files were successfuly validated.")
    from ProcessState import setProcessState
    setProcessState(1) #modelPipelineSetup.py finished

if (len(missingDir) > 0 or len(missingFile) > 0):
    result = input("Would you like to set up the listed required directories and files? (Y/N)\n")
    while ((result != 'Y' and result != 'y' and result != 'N' and result != 'n')):
        result = input("Please enter a decision (Y/N): ")
    if (result == 'Y' or result == 'y'):
        for dir in missingDir:
            #Create target Directory if it does not already exist
            if not os.path.exists(dir):
                os.mkdir(dir)
                print("Directory " +dir +" created.")
            else:
                print("Directory " +dir +" already exists")
        for file in missingFile:
            #Create target file if it does not already exist
            try:
                if (file == "DTPipeline/Settings/Temp/ProcessingState.json"):
                    try:
                        data = {}
                        #Write file to disk
                        file = open("DTPipeline/Settings/Temp/ProcessingState.json", 'w')
                        with file as outfile:
                            data['ProcessingState'] = 2
                            json.dump(data, outfile)
                            file.close()
                            print("Processing State Updated: " +str(2))
                    except FileExistsError:
                        print("Error overwriting file: " +file)
                elif (file == "DTPipeline/Settings/Temp/fileExtensions.json"):
                    try:
                        data = {}
                        data['knownFileExtensions'] = {}
                        data['knownFileExtensions'][0] = ".MODEL"
                        data['knownFileExtensions'][1] = ".CATPart"
                        data['knownFileExtensions'][2] = ".CATProduct"
                        data['ignoredFileExtensions'] = {}
                        data['knownRecipeExtensions'] = {}
                        data['ignoredRecipeExtensions'] = {}
                        #Write file to disk
                        file = open("DTPipeline/Settings/Temp/fileExtensions.json", 'w')
                        with file as outfile:
                            json.dump(data, outfile)
                            file.close()
                    except FileExistsError:
                        print("Error overwriting file: " +file)
                else:
                    #Write file to disk
                    with open(file, 'w') as outfile:
                        print("File " +file +" created.")
            except FileExistsError:
                print("File " +file +" already exists")
        from ProcessState import setProcessState
        print("From: "+str(sys.argv[0]))
        setProcessState(1) #modelPipelineSetup.py finished
    else:
        print("First time setup aborted.\nExiting.")
        if (os.path.exists("DTPipeline/Settings/Temp/ProcessingState.json")):
            from ProcessState import setProcessState
            print("From: "+str(sys.argv[0]))
            setProcessState(-1) #modelPipelineSetup.py finished
        sys.exit()
