import os
import sys
import json
import glob

#initialize variables

#Read a json file
file1 = open("DTPipeline/Settings/Temp/fileExtensions.json", 'r')
with file1 as json_file1:
    fileExtensionsJson = json.load(json_file1)
    file1.close()
fileExtensions = [] #list of known extensions
for item in fileExtensionsJson['knownFileExtensions']:
    fileExtensions.append(item)

ignoredExtensions = [] #list for ignored file extensions
for item in fileExtensionsJson['ignoredFileExtensions']:
    ignoredExtensions.append(item)

recipeExtensions = [] #list of known recipe extensions
for item in fileExtensionsJson['knownRecipeExtensions']:
    recipeExtensions.append(item)

ignoredRecipeExtensions = [] #list for ignored recipe extensions
for item in fileExtensionsJson['ignoredRecipeExtensions']:
    ignoredRecipeExtensions.append(item)

recipeList = []
preProcessedFiles = {} #json dictionary
fileCount = -1 #global file count for each list
listCount = -1 #start list count at negative 1 so that list count is incremented to 0

for root, dirs, files in os.walk('DTPipeline/Recipes'):
    for file in files:
        ignoreExt = False
        for iExt in ignoredRecipeExtensions:
            if (file.endsWith(iExt)):
                ignoreExt = True
        if (ignoreExt == False):
            knownExt = False
            for ext in recipeExtensions:
                if (file.endswith(ext)):
                    knownExt = True
                    if (knownExt == True):
                        recipeList.append(os.path.join(root, file))
            if (knownExt == False):
                print("Warning, the extension for the file: "+file+" was not an expected extension.")
                print("To add the extension to the list of expected file extensions, enter the word: add")
                print("To add the extension to the list of ignored file extensions, enter the word: ignore")
                print("To remove "+file+" from the Pre-processed directory, enter the word: remove")
                decision = input("To ignore this file during this run, enter the word: unlist\n")
                validInput = False
                while (validInput == False):
                    if (decision == "add" or decision == "ignore" or decision == "remove" or decision == "unlist"):
                        validInput = True
                        if (decision == "add"):
                            fileWithExtension = os.path.splitext(file)
                            recipeExtensions.append(fileWithExtension[1])
                        elif (decision == "ignore"):
                            fileWithExtension = os.path.splitext(file)
                            ignoredRecipeExtensions.append(fileWithExtension[1])
                        elif (decision == "remove"):
                            os.remove(os.path.join(root, file))
                        else:
                            print("Ignoring file: "+file)
                    else:
                        validInput = False
                    if (validInput == False):
                        print("The previous entry: "+decision +" could not be processed.")
                        decision = input("Please enter one of the following keywords: \nadd \nignore \nremove \nunlist \n")


if (len(recipeList) > 1):
    iteration = 0
    validInput = False
    while (validInput == False):
        print("List of recipe files discovered: ")
        sorted(recipeList)
        for recipe in recipeList:
            print(recipe)
        recipe = input("Warning, multiple recipe files were discovered. \nPlease enter the file name and extension of the recipe for this batch: \n")
        for file in recipeList:
            if (recipe == file):
                validInput = True
                listCount += 1
                preProcessedFiles[listCount] = {}
                preProcessedFiles[listCount]['settingsFile'] = file
                preProcessedFiles[listCount]['conversionFileList'] = {}
        if (validInput == False):
            print("The selected file "+recipe+" was not found, please enter a valid filename from the following: ")
            print(recipeList)
        iteration += 1
elif (len(recipeList) == 0):
    from ProcessState import setProcessState
    print("From: "+str(sys.argv[0]))
    setProcessState(-1)
    sys.exit()
else:
    listCount = 0
    preProcessedFiles[listCount] = {}
    preProcessedFiles[listCount]['settingsFile'] = recipeList[0]
    preProcessedFiles[listCount]['conversionFileList'] = {}

for root, dirs, files in os.walk('DTPipeline/Pre-processed'):
    for file in files:
        if (os.path.exists('DTPipeline/Settings/Temp/jobQueue.json')):
            #Read a json file
            file2 = open('DTPipeline/Settings/Temp/jobQueue.json', 'r')
            with file2 as json_file2:
                data = json.load(json_file2)
                file2.close()
                for batchID in data['jobQueue']:
                    for jobID in data['jobQueue'][batchID]:
                        for fileID in data['jobQueue'][batchID][jobID]:
                            if (data['jobQueue'][batchID][jobID][fileID]['filePriority'] != 0 and file != data['jobQueue'][batchID][jobID][fileID]['fileName']):
                                ignoreExt = False
                                for iExt in ignoredExtensions:
                                    if (file.endswith(iExt)):
                                        ignoreExt = True
                                if (ignoreExt == False):
                                    knownExt = False
                                    for ext in fileExtensions:
                                        if (file.endswith(ext)):
                                            knownExt = True
                                            if (knownExt == True):
                                                fileCount += 1
                                                #If file extension is known, add it to the proper location in the json object
                                                preProcessedFiles[listCount]['conversionFileList'][fileCount] = {}
                                                preProcessedFiles[listCount]['conversionFileList'][fileCount]['filePath'] = root
                                                preProcessedFiles[listCount]['conversionFileList'][fileCount]['fileName'] = file

                            else:
                                print("File: "+file+" has already been added to the queue, skipping.")
        else:
            ignoreExt = False
            for iExt in ignoredExtensions:
                if (file.endswith(iExt)):
                    ignoreExt = True
            if (ignoreExt == False):
                knownExt = False
                for ext in fileExtensions:
                    if (file.endswith(ext)):
                        knownExt = True
                        if (knownExt == True):
                            fileCount += 1
                            #If file extension is known, add it to the proper location in the json object
                            preProcessedFiles[listCount]['conversionFileList'][fileCount] = {}
                            preProcessedFiles[listCount]['conversionFileList'][fileCount]['filePath'] = root
                            preProcessedFiles[listCount]['conversionFileList'][fileCount]['fileName'] = file

                if (knownExt == False):
                    print("Warning, the extension for the file: "+file+" was not an expected extension.")
                    print("To add the extension to the list of expected file extensions, enter the word: add")
                    print("To add the extension to the list of ignored file extensions, enter the word: ignore")
                    print("To remove "+file+" from the Pre-processed directory, enter the word: remove")
                    decision = input("To ignore this file during this run, enter the word: unlist\n")
                    validInput = False
                    while (validInput == False):
                        if (decision == "add" or decision == "ignore" or decision == "remove" or decision == "unlist"):
                            validInput = True
                            if (decision == "add"):
                                fileWithExtension = os.path.splitext(file)
                                fileExtensions.append(fileWithExtension[1])
                            elif (decision == "ignore"):
                                fileWithExtension = os.path.splitext(file)
                                ignoredExtensions.append(fileWithExtension[1])
                            elif (decision == "remove"):
                                os.remove(os.path.join(root, file))
                            else:
                                print("Ignoring file: "+file)
                        else:
                            validInput = False
                        if (validInput == False):
                            print("The previous entry: "+decision +" could not be processed.")
                            decision = input("Please enter one of the following keywords: \nadd \nignore \nremove \nunlist \n")
try:
    #Write file to disk
    file1 = open('DTPipeline/Settings/Temp/fileListUnsorted.json', 'w')
    with file1 as outfile1:
        json.dump(preProcessedFiles, outfile1)
        file1.close()
except FileExistsError:
    print("File already exists")

try:
    fileExtensionsJson['knownFileExtensions'] = fileExtensions #list of known extensions
    fileExtensionsJson['ignoredFileExtensions'] = ignoredExtensions #list for ignored extensions
    fileExtensionsJson['knownRecipeExtensions'] = recipeExtensions #list of known recipe extensions
    fileExtensionsJson['ignoredRecipeExtensions'] = ignoredRecipeExtensions #list for ignored recipe extensions

    file2 = open('DTPipeline/Settings/Temp/fileExtensions.json', 'w')
    #Write file to disk
    with file2 as outfile2:
        json.dump(fileExtensionsJson, outfile2)
        file2.close()
except FileExistsError:
    print("File already exists")

#Set the process state to 3
from ProcessState import setProcessState
print("From: "+str(sys.argv[0]))
setProcessState(3)
